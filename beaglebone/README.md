Some notes on setting up the BeagleBone Black board.

## Bringup
### Hardware
1. Beaglebone Black
2. miniUSB to USB-A cable
3. USB to UART adapter (e.g. FT232 cable)

- Power up from the miniUSB cable
- BBB's IP is `192.168.7.2`. Fire it up from your browser.
- Run the example in `BeagleBone/Black/blinkLED.c`. LED3 (check USB client pins) starts blinking

### Pinout
<div style="text-align: center;">
<img src="img/pinout.avif" alt="BBB pinout" style="width:80%">
</div>

For detailed info, check the [Software Reference Manual](beaglebone/docs/BBB_SRM.pdf).
### Serial login

Check the pinout image from above:  
RX --> pin 4 of J1  
TX --> pin 5 of J1  
GND --> pin 1 of J1 (or pick any black pin from pinout image...)

Then:  
`picocom -b 115200 --imap lfcrlf /dev/ttyUSBX`

### SSH
`ssh debian@192.168.7.2`  
password is: temppwd