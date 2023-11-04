# Generating the initramfs using the rootfs

1. Extract the rootfs from this directory (am335x_tiny_filesystem.zip)

`unzip am335x_tiny_filesystem.zip -d rootfs && cd rootfs`

2. 
```
find . | cpio -H newc -o > ../initramfs.cpio
cat ../initramfs.cpio | gzip > ../initramfs.gz
```

3. Make the initramfs uboot friendly by attaching the uboot header with load address and other info:

    (You'll need uboot tools for this. In Arch: `pacman -S uboot-tools`)
```
mkimage -A arm -O Linux -T ramdisk -C none -a 0x80800000 -n "Root Filesystem" -d ../initramfs.gz  ../initramfs

Image Name:   Root Filesystem
Created:      Sat Nov  4 22:09:54 2023
Image Type:   ARM Linux RAMDisk Image (uncompressed)
Data Size:    3108867 Bytes = 3036.00 KiB = 2.96 MiB
Load Address: 80800000
Entry Point:  80800000
```