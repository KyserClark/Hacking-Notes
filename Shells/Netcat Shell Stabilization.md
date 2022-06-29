# Netcat Shell Stabilization

## Technique #1
```
python -c 'import pty;pty.spawn("/bin/bash")'
```
(replace python with python2 or python3 as required)
```
export TERM=xterm
```
(gives access to term commands such as clear)

*Background shell with Ctrl+Z*
```
stty raw -echo; fg
```
(gives tab autocomplete, arrow keys, and Ctrl+C and forgrounds the shell)
######################################################################################
## Technique #2 (Useful with Windows Shells)

sudo apt install rlwrap

rlwrap nc -lvnp [PORT]

*Background shell with Ctrl+Z*
stty raw -echo; fg

######################################################################################

## Reference
* https://tryhackme.com/room/introtoshells
