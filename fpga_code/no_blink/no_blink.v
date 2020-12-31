module top (output g, b, r);

    // Instantiate the RGB driver
    SB_RGBA_DRV RGBA_DRIVER (
        .CURREN(1),
        .RGBLEDEN(1),
        .RGB0PWM(1),
        .RGB1PWM(0),
        .RGB2PWM(0),
        .RGB0(r),
        .RGB1(g),
        .RGB2(b)
    );
    defparam RGBA_DRIVER.CURRENT_MODE = "0b1";
    defparam RGBA_DRIVER.RGB0_CURRENT = "0b000001";
    defparam RGBA_DRIVER.RGB1_CURRENT = "0b000111";
    defparam RGBA_DRIVER.RGB2_CURRENT = "0b000111";

endmodule