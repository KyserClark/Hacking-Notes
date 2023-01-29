# Enumeration

* [Port Scanning With Auxiliary Modules](#port-scanning-with-auxiliary-modules)
* [FTP](#ftp)
* [SMB](#smb)
* [HTTP](#http)
* [MySQL](#mysql)
* [SSH](#ssh)
* [SMTP](#smtp)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## Port Scanning With Auxiliary Modules

* Can't use payloads with auxiliary modules because auxiliary modules are not used for exploiting
* Rather, auxiliary modules are used for scanning and enumeration
* Good for pivoting when Nmap (and other tools) are not available after initial compromise

```
search portscan
```

After initial exploiting:
* Get Target subnet info
* Create link between Target 1 and Target 2:
```
run autoroute -s [TARGET-IP]
```

***********************************************************************

## FTP

Search for FTP auxiliary modules:
```
search type:auxiliary name:ftp
```
Check FTP version:
```
use auxiliary/scanner/ftp/ftp_version
```
Dictionary attack:
```
use auxiliary/scanner/ftp/ftp_login
```
Check for anonymous login:
```
use auxiliary/scanner/ftp/anonymous
```

***********************************************************************

## SMB

Search for SMB auxiliary modules:
```
search type:auxiliary name:smb
```
Check SMB version:
```
use auxiliary/scanner/smb/smb_version
```
Enumerate users:
```
use auxiliary/scanner/smb/smb_enumusers
```
Enumerate shares:
```
use auxiliary/scanner/smb/smb_enumshares
```
Dictionary attack:
```
use auxiliary/scanner/smb/smb_login
```

***********************************************************************

## HTTP

Search for HTTP auxiliary modules:
```
search type:auxiliary name:http
```
Check for HTTP version:
```
use auxiliary/scanner/http/http_version
```
Look at HTTP Header:
```
use auxiliary/scanner/http/http_header
```
Get robots.txt file:
```
use auxiliary/scanner/http/robots_txt
```
Get/Download file:
```
curl [FILE-PATH]
```
Directory scanning:
```
use auxiliary/scanner/http/dir_scanner
```
Interesting File Scanner:
```
use auxiliary/scanner/http/files_dir
```
Dictionary attack:
```
use auxiliary/scanner/http/http_login
```
Apache user enumeration:
```
use auxiliary/scanner/http/apache_userdir_enum
```

***********************************************************************

## MySQL

Search for MySQL auxiliary modules:
```
search type:auxiliary name:mysql
```
Check MySQL version:
```
use auxiliary/scanner/mysql/mysql_version
```
Dictionary attack:
```
use auxiliary/scanner/mysql/mysql_login
```
Enumeration Module:
```
use auxiliary/admin/mysql/mysql_enum
```
MySQL SQL Query Execution:
```
use auxiliary/admin/mysql/mysql_sql
```
Schema Dump:
```
use auxiliary/scanner/mysql/mysql_schemadump
```

***********************************************************************

# SSH

Search for SSH auxiliary modules:
```
search type:auxiliary name:ssh
```
Check SSH version:
```
use auxiliary/scanner/ssh/ssh_version
```
Dictionary attack:
```
use auxiliary/scanner/ssh/ssh_login
```
Enumerate Users:
```
use auxiliary/scanner/ssh/ssh_enumusers
```

***********************************************************************

# SMTP

Search for SMTP auxiliary modules:
```
search type:auxiliary name:smtp
```
Check SMTP version:
```
use auxiliary/scanner/smtp/smtp_version
```
User enumeration:
```
use auxiliary/scanner/smtp/smtp_enum
```

***********************************************************************

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2