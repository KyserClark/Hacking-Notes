# Linux File Search

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
