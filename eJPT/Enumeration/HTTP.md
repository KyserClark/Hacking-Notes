# HTTP

* [Internet Browser](#internet-browser)
* [nmap](#nmap)
* [Metasploit](#metasploit)
* [curl](#curl)
* [wget](#wget)
* [whatweb](#whatweb)
* [htt pie](#htt-pie)
* [dirb](#dirb)
* [browsh](#browsh)
* [lynx](#lynx)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## Internet Browser
***********************************************************************

## nmap
* --script http-enum
* --script http-headers
* -script banner
* --script http-methods --script-args http-methods.url-path=/[URL]
* --script http-webdav-scan --script-args http-methods.url-path=/[URL]

***********************************************************************

## Metasploit
```
use auxiliary/scanner/http/http_version
```
```
use auxiliary/scanner/http/brute_dirs
```
```
use auxiliary/scanner/http/robots_txt
```

***********************************************************************

## curl
```
curl [IP-ADDRESS]
```

***********************************************************************

## wget
```
wget [URL]
```

***********************************************************************

## whatweb
```
whatweb [IP-ADDRESS] 
```

***********************************************************************

## htt pie
```
http [IP-ADDRESS]
```

***********************************************************************

## dirb
```
dib [URL]
```

***********************************************************************

## browsh
```
browsh --startup-url [URL]
```

***********************************************************************

## lynx
```
lynx [URL]
```

***********************************************************************

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
