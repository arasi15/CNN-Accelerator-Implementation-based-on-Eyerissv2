import cv2
# from r03_find_optimal_bit_for_weights import convert_to_fix_point
import numpy as np
import random

# from a00_common_functions import prepare_image_from_camera

def convert_to_fix_point(arr1, bit):
    arr2 = arr1.copy().astype(np.float32)
    arr2[arr2 < 0] = 0.0
    arr2 = np.round(np.abs(arr2) * (2 ** bit))
    arr3 = arr1.copy().astype(np.float32)
    arr3[arr3 > 0] = 0.0
    arr3 = -np.round(np.abs(-arr3) * (2 ** bit))
    arr4 = arr2 + arr3
    return arr4.astype(np.int64)
def prepare_image_from_camera(im_path):
    Verilog_flag=0
    img = cv2.imread(im_path)
    print('Read image: {} Shape: {}'.format(im_path, img.shape))
    img=cv2.resize(img, (510,510), interpolation=cv2.INTER_CUBIC)
    # print(img[0,0])
    # cv2.imwrite(".\\lena_resize.png",img)
    # Take central part of image with size 224х224
    # img = img[8:-8, 48:-48]
    print('Reduced shape: {}'.format(img.shape))

    # Convert to grayscale with human based formulae https://samarthbhargav.wordpress.com/2014/05/05/image-processing-with-python-rgb-to-grayscale-conversion/
    # Divider here is 16 for easier implementation of division in verilog for FPGA.
    # Colors are in BGR order
    gray = np.zeros(img.shape[:2], dtype=np.uint16)
    gray[...] = 3*img[:, :, 0].astype(np.uint16) + 8*img[:, :, 1].astype(np.uint16) + 5*img[:, :, 2].astype(np.uint16)
    gray //= 16
    print(gray[:3])

    # Invert color (don't need this)
    # gray = 255 - gray
    # show_image(gray.astype(np.uint8))
    output_image=gray
    # Rescale to 28x28 using mean pixel for each 8x8 block
    # output_image = np.zeros((28, 28), dtype=np.uint8)
    # for i in range(28):
    #     for j in range(28):
    #         output_image[i, j] = int(gray[i*8:(i+1)*8, j*8:(j+1)*8].mean())

    # Check dynamic range
    min_pixel = output_image.min()
    max_pixel = output_image.max()
    print('Min pixel: {}'.format(min_pixel))
    print('Max pixel: {}'.format(max_pixel))

    # Rescale dynamic range if needed (no Verilog implementation, so skip)
    if Verilog_flag:
        if min_pixel != 0 or max_pixel != 255:
            if max_pixel == min_pixel:
                output_image[:, :] = 0
            else:
                output_image = 255 * (output_image.astype(np.float32) - min_pixel) / (max_pixel - min_pixel)
                output_image = output_image.astype(np.uint8)

    if Verilog_flag:
        u = np.unique(output_image, return_counts=True)
        print(u)

    # Check image (rescaled x10 times)
    # show_resized_image(output_image, 280, 280)
    return output_image
def main():
    for num2test in range(1):
        img_path = '.\\lena.png'
        verilog_path = '.\\lena_pixel.txt'
        image = prepare_image_from_camera(img_path)
        prob=0.01
        thres=1-prob
        noise=0
        pixel_mf=np.zeros((510,510))
        # print(image_binary)
        if noise:
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    rdn = random.random()
                    if rdn < prob:
                        image[i][j] = 0
                    elif rdn > thres:
                        image[i][j] = 255

        image_one = image / 256.
        image_binary = convert_to_fix_point(image_one, 15)
        with open(verilog_path, 'w') as file:
            for i in range(image_binary.shape[0]):
                for j in range(image_binary.shape[1]):
                    pixel = image[i][j]
                    pixel_one = image_one[i][j]
                    pixel_binary = image_binary[i][j]
                    if i==0 or j==0 or i==image_binary.shape[0]-1 or j==image_binary.shape[1]-1:
                        pass
                    else:
                        pixel_mf[i][j] = int(image[(i-1):(i + 2),(j-1):(j+2)].sum()/9.0)
                    file.write('{:016b}\n'.format(pixel))
        file.close()
        # print(pixel_mf[20,15:20],image[20,15:20])
        # cv2.imwrite(".\\lena_gray.png", image*255)
        cv2.imwrite(".\\lena_mf_python.png",pixel_mf)
        print(pixel_mf)

if __name__ == '__main__':
    main()