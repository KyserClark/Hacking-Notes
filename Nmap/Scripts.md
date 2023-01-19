# Nmap Scripts

* [Enumerate SMB Shares](#enumerate-smb-shares)
* [Show SMB Mounts](#show-smb-mounts)
* [Check for Known Vulnerabilities within an SMB Share](#check-for-known-vulnerabilities-within-an-smb-share)
* [Brute Force Domain](#brute-force-domain)
* [Detect Web Application Firewall](#detect-web-application-firewall)
* [SSL Enumeration](#ssl-enumeration)
* [Resources](#resources)

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
***************************************************************************
## Brute Force Domain
```
nmap --script=dns-brute.nse [DOMAIN]
```
Example:
```
nmap --script=dns-brute.nse KyserClark.com
```
***************************************************************************
## Detect Web Application Firewall
```
nmap --script=http-waf-detect.nse [DOMAIN]
```
Example:
```
nmap --script=http-waf-detect.nse KyserClark.com
```
***************************************************************************
## Certificate Enumeration and Inspection
```
nmap --script=ssl-cert.nse
```
***************************************************************************
## SSL Enumeration
```
nmap -sV --script ssl-enum-cipers -p [PORT] [HOST]
```
***************************************************************************
## Resources
https://nmap.org/nsedoc/index.html 
