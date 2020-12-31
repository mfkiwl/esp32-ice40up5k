name = blink

all: $(name).v $(name).pcf
	make clean ;
	yosys -p 'synth_ice40 -top top -json $(name).json' $(name).v ;
	nextpnr-ice40 --up5k --package sg48 --json $(name).json --pcf $(name).pcf --asc $(name).asc
	icepack $(name).asc $(name).bin

clean: 
	rm -f *.bin *.asc *.blif *.json