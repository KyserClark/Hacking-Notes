# Netcat Shell Stabilization

## Technique #1
1.
```
python -c 'import pty;pty.spawn("/bin/bash")'
```
(replace "python" with "python2" or "python3" as required)
2.
```
export TERM=xterm
```
(gives access to term commands such as clear)

3. *Background shell with Ctrl+Z*
4. 
```
stty raw -echo; fg
```
(gives tab autocomplete, arrow keys, and Ctrl+C and forgrounds the shell)
*******************************************************************************
## Technique #2 (Useful with Windows Shells)

sudo apt install rlwrap

rlwrap nc -lvnp [PORT]

*Background shell with Ctrl+Z*
stty raw -echo; fg

*******************************************************************************

## Reference
* https://tryhackme.com/room/introtoshells
