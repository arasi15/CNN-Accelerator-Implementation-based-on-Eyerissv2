`timescale 1ns / 1ps


module glb_psum #( parameter DATA_BITWIDTH = 16,
			 parameter ADDR_BITWIDTH = 10,
			 parameter X_dim=3,
			 parameter Y_dim =3 )
		   ( input clk,
			 input reset,
			 input read_req,
			 input write_en,
			 input [ADDR_BITWIDTH-1 : 0] r_addr,
			 input [ADDR_BITWIDTH-1 : 0] w_addr,
			 input [DATA_BITWIDTH-1 : 0] w_data,
			 output  [DATA_BITWIDTH-1 : 0] r_data,
			 input [ADDR_BITWIDTH-1 : 0] r_addr_inter,
			 input read_req_inter,
			 output  [DATA_BITWIDTH*X_dim-1 : 0] r_data_inter,
			 output reg read_en_inter

    );
	
	reg [DATA_BITWIDTH-1 : 0] mem [0 : (1 << ADDR_BITWIDTH) - 1]; 
		// default - 1024(2^10) 16-bit memory. Total size = 2kB 
	reg [DATA_BITWIDTH-1 : 0] data;
	reg [DATA_BITWIDTH*X_dim-1 : 0] data_inter;
	always@(posedge clk)
		begin : READ
			if(reset)
				data = 0;
			else
			begin
				if(read_req) begin
					data = mem[r_addr];
//					$display("Read Address to SPad:%d",r_addr);
				end else begin
					data = 10101; //Random default value to verify model
				end
			end
		end
	
	assign r_data = data;
	
	always@(posedge clk)
		begin : READ_INTER
			if(reset)
			begin
				data_inter=0;
				read_en_inter=0;
			end
			else
			begin
				if(read_req_inter) 
				begin
					
					data_inter = {mem[r_addr_inter+2],mem[r_addr_inter+1],mem[r_addr_inter]};
					
					read_en_inter=1;
				end
				else 
				begin
					data_inter=0;
					read_en_inter=0;
				end
			end
		end

	assign r_data_inter = data_inter ;
	
	always@(posedge clk)
		begin : WRITE
		
/* 				$display("\t\t\t\t\t Current Status in glb_psum:\n \
				 \t psum[0]:%d", mem[0],
				" | psum[1]:%d", mem[1],
				" | psum[2]:%d", mem[2],
				" | psum[3]:%d", mem[3],
				" | psum[4]:%d", mem[4],
				" | psum[5]:%d", mem[5],
				" | psum[6]:%d", mem[6],
				" | psum[7]:%d", mem[7],
				" | psum[8]:%d", mem[8],
				" | psum[9]:%d", mem[9]
				);
			
			$display("WriteEn: %d\n",write_en);
			$display("Write Data: %d\n",w_data);
			$display("Write Addr: %d\n\n\n",w_addr); */
			
			if(write_en && !reset) begin
				mem[w_addr] = w_data;
			end
		end
	
endmodule

