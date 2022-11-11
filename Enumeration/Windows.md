# Windows Enumeration

* Get users on local machine:
```
Get-LocalUser
```

* Get users that do not require a password:
```
Get-LocalUser | Where-Object -Property PasswordRequired -Match false
```

* List local machine groups:
```
Get-LocalGroup
```

* List Listening Ports:
```
Get-NetTCPConnection | Where-Object -Property State -Match Listen
```

* List recent updates on the system:
```
Get-Hotfix
```

* List backup files:
```
Get-ChildItem -Path C:\ -Include *.bak* -File -Recurse -ErrorAction SilentlyContinue
```

* List files containing API_KEY: *WARNING: THIS PRODUCES A LOT OF OUTPUT AND TAKES A WHILE TO PROCESS*  
* *The file path(s) will be listed at the end above the error output*
```
Get-ChildItem C:\* -Recurse | Select-String -pattern API_KEY
```
* List all running processes:
```
Get-Process
```
* List ACL for file path:
```
Get-Acl [FILE-PATH]
```
