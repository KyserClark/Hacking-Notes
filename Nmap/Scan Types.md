# Nmap Scan Types
* [Nmap Live Host Discovery](#nmap-live-host-discovery)
   * [ARP Scan](#arp-scan)
   * [ICMP Echo Scan](#icmp-echo-scan)
   * [ICMP Timestamp Scan](#icmp-timestamp-scan)
   * [ICMP Address Mask Scan](#icmp-address-mask-scan)
   * [TCP SYN Ping Scan](#tcp-syn-ping-scan)
   * [TCP ACK Ping Scan](#tcp-ack-ping-scan)
   * [UDP Ping Scan](#udp-ping-scan)
* [Nmap Basic Port Scans](#nmap-basic-port-scans)
   * [TCP Connect Scan](#tcp-connect-scan)
   * [TCP SYN Scan](#tcp-syn-scan)
   * [UDP Scan](#udp-scan)
      * [Basic Options](#basic-options)
* [Nmap Advanced Port Scans](#nmap-advanced-port-scans)
   * [TCP Null Scan](#tcp-null-scan)
   * [TCP FIN Scan](#tcp-fin-scan)
   * [TCP Xmas Scan](#tcp-xmas-scan)
   * [TCP Maimon Scan](#tcp-maimon-scan)
   * [TCP ACK Scan](#tcp-ack-scan)
   * [TCP Window Scan](#tcp-window-scan)
   * [Custom TCP Scan](#custom-tcp-scan)
   * [Spoofed Source IP](#spoofed-source-ip)
   * [Spoofed MAC Address](#spoofed-mac-address)
   * [Decoy Scan](#decoy-scan)
   * [Idle (Zombie) Scan](#idle-(zombie)-scan)
      * [Advanced Options](#advanced-options)
 * [Nmap Post Port Scans](#nmap-post-port-scans)
      * [Post Scan Options](#post-scan-options)
 * [References](#references)

## Nmap Live Host Discovery

### ARP Scan
```
sudo nmap -PR -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PR -sn 10.10.86.0/24
```
**********************************************
### ICMP Echo Scan
```
sudo nmap -PE -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PE -sn 10.10.133.42/16
```
**********************************************
### ICMP Timestamp Scan
```
sudo nmap -PP -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PP -sn 192.168.100.8/28
```
**********************************************
### ICMP Address Mask Scan
```
sudo nmap -PM -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PM -sn 192.168.1.1/30
```
**********************************************
### TCP SYN Ping Scan
```
sudo nmap -PS[PORT],[PORT],[PORT] -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PS22,80,443 -sn 192.168.1.1/24
```
**********************************************
### TCP ACK Ping Scan
```
sudo nmap -PA[PORT],[PORT],[PORT] -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PA22,80,443 -sn 192.168.1.1/24
```
**********************************************
### UDP Ping Scan
``` 
sudo nmap -PU[PORT],[PORT],[PORT] -sn [TARGET-IP]/[CIDR-NOTATION]
```
Example:
```
sudo nmap -PU53,161,162 -sn 192.168.1.1/24
```
**********************************************
## Nmap Basic Port Scans

### TCP Connect Scan:	
```
sudo nmap -sT [TARGET-IP]
```

### TCP SYN Scan: 
```
sudo nmap -sS [TARGET-IP]
```

### UDP Scan
```
sudo nmap -sU [TARGET-IP]
```

#### Basic Options

Option                | Description
--------------------- | -------------
-p-                   | All ports
-p1-1023              | Ports 1-1023
-F                    | Top 100 common ports
-r                    | Scan ports in consecutive order
-T<0-5>               | -T0 being the slowest and -T5 the fastest
--max-rate 50         | Rate <= 50 packets/sec
--max-rate 15         | Rate >= 15 packets/sec
--min-parallelism 100 | At least 100 probes in parallel

*********************************************************
## Nmap Advanced Port Scans


### TCP Null Scan
```
sudo nmap -sN [TARGET-IP]
```

### TCP FIN Scan
```
sudo nmap -sF [TARGET-IP]
```

### TCP Xmas Scan
```
sudo nmap -sX [TARGET-IP]
```

### TCP Maimon Scan
```
sudo nmap -sM [TARGET-IP]
```

### TCP ACK Scan
```
sudo nmap -sA [TARGET-IP]
```

### TCP Window Scan	
```
sudo nmap -sW [TARGET-IP]
```

### Custom TCP Scan
```
sudo nmap --scanflags URGACKPSHRSTSYNFIN [TARGET-IP]
```

### Spoofed Source IP	
```
sudo nmap -S [SPOOFED-IP] [TARGET-IP]
```

### Spoofed MAC Address
```
--spoof-mac [SPOOFED-MAC]
```

### Decoy Scan
```
nmap -D DECOY_IP,ME [TARGET-IP]
```

### Idle (Zombie) Scan
```
sudo nmap -sI [ZOMBIE-IP] [TARGET-IP]
```

#### Advanced Options

Option                 | Description
---------------------- | -------------
-f                     | Fragment IP data into 8 bytes
-ff                    | Fragment IP data into 16 bytes
--source-port PORT_NUM | Specify source port number
--data-length NUM      | Append random data to reach given length
--reason               | Explains how Nmap made its conclusion
-v                     | Verbose
-vv                    | Very verbose
-d                     | Debugging
-dd                    | Detailed debugging


## Nmap Post Port Scans

### Post Scan Options

Option                  | Description
----------------------- | -------------
-sV                     | Determine service/version info on open ports
-sV --version-light     | Try the most likely probes (2)
-sV --version-all       | Try all available probes (9)
-O	                    | Detect OS
--traceroute            | Run traceroute to target
--script=SCRIPTS	      | Nmap scripts to run
-sC or --script=default | Run default scripts
-A                      | Equivalent to -sV -O -sC --traceroute
-oN                     | Save output in normal format
-oG                     | Save output in grepable format
-oX                     | Save output in XML format
-oA                     | Save output in normal, XML and Grepable formats


## References
* https://tryhackme.com/room/nmap01
* https://tryhackme.com/room/nmap02
* https://tryhackme.com/room/nmap03
* https://tryhackme.com/room/nmap04
