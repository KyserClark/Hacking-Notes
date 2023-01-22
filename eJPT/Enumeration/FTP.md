# FTP

* [Login](#login)
* [Hydra](#hydra)
* [nmap](#nmap)
* [References](#references)

******************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
******************************************************************************

## Login
```
ftp [TARGET-IP]
```
Login with anonymous does not require password if anonymous logins are allowed.  

***********************************************************************

## Hydra
```
hydra -L [WORDLIST-PATH] -P [WORDLIST-PATH] [TARGET-IP] ftp
```

***********************************************************************

## nmap 
Dictionary attack
```
nmap [TARGET-IP] --script ftp-brute --script-args userdb=[WORDLIST-PATH] -p 21
```
Check for anonymous logins
```
nmap [TARGET-IP] --script ftp-anon -p 21
```

***********************************************************************

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
