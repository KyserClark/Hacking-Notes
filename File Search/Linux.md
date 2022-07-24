# Linux File Search

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Find a File by Name
```
find / -name [file-name] 2>/dev/null
```

### Find Files with SUID Bit Set
```
find / -perm -u=s -type f 2>/dev/null
```

### Display Kernel Information
```
uname -r
```
