# HTTP

* [Internet Browser](#internet-browser)
* [nmap](#nmap)
* [Metasploit](#metasploit)
* [Proxies](#proxies)
* [Nikto](#nikto)
* [SQLMap](#sqlmap)
* [XSSer](#xsser)
* [curl](#curl)
* [wget](#wget)
* [whatweb](#whatweb)
* [htt pie](#htt-pie)
* [dirb](#dirb)
* [gobuster](#gobuster)
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

## Proxies

* Burp Suite
* Zed Attack Proxy (ZAP)

***********************************************************************

## Nikto

```
nikto -h [URL] -o [OUTFILE] -Format htm
```

***********************************************************************

## SQLMap

```
sqlmap -u "[URL]"
```

***********************************************************************

## XSSer

```
xsser --url "[URL]" -p [PAYLOAD] --auto
```

***********************************************************************

## curl
```
curl [URL]
```

Check methods:
```
curl -X OPTIONS [URL]
```

Upload file:
```
curl [URL] --upload-file [FILE]
```

Delete file:
```
curl -X DELETE [URL]
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
dirb [URL]
```

***********************************************************************

## gobuster

*Should go faster than dirb*

```
gobuster dir -u [URL] -w [WORDLIST]
```

Search for specific file types:
```
gobuster dir -u [URL] -w [WORDLIST] -x [FILE-TYPE-EXTENSION-COMMA-SEPARATED] -r
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
