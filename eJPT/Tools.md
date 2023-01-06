# Tools

## Reconnaissance
### Passive Recon
* Firefox Add-Ons
   * BuiltWith
   * Wappalyzer  
  
* Kali Linux - Built In
   * whatweb
   * whois
   * host
   * dnsrecon
   * waf00f
      * https://github.com/EnableSecurity/wafw00f
   * theHarvester
      * https://github.com/laramies/theHarvester 
   * Wireshark

* Downloadable Tools
   * https://www.httrack.com 
      ```
      sudo apt-get install webhttrack
      ```
   * Sublist3r
      * https://github.com/aboul3la/sublist3r 
      
      
* Web Tools
   * https://who.is 
   * https://www.netcraft.com
   * https://dnsdumpster.com
   * Google Dorks
      * https://www.exploit-db.com/google-hacking-database
      * cache: 
   * https://haveibeenpwned.com

### Active Recon

* Kali Linux - Built In
   * nmap
      * https://github.com/KyserClark/Hacking-Notes/blob/main/Nmap/Scan%20Types.md 
   * Masscan
   * dnsenum
   * dig axfer 
   * fierce
   * arp-scan
   * ping
   * fpingfp

* Downloadable Tools
   * netdiscover
      ```
      sudo apt-get install netdiscover
      ```  
   * Zenmap (GUI nmap)
   * nmap Automator
   * Rustscan
   * Autorecon
      
## Enumeration

### Sever Message Block (SMB)

#### Connect to Share via Windows CLI
```
net use z: \\[TARGET-IP]\c$ [PASSWORD] /user:[USERNAME]
```

#### nmap

* Check SMB Version/Protocols/Dialects
```
nmap -p 445 --script smb-protocols [TARGET-IP]
```
* Check SMB Security
```
nmap -p 445 --script smb-security-mode [TARGET-IP]
```
* Show SMB Sessions
```
nmap -p 445 --script smb-enum-sessions [TARGET-IP]
```
* Log into SMB Share
```
nmap -p 445 --script smb-enum-sessions --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* Enumerate SMB Shares & Users
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse [TARGET-IP]
```
* After Authenticating
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* Enumerate SMB Shares & List Directories
```
nmap -p [PORT] --script=smb-enum-shares,smb-ls --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* SMB Server Stats
```
nmap -p [PORT] --script=smb-server-stats --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* Enumerate Domains
```
nmap -p [PORT] --script=smb-enum-domains --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* Enumerate Groups
```
nmap -p [PORT] --script=smb-enum-groups --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
* Enumerate Services
```
nmap -p [PORT] --script=smb-enum-services --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

#### smbmap
```
smbmap -u [USERNAME] -p "[PASSWORD]" -d . -H [TARGET-IP]
```
```
smbmap -u guest -p "" -d . -H [TARGET-IP]
```
```
smbmap -u [USERNAME] -p "[PASSWORD]" -d . -H [TARGET-IP] -x [COMMAND-TO-RUN]
```
* -L to list drives
* -r '[DRIVE-LETTER]'$ | Example: -r 'c$'
* --upload '[FILE-PATH]' '[DESTINATION] | Example: --upload '/root/backdoor' 'C$\backdoor'
* --download ['FILE-PATH] | Example: --download 'C$\flag.txt'


### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
