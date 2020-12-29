from machine import Pin, I2C
import time

device_id = 64
read_delay = 6

ob_i2c = I2C(1, scl=Pin(14), sda=Pin(13), freq=400000)

def init():
    config = bytearray([2, 22, 0])
    ob_i2c.writeto(device_id, config)

def read():
    ob_i2c.writeto(device_id, bytearray([0]))
    time.sleep_ms(read_delay)
    output = ob_i2c.readfrom(device_id, 4)
    output_int = int.from_bytes(output, 'big')
    temp = (output_int >> 16)/(2**16)*165-40
    rh = (output_int & 65535)/(2**16)*100
    return [temp, rh]

def heat(duration):
    config = bytearray([2, 54, 0])
    ob_i2c.writeto(device_id, config)
    start = time.ticks_ms()
    delta = time.ticks_diff(time.ticks_ms(), start)
    while (delta < duration):
        read()
        delta = time.ticks_diff(time.ticks_ms(), start)
    init()
    return read()


# Ensure device is initialized before first call
init()
