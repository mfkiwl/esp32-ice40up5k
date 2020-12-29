# esp32-ice40up5k
Files for a dev board containing an ESP32-Wrover module and an ice40up5k-sg48 FPGA. The ESP32 runs micropython (http://micropython.org/) and uploads the binay image to the FPGA via an spi-like interface. The fpga images are compiled using Project IceStorm: http://www.clifford.at/icestorm/. The FPGA is also attached to external spi flash and ram. The intent of this board is to make fpga prototyping easier by providing simpler interfaces into and out of the FPGA and by allowing the FPGA to "piggyback" off of the ESP32.
