# Accessing u-boot with picocom to transfer files via serial interface

1. Install x/y/zmodem file transfer protocols  
Arch: `pacman -S lrzsz`

## Host
`picocom --baud 115200 --send-cmd="lrzsz-sb -vv" --receive-cmd="lrzsz-rb -vvv" /dev/ttyUSB0`

## Target
```
U-Boot# loady
## Ready for binary (ymodem) download to 0x80200000 at 115200 bps...
```

Type `Ctl+a, Ctl+s` and choose the file:

```
*** file: path/to/uEnv.txt
$ lrzsz-sb -vv path/to/uEnv.txt
Sending: uEnv.txt
Bytes Sent:    384   BPS:43                              
Sending: 
Ymodem sectors/kbytes sent:   0/ 0k
Transfer complete

*** exit status: 0 ***

## Total Size      = 0x00000172 = 370 Bytes
```

To import the variables:  
`env import -t 0x80200000 370`