# Credit: https://github.com/Sq00ky/Bash-Port-Scanner

## spookyscan.sh

```
#!/bin/bash
#Variables
empty=""
#Arguments for the script
while [ "$1" != "" ]; do
	case "$1" in
		-i | --ip )		ip="$2";	shift;;
		-p | --ports )		ports="$2";	shift;;
	esac
	shift
done
#Checking if the -i is empty
if [[ $ip == $empty ]]; then
	echo "Please specify an IP address with -i"
	exit
fi
#checking is -p is empty
if [[ $ports == $empty ]]; then
	echo "Please specify the max port range -p"
	exit
fi
#Scans ports/Dumps closed ports/displays open ports
for i in $(seq 1 $ports); do
	( echo > /dev/tcp/$ip/$i) > /dev/null 2>&1 && echo $ip":"$i "is open";
done
```
