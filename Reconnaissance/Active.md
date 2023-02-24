# Active Reconnaissance

* FoxyProxy - quickly change proxy servers, very useful when using Burp Suite
* User-Aget Switcher and Manager - pretend to be accessing webpages from different OS and browser
* Wappalyzer - provides insights about technology used on visited websites
* Ping
* Traceroute
* Telnet
* Netcat

## DNS
```
host
```
Zone Transfer
```
host -l [DOMAIN] [DNS-SERVER-ADDRESS]
```
```
dnsrecon -d [DOMAIN] -t axfr
```
Brute force:
```
dnsrecon -d [DOMAIN] -D [WORDLIST] -t brt 
```  
  
```
dnsenum [DOMAIN]
```

```
nmap --script=dns-zone-transfer -p 53 [DOMAIN]
```

## Port Scanning

### netcat 

TCP:
```
nc -nvv -w 1 -z [IP-ADDRESS] [PORT-RANGE]
```

UDP:
```
nc -nvv -u -w 1 -z [IP-ADDRESS] [PORT-RANGE]
```

### nmap

* https://github.com/KyserClark/Hacking-Notes/blob/main/Nmap/Scan%20Types.md


 
  

## Reference
* https://tryhackme.com/room/activerecon
