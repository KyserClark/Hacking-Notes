# Linux Shell Stabilization

```
/bin/bash -i
```
```
/bin/bash -p
```

## Netcat Shell Stabilization

### Technique #1
1. Run this command: (replace "python" with "python2" or "python3" as required)
```
python -c 'import pty;pty.spawn("/bin/bash")'
```
```
python2 -c 'import pty;pty.spawn("/bin/bash")'
```
```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
2. Give access to term commands such as clear with this command:
```
export TERM=xterm
```
3. *Background shell with Ctrl+Z*
4. Give tab autocomplete, arrow keys, and Ctrl+C and foregrounds the shell with this command:
```
stty raw -echo; fg
```
*******************************************************************************
### Technique #2 (Useful with Windows Shells)
1. Install rlwrap:
```
sudo apt install rlwrap
```
2. Start rlwrap netcat listener:
```
rlwrap nc -lvnp [PORT]
```
3. *Background shell with Ctrl+Z*
4. Stabilize and foreground shell:
```
stty raw -echo; fg
```
*******************************************************************************

### Reference

* https://tryhackme.com/room/introtoshells
