# Netcat Shell Stabilization

## Technique #1
1. Run this command: (replace "python" with "python2" or "python3" as required)
```
python -c 'import pty;pty.spawn("/bin/bash")'
```
2. Run this command:(gives access to term commands such as clear)
```
export TERM=xterm
```
3. *Background shell with Ctrl+Z*
4. Run this command: (gives tab autocomplete, arrow keys, and Ctrl+C and forgrounds the shell)
```
stty raw -echo; fg
```
*******************************************************************************
## Technique #2 (Useful with Windows Shells)

sudo apt install rlwrap

rlwrap nc -lvnp [PORT]

*Background shell with Ctrl+Z*
stty raw -echo; fg

*******************************************************************************

## Reference
* https://tryhackme.com/room/introtoshells
