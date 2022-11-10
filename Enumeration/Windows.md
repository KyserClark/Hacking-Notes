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
