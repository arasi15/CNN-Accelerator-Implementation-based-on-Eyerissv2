`timescale 1ns / 1ps

module SPad #( parameter DATA_BITWIDTH = 16,
			 parameter ADDR_BITWIDTH = 9 )
		   ( input clk,
			 input reset,
			 input read_req,
			 input write_en,
			 input [ADDR_BITWIDTH-1 : 0] r_addr,
			 input [ADDR_BITWIDTH-1 : 0] w_addr,
			 input [DATA_BITWIDTH-1 : 0] w_data,
			 output  [DATA_BITWIDTH-1 : 0] r_data
    );
	
	reg [DATA_BITWIDTH-1 : 0] mem [0 : (1 << ADDR_BITWIDTH) - 1]; 
		// default - 512(2^9) 16-bit memory. Total size = 1kB 
	reg [DATA_BITWIDTH-1 : 0] data;
	
	always@(posedge clk)
		begin : READ
			if(reset)
				data <= 0;
			else
			begin
				if(read_req) begin
					data <= mem[r_addr];
//					$display("Read Address to SPad:%d",r_addr);
				end else begin
					data <= 10101;
				end
			end
		end
	
	assign r_data = data;
	
	always@(posedge clk)
		begin : WRITE
		
    		
 		/*$display("\t\t\t\t\t Current Status:\n \
				 \t mem[0]:%d", mem[0],
				" | mem[1]:%d", mem[1],
				" | mem[2]:%d", mem[2],
				" | mem[3]:%d", mem[3],
				" | mem[4]:%d", mem[4],
				" | mem[5]:%d", mem[5],
				" | mem[8]:%d", mem[8],
				" | mem[24]:%d\n", mem[24],
				" \t\t\t\t\t mem[100]:%d", mem[100],
				" | mem[101]:%d", mem[101],
				" | mem[102]:%d", mem[102],
				" | mem[103]:%d", mem[103],
				" | mem[104]:%d", mem[104],
				" | mem[105]:%d\n", mem[105],
				" | mem[124]:%d\n", mem[124],
				" | mem[148]:%d\n", mem[148],
				" \t\t\t\t\t psum:%d", mem[500],
				" | psum:%d", mem[501],
				" | psum:%d", mem[502],
				" | psum:%d", mem[503],
				" | psum:%d", mem[504]
				); */
				 
			if(write_en && !reset) begin
				mem[w_addr] <= w_data;
			end
		end
	
endmodule
