module top (output g, b, r);
    wire clk;
    reg [32:0] clk_div;

    // Instantiate the high-frequency clock (48 MHz)
    SB_HFOSC OSCInst1 (
        .CLKHFEN(1'b1),
        .CLKHFPU(1'b1),
        .CLKHF(clk)
    );
    defparam OSCInst1.CLKHF_DIV = "0b00";


    // Instantiate the RGB driver
    SB_RGBA_DRV RGBA_DRIVER (
        .CURREN(1),
        .RGBLEDEN(1),
        .RGB0PWM(clk_div[28] & clk_div[6] & clk_div[7] & clk_div[8]),
        .RGB1PWM(clk_div[27] & clk_div[6] & clk_div[7] & clk_div[8]),
        .RGB2PWM(clk_div[26] & clk_div[6] & clk_div[7] & clk_div[8]),
        .RGB0(r),
        .RGB1(g),
        .RGB2(b)
    );
    defparam RGBA_DRIVER.CURRENT_MODE = "0b0";
    defparam RGBA_DRIVER.RGB0_CURRENT = "0b001111";
    defparam RGBA_DRIVER.RGB1_CURRENT = "0b000111";
    defparam RGBA_DRIVER.RGB2_CURRENT = "0b000111";

    always @ (posedge clk) begin
        clk_div = clk_div + 1;
    end

endmodule
