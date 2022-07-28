# Server Message Block (SMB) | Samba

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Enumerate SMB Shares:
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse [TARGET-IP]
```
### List SMB Shares:
```
smbclient -L \\[TARGET-IP]
```
### Inspect Share:
```
smbclient //[TARGET-IP]/[SHARE-NAME]
```

### Log Into Share:
```
smbclient -U [USERNAME]//[TARGET-IP]/[SHARE-NAME]
```
```
smbclient //[TARGET-IP]/[SHARE-NAME]
```


### Recursively Download SMB Share:
(Submit username and password as nothing if the share is not secured)
```
smbget -R smb://[TARGET-IP]/[SHARE-NAME]
```

### Enumerate Specific Share to See Mounts: 
```
nmap -p [PORT] --script=nfs-ls,nfs-statfs,nfs-showmount [TARGET-IP]
```
