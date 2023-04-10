# Sever Message Block (SMB)

* [Connect to Share via Windows CLI](#connect-to-share-via-windows-cli)
* [nmap](#nmap)
* [smbmap](#smbmap)
* [Metasploit](#metasploit)
* [nmblookup](#nmblookup)
* [smbclient](#smbclient)
* [rpcclient](#rpcclient)
* [enum4linux](#enum4linux)
* [hydra](#hydra)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## Connect to Share via Windows CLI
```
net use z: \\[TARGET-IP]\c$ [PASSWORD] /user:[USERNAME]
```

***********************************************************************

## nmap

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
* SMB OS Discovery
```
nmap -p [PORT] --script smb-os-discovery [TARGET-IP]
```

***********************************************************************

## smbmap
```
smbmap -H [TARGET-IP]
```
```
smbmap -H [TARGET-IP] -v
```
```
smbmap -u [USERNAME] -p [PASSWORD] -d . -H [TARGET-IP]
```
```
smbmap -u guest -p "" -d . -H [TARGET-IP]
```
```
smbmap -u [USERNAME] -p "[PASSWORD]" -d . -H [TARGET-IP] -x [COMMAND-TO-RUN]
```
* -L to list drives
* -r to look at contents: -r '[DRIVE-LETTER]'$ | Example: -r 'c$'
* --upload '[FILE-PATH]' '[DESTINATION] | Example: --upload '/root/backdoor' 'C$\backdoor'
* --download '[FILE-PATH]' | Example: --download 'C$\flag.txt'

***********************************************************************

## Metasploit
```
msfconsole
```
```
use auxilary/scanner/smb/[SMB-VERSION]
```
Example:
```
use auxilary/scanner/smb/smb2
```
```
use auxilary/scanner/smb/smb_enumshares
```
```
use auxilary/scanner/smb/smb_login
```
```
use auxilary/scanner/smb/pipe-auditor
```
```
show options 
```
* set fields
```
exploit
```

***********************************************************************

## nmblookup
```
nmblookup -A [TARGET-IP]
```

***********************************************************************

## smbclient
* Null login
```
smbclient -L [TARGET-IP] -N
```
```
smbclient //[TARGET-IP]/[SHARE] -N
```
* Authenticated login
```
smbclient -L [TARGET-IP] -U [USERNAME]
```
```
smbclient //[TARGET-IP]/[SHARE] -U [USERNAME]
```

***********************************************************************

## rpcclient
```
rpcclient -U "[USERNAME]" -P "[PASSWORD]" [TARGET-IP]
```
```
rpcclient -U "" -N [TARGET-IP]
```
* Command below is only for AFTER connection is made with rpcclient
Service info
```
srvinfo
```
* Show users
```
enumdomusers
```
```
lookupnames [USERNAME]
```
* Show groups
```
enumdomgroups
```

***********************************************************************

## enum4linux
* OS info
```
enum4linux -o [TARGET-IP]
```
* Show users
```
enum4linux -U [TARGET-IP]
```
* Show user SIDs
```
enum4linux -r -u "[USERNAME]" -p "[PASSWORD]" [TARGET-IP]
```
* Show groups
```
enum4linux -G [TARGET-IP]
```
* Show shares
```
enum4linux -S [TARGET-IP]
```
* See if printing is set up
```
enum4linux -i [TARGET-IP]
```

***********************************************************************

## hydra
```
hydra -l [USERNAME] -P [PATH-TO-WORDLIST] [TARGET-IP] smb
```

***********************************************************************

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
