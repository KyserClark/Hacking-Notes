# Nmap Scripts

* [Enumerate SMB Shares](#enumerate-smb-shares)
* [Show SMB Mounts](#show-smb-mounts)

## Enumerate SMB Shares
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse [TARGET-IP]
```

## Show SMB Mounts
```
nmap -p [PORT] --script=nfs-ls,nfs-statfs,nfs-showmount [TARGET-IP]
```

* Items inside [Square Brackets] indicate changeable fields. Tailor them to your use case. Remove the brackets for commands to function.
