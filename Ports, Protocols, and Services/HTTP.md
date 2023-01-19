# HTTP

## Tools

### internet browser

### nmap
* --script http-enum
* --script http-headers
* -script banner
* --script http-methods --script-args http-methods.url-path=/[URL]
* --script http-webdav-scan --script-args http-methods.url-path=/[URL]

### Metasploit
```
use auxiliary/scanner/http/http_version
```
```
use auxiliary/scanner/http/brute_dirs
```
```
use auxiliary/scanner/http/robots_txt
```

### curl
```
curl [IP-ADDRESS]
```

### wget
```
wget [URL]
```

### whatweb
```
whatweb [IP-ADDRESS] 
```
### htt pie
```
http [IP-ADDRESS]
```
### dirb
```
dib [URL]
```
### browsh
```
browsh --startup-url [URL]
```

### lynx
```
lynx [URL]
```


### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
