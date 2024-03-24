### SD Card prep
- Get your OS from https://www.raspberrypi.com/software/operating-systems/
- `xz -vd your_raspios.img.xz`
- Insert SD card and identify it (e.g. with `dmesg`)
- Unmount it: `umount /dev/sdX*`
- `sudo dd bs=4M if=your_raspios.img of=/dev/sdX conv=fsync status=progress`

... OR

- Download the RPi Imager tool (e.g. in Debian: `sudo apt install rpi-imager`)
and do everything with GUI buttons :) 

### SSH
1. Add an empty file named `ssh` in the boot partition
2. Add a `userconf.txt` file, which contains a string of the format: `myUserName:encryptedpassword`.  
To generate the encrypted password: `openssl passwd -6`
3. (Optional) To be able to painlessly ssh in the raspberrypi as `ssh raspberrypi`

    In your host's machine SSH config file (`~/.ssh/config`) add:

   ```
    Host raspberrypi
    HostName <RPI_IP>
    User myUserName
   ```


4. (Optional) To be able to have passwordless ssh:  
    `ssh-copy-id -i ~/.ssh/id_rsa.pub myUserName@RPI_IP`

### First setup
`sudo apt-get update && sudo apt-get upgrade -y`