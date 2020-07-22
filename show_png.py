import numpy as np
import cv2


def main():
    cls=['west_0','west_1','east_0','east_1']
    png_pixel=[]
    for direction in cls:
        txt=open(".\\lena_mf_{}.txt".format(direction),'rb')
        pixels=txt.readlines()
        # print(pixels[0][-1])
        pixels=[b'0000000000000000\r\n' if pixel==b'xxxxxxxxxxxxxxxx\r\n' else pixel for pixel in pixels]
        pixels=[int(pixel[:-2],base=2) for pixel in pixels]

        pixels=np.asarray(pixels)
        pixels=np.reshape(pixels,(85,85,3,3))
        lena_out_part=np.zeros((255,255))
        for m in range(pixels.shape[0]):
            for n in range(pixels.shape[1]):
                for i in range(pixels.shape[2]):
                    for j in range(pixels.shape[3]):
                        lena_out_part[3*m+i][3*n+j]=int(pixels[m][n][i][j]/9.0)
                        # if direction=='west_1' and lena_out_part[3*m+i][3*n+j]!=128:
                        #     print(pixels[m][n][i][j])

        png_pixel.append(lena_out_part)
    # for i in range(png_pixel[1].shape[0]):
    #     for j in range(png_pixel[1].shape[1]):
    #         if png_pixel[1][i,j]!=128:
    #             print(i,j)
    png_pixel=np.hstack((np.vstack((png_pixel[0],png_pixel[1][:-2,:])),np.vstack((png_pixel[2][:,:-2],png_pixel[3][:-2,:-2]))))
    # png_mf_python=cv2.imread(".\\lena_mf_python.png")
    # png_gray=cv2.imread(".\\lena_gray.png")

    # print(png_mf_python[:,:,0])
    cv2.imwrite(".\\lena_out.png",png_pixel)
    # print(png_pixel)
    np.savetxt(".\\png_out.txt",png_pixel,fmt="%4d")
    # np.savetxt(".\\png_mf_python.txt",png_mf_python[:,:,0],fmt="%4d")
    # np.savetxt(".\\png_gray.txt",png_gray[:,:,0],fmt="%4d")
    # print(png_mf_python==png_pixel)
if __name__=="__main__":
    main()
    # png_gray = cv2.imread(".\\lena_gray.png")
    # np.savetxt(".\\png_gray.txt", png_gray[:, :, 0], fmt="%4d")

