# Hashcat

## Basic Dictionary Attack
```
hashcat -m [HASH-TYPE-CODE] -a 0 [HASH-FILE] [WORDLIST]
```
Example:
```
hashcat -m 1800 -a 0 hashes.txt wordlists/rockyou.txt
```
