# SSL

* [nmap](#nmap)
* [References](#references)

***********************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
***********************************************************************

## nmap

```
nmap -sV --script ssl-enum-cipers -p [PORT] [HOST]
```
```
nmap -p [PORT] --script ssl-heartbleed [TARGET]
```

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
