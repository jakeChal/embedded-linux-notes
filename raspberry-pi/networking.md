## USB networking

It's useful for development to leverage Ethernet via the USB gadget subsystem (especially in Pi Zero, which doesn't have an Ethernet port).
To do this:

- In `/boot/cmdline.txt` add the following after `rootwait`: `modules-load=dwc2,g_ether`
- In `/boot/config.txt` add the following in the end of the file: `dtoverlay=dwc2`

Now, if you reboot and check the boot logs (via UART) verify that `dwc2` and `g_ether` are loaded, e.g.:

```
[   10.274812] g_ether gadget.0: Ethernet Gadget, version: Memorial Day 2008
[   10.274825] g_ether gadget.0: g_ether ready
[   10.274839] dwc2 3f980000.usb: bound driver g_ether
[   10.395245] dwc2 3f980000.usb: new device is high-speed
```

- SSH on target (e.g. via serial cable or Wifi) and verify that `usb0` interface is there (e.g. via `ip a`)

- Configure the `usb0` interface:
```
echo "allow-hotplug usb0
iface usb0 inet static
        address 192.168.7.2
        netmask 255.255.255.0
        network 192.168.7.0
        broadcast 192.168.7.255
        gateway 192.168.7.1" | sudo tee -a /etc/network/interfaces
```

- `sudo ifdown usb0 && sudo ifup usb0`

- On the host:  
Example:
    - IP: 192.168.7.1
    - Subnet mask: 255.255.255.0
    - Gateway: 192.168.7.1

- Try pinging the raspberry (`ping 192.168.7.2`).  
If it doesn't work, you may need to add the following on the Pi:  
`echo options g_ether use_eem=0 > /etc/modprobe.d/g_ether.conf`  
Then reboot it.


## WiFi

- `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
- Add network configuration:
```
network={
    ssid="YourSSID"
    psk="YourPassphrase"
}
```
- `sudo systemctl restart wpa_supplicant`
- Get an IP via DHCP: `sudo dhclient -v wlan0`
- Verify IP: `ifconfig wlan0`
- Verify connection: `ping 8.8.8.8`

Another way to setup your SSID/password is via `raspi-config` menu.

Tip: If WiFi seems to be down, try to restart networking service: `systemctl restart networking`
