def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('INSERT WIFI NAME HERE', 'INSERT PASSWORD HERE')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

from machine import Pin
red = Pin(23, Pin.OUT)
blue = Pin(5, Pin.OUT)
green = Pin(0, Pin.OUT)

red.on()
blue.off()
green.off()

import machine
machine.freq(240000000)

do_connect()

# Program FPGA
import fpga
fpga.upload('blink.bin')


red.off()
blue.on()

