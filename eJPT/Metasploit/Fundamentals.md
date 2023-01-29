# Metasploit Fundamentals 

* [Installation & Configuration](#installation--configuration)
* [Fundamentals](#fundamentals)
* [Creating & Managing Workspaces](#creating--managing-workspaces)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## Installation & Configuration

```
sudo apt-get update && sudo apt-get install metasploit-framework -y
```
```
sudo systemctl enable postgresql
```
```
sudo systemctl start postgresql
```
```
sudo systemctl status postgresql
```
```
sudo msfdb
```
```
sudo msfdb init
```
```
sudo msfdb status
```
```
msfconsole
```
```
db_status
```

***********************************************************************

## Fundamentals

Variable | Purpose
---------|---------
LHOST    | Attacker IP
LPORT    | Attacker Port
RHOST    | Target IP
RHOSTS   | Target IP Range
RPORT    | Target Port

Basic commands:  

```
help
```
```
version
```
```
show all
```
```
show exploits
```
```
show -h
```
* -h works with other commands too.
```
search [MODULE]
```
```
use [MODULE]
```
```
show options
```
```
set [VARIABLE] [VALUE]
```
Examples:
```
set RHOSTS 192.168.2.1
```
```
set PORTS 1-1000
```
```
run
```
OR
```
exploit
```
```
back
```
Search examples:  
```
search cve:2017 type:exploit platform:-windows
```
```
search eternalblue
```
```
set payload [PAYLOAD]
```
```
sessions
```
```
connect [TARGET-IP] [PORT]
```
Set global variables:
```
setg [VARIABLE]
```
Get info about a module (after use [MODULE]):
```
info
```
```
services
```
```
creds
```
```
loot
```
Check for vulnerabilities:
```
analyze
```
```
vulns
```

***********************************************************************

## Creating & Managing Workspaces

* Workspaces keep track of Metasploit activities
* Create a new workspace for each new engagement to separate client data

```
workspace -h
```
```
workspace
```
```
hosts
```
Create new workspace:  
```
workspace -a [NAME]
```
Switch workspace:
```
workspace [NAME]
```
Delete workspace:  
```
workspace -d [NAME]
```
Rename workspace:
```
workspace -r [OLD-NAME] [NEW-NAME]
```

***********************************************************************

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2