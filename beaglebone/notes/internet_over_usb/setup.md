## Host
0. Verify that you can talk to the BBB:  
```ping 192.168.7.2```

1.
```
iptables --table nat --append POSTROUTING --out-interface INTERNET_IFACE_HOST -j MASQUERADE
iptables --append FORWARD --in-interface INTERNET_IFACE_HOST -j ACCEPT
```
2. Verify that forwarding is enabled:
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

## BBB
0. Verify that you can talk to the host:  
```ping 192.168.7.1```
1. `sudo vim /etc/network/interfaces` and append the following:
```
​​iface usb0 inet static
    address 192.168.7.2
    netmask 255.255.255.252
    network 192.168.7.0
    gateway 192.168.7.1
    dns-nameservers 1.1.1.1
    post-up route add default gw 192.168.7.1
```

2. Route `default` requests via Host:  
`route add default gw 192.168.7.1`

3. Reboot and try pinging something (e.g. `ping google.com`)

--------------------
### Troubleshooting
It can be that already existing `iptables` on the host is messing up the setup for BBB. To use a pristine `iptables` setup on host: 

1. Save the current `iptables`:  
` iptables-save > path/to/savedrules.txt`

2. 

```
[root ~]# iptables -P INPUT ACCEPT
[root ~]# iptables -P FORWARD ACCEPT
[root ~]# iptables -P OUTPUT ACCEPT
[root ~]# iptables -t nat -F
[root ~]# iptables -t mangle -F
[root ~]# iptables -F
[root ~]# iptables -X
[root ~]# iptables -nvL  #Verify that iptables is cleaned up
```

3. Make sure you set again the `iptables` rules from step 1 of the Host. 

4. (Optional)  
If later on you want to restore your previous `iptables`:  
`iptables-restore < path/to/savedrules.txt `