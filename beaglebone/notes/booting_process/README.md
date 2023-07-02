## Boot from SD Card

0. SD card preparation. Example partition table: 

```
Device     Boot   Start      End  Sectors  Size Id Type  
/dev/sdb1  *       2048  2099199  2097152    1G  6 FAT16  
/dev/sdb2       2099200 14387199 12288000  5.9G 83 Linux  
```
1. ROM bootloader is already on the SoC. We need the 2nd stage bootloader (MLO):  
Get MLO image from `EmbeddedLinuxBBB/pre-built-images/Angstrom_Demo/MLO-beaglebone-2013.04`:  
E.g.  
`cp EmbeddedLinuxBBB/pre-built-images/Angstrom_Demo/MLO-beaglebone-2013.04 /run/media/jacob/BOOT/MLO`

2. We need uboot also (make sure the name of the image on the SD is `u-boot.img`):   
`cp EmbeddedLinuxBBB/pre-built-images/Angstrom_Demo/u-boot-beaglebone-2013.04-r0.img /run/media/jacob/BOOT/u-boot.img`

3. uboot needs to load the linux kernel and the DTB. To do that, we need:  
- `uEnv.txt` file, which says where to place the image in RAM  
`cp EmbeddedLinuxBBB/pre-built-images/Angstrom_Demo/uEnv.txt /run/media/jacob/BOOT`

4. Copy the rootfs to the SD card:
`tar xvf EmbeddedLinuxBBB/pre-built-images/Angstrom_Demo/Angstrom-systemd-image-eglibc-ipk-v2012.12-beagleboard.rootfs.tar.xz`    
`cp -r Angstrom-systemd-image-eglibc-ipk-v2012.12-beagleboard.rootfs/* /run/media/jacob/ROOTFS/`

5. Boot from SD card  
- Put the board in power down mode by doing a long press on power button (S3)  
- Press and hold the boot button (S2)  
- Press and release S3  
- Release S2

More detailed info on boot order & sysboot: https://fastbitlab.com/linux-device-driver-programming-lecture-6-booting-sequence-beaglebone-black-hardware/



### Uboot commands

- load image from SD card to RAM:
`load mmc 0:2 0x82000000 /boot/uImage`

- Read 4 bytes at location 0x82000000:  
`md 0x82000000 4`

- Print header information from uImage:
`imi 0x8200000`  
