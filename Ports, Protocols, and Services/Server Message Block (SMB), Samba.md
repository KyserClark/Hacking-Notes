# Server Message Block (SMB) | Samba

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Enumerate SMB Shares & Users:
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse [TARGET-IP]
```
#### After Authenticating:
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### Enumerate SMB Shares & List Directories
```
nmap -p [PORT] --script=smb-enum-shares,smb-ls --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### List SMB Shares:
```
smbclient -L \\[TARGET-IP]
```

### Inspect Share:
```
smbclient //[TARGET-IP]/[SHARE-NAME]
```

### Log Into Share:
```
smbclient -U [USERNAME]//[TARGET-IP]/[SHARE-NAME]
```
```
smbclient //[TARGET-IP]/[SHARE-NAME]
```

### Recursively Download SMB Share:
(Submit username and password as nothing if the share is not secured)
```
smbget -R smb://[TARGET-IP]/[SHARE-NAME]
```

### Download Single File From Share After Logging In:
```
mget [FILE-NAME]
```

### Enumerate Specific Share to See Mounts: 
```
nmap -p [PORT] --script=nfs-ls,nfs-statfs,nfs-showmount [TARGET-IP]
```

### Check for Known Vulnerabilities within an SMB Share:
```
nmap -p [PORT] --script smb-vuln* [TARGET-IP]
```

### Check SMB Versions/Protocols/Dialects:
```
nmap -p 445 --script smb-protocols [TARGET-IP]
```

### Check SMB Security:
```
nmap -p 445 --script smb-security-mode [TARGET-IP]
```

### Show SMB Sessions:
```
nmap -p 445 --script smb-enum-sessions [TARGET-IP]
```

### Log into SMB Share:
```
nmap -p 445 --script smb-enum-sessions --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### SMB Server Stats:
```
nmap -p [PORT] --script=smb-server-stats --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### Enumerate Domains:
```
nmap -p [PORT] --script=smb-enum-domains --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### Enumerate Groups
```
nmap -p [PORT] --script=smb-enum-groups --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```

### Enumerate Services
```
nmap -p [PORT] --script=smb-enum-services --script-args smbsusername=[USERNAME],smbpassword=[PASSWORD] [TARGET-IP]
```
### SMB OS Discovery
```
nmap -p [PORT] --script smb-os-discovery [TARGET-IP]
```
### smbmap
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
* -r to look at contents: -r '[DRIVE-LETTER]'$ | Example: -r 'c$'
* --upload '[FILE-PATH]' '[DESTINATION] | Example: --upload '/root/backdoor' 'C$\backdoor'
* --download '[FILE-PATH]' | Example: --download 'C$\flag.txt'

### Metasploit
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
use auxilary/scanner/smb/pipe-auditor
```
```
show options 
```
* set fields
```
exploit
```

### nmblookup
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

### rpcclient
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

### enum4linux
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

### hydra
```
hydra -l [USERNAME] -P [PATH-TO-WORDLIST] [TARGET-IP] smb
```
