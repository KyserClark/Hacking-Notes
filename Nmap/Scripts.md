# Nmap Scripts

* [Enumerate SMB Shares](#enumerate-smb-shares)
* [Show SMB Mounts](#show-smb-mounts)
* [Check for Known Vulnerabilities within an SMB Share](#check-for-known-vulnerabilities-within-an-smb-share)

*************************************************************************************************************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*************************************************************************************************************************************************************************

## Enumerate SMB Shares
```
nmap -p [PORT] --script=smb-enum-shares.nse,smb-enum-users.nse [TARGET-IP]
```
Example:
```
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.128.86
```
***************************************************************************
## Show SMB Mounts
```
nmap -p [PORT] --script=nfs-ls,nfs-statfs,nfs-showmount [TARGET-IP]
```
Example:
```
nmap -p 139 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.128.86
```
***************************************************************************
## Check for Known Vulnerabilities within an SMB Share
```
nmap -p [PORT] --script smb-vuln* [TARGET-IP]
```
Example:
```
nmap -p 139, 445 --script smb-vuln* 10.10.75.145
```
