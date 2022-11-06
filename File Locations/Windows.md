# Windows File Locations

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

* [Powershell Command History](#powershell-command-history)
* [Look for the password Keyword in the Registry](#look-for-the-password-keyword-in-the-registry)

## PowerShell Command History
```
C:\Users\[USER]\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

********************************************

## Look for the password Keyword in the Registry

```
c:\Users\[USER]> reg query HKLM /f password /t REG_SZ /s
```
OR
```
C:\Users\[USER]> reg query HKCU /f password /t REG_SZ /s
```
