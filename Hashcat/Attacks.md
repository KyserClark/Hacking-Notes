# Hashcat

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

## Basic Dictionary Attack
* -m = Mode (Hash Type Code)
* -a = attack mode (0 = Dictionary || 3 = Brute Force)
```
hashcat -m [HASH-TYPE-CODE] -a 0 [HASH-FILE] [WORDLIST]
```
Example:
```
hashcat -m 1800 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```
*You can also put the raw hash value in place of the hashfile; I.E. you don't have to use a file for a single hash*

## Identify the hash 

* https://hashes.com/

*These tools may need to be installed*
```
hashid
```
```
hash-identifier
```

## Brute Force Four-Digit Pin

```
hashcat -a 3 -m [HASH-TYPE-CODE] [HASH] ?d?d?d?d
```
