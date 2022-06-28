# Nmap Scan Types
* [Nmap Live Host Discovery](#nmap-live-host-discovery)
   *[Arp Scan](#arp-scan)

## Nmap Live Host Discovery

### ARP Scan
```
sudo nmap -PR -sn MACHINE_IP/24
```

### ICMP Echo Scan:	
```
sudo nmap -PE -sn MACHINE_IP/24
```

### ICMP Timestamp Scan:
```
sudo nmap -PP -sn MACHINE_IP/24
```

### ICMP Address Mask Scan:
```
sudo nmap -PM -sn MACHINE_IP/24
```

### TCP SYN Ping Scan
```
sudo nmap -PS22,80,443 -sn MACHINE_IP/30
```

### TCP ACK Ping Scan
```
sudo nmap -PA22,80,443 -sn MACHINE_IP/30
```

### UDP Ping Scan:
``` 
sudo nmap -PU53,161,162 -sn MACHINE_IP/30
```

*********************************************************

## Nmap Basic Port Scans

TCP Connect Scan:	
```
sudo nmap -sT MACHINE_IP
```

TCP SYN Scan: 
```
sudo nmap -sS MACHINE_IP
```

UDP Scan:
```
sudo nmap -sU MACHINE_IP
```

### Options

Option        | Description
------------- | -------------
-p-           | Content Cell
Content Cell  | Content Cell

-p-	
all ports

-p1-1023
scan ports 1 to 1023

-F	
100 most common ports

-r	
scan ports in consecutive order

-T<0-5>	
-T0 being the slowest and T5 the fastest

--max-rate 50	
rate <= 50 packets/sec

--min-rate 15	
rate >= 15 packets/sec

--min-parallelism 100
at least 100 probes in parallel

*********************************************************
Nmap Advanced Port Scans


TCP Null Scan:
sudo nmap -sN MACHINE_IP

TCP FIN Scan:
sudo nmap -sF MACHINE_IP

TCP Xmas Scan:
sudo nmap -sX MACHINE_IP

TCP Maimon Scan:	
sudo nmap -sM MACHINE_IP

TCP ACK Scan:	
sudo nmap -sA MACHINE_IP

TCP Window Scan:	
sudo nmap -sW MACHINE_IP

Custom TCP Scan:	
sudo nmap --scanflags URGACKPSHRSTSYNFIN MACHINE_IP

Spoofed Source IP:	
sudo nmap -S SPOOFED_IP MACHINE_IP

Spoofed MAC Address:
--spoof-mac SPOOFED_MAC

Decoy Scan:
nmap -D DECOY_IP,ME MACHINE_IP

Idle (Zombie) Scan	
sudo nmap -sI ZOMBIE_IP MACHINE_IP


OPTIONS


Fragment IP data into 8 bytes:
-f

Fragment IP data into 16 bytes:
-ff

specify source port number:
--source-port PORT_NUM

append random data to reach given length:
--data-length NUM

explains how Nmap made its conclusion:
--reason

verbose:
-v

very verbose:
-vv

debugging:
-d

more details for debugging:
-dd

*********************************************************
Nmap Post Port Scans


OPTIONS

-sV	
determine service/version info on open ports

-sV --version-light	
try the most likely probes (2)

-sV --version-all	
try all available probes (9)

-O	
detect OS

--traceroute	
run traceroute to target

--script=SCRIPTS	
Nmap scripts to run

-sC or --script=default	
run default scripts

-A	
equivalent to -sV -O -sC --traceroute

-oN	
save output in normal format

-oG	
save output in grepable format

-oX	
save output in XML format

-oA	
save output in normal, XML and Grepable formats

## References
https://tryhackme.com/room/nmap01
https://tryhackme.com/room/nmap02
https://tryhackme.com/room/nmap03
https://tryhackme.com/room/nmap04

