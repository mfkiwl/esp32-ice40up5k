import machine
from machine import SPI, Pin
import time


def upload(filename):
    # Read in the binary fpga configuration
    fpga_file = open(filename, 'rb')
    bblob = fpga_file.read()
    fpga_file.close()

    # Setup a soft SPI bus (18, 27, 19)
    spi = machine.SPI(baudrate=4000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(27))

    spi.init(baudrate=4000000)

    ICE_SS = Pin(14, Pin.OUT) # 14
    CRESET_B = Pin(25, Pin.OUT) # 25
    CDONE = Pin(26, Pin.IN) # 26

    ICE_SS.value(0)
    CRESET_B.value(0)   # Reset the FPGA
    time.sleep_ms(1)
    CRESET_B.value(1)
    time.sleep_ms(1)

    spi.write(bblob)

    for x in range(8):
        spi.write(b'0')

    print(CDONE.value())
