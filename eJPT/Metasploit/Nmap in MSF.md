# Nmap in MSF

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## Output Nmap Scan in XML
```
Nmap [SCAN-OPTIONS] -oX [OUTFILE] 
```

***********************************************************************

## Import Nmap into MSF

Create a new workspace:
```
workspace -a [NAME]
```
Import:
```
db_import [PATH-TO-FILE]
```
Confirm successful import:
```
hosts
```
```
services
```

***********************************************************************

## Perform Nmap Scan within MSF

```
db_nmap [USE-NORMAL-NMAP-COMMAND-OPTIONS]
```
* The output is saved to MSF automatically  

Check for Vulnerabilities:
```
vulns
```

***********************************************************************

### References
Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2