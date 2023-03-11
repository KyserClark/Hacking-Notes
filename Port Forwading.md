# Port Forwarding

## Basic SSH Port Forwarding

```
ssh -L [LPORT]:localhost:[RPORT] [USERNAME]@[TARGET-IP] -fN
```

Example:
```
ssh -L 8686:127.0.0.1:80 Kyser@10.10.10.10 -fN
```

* -N 

   * Do not execute a remote command.  This is useful for just forwarding ports. Refer to the description of SessionType in ssh_config(5) for details.

* -L [bind_address:]port:host:hostport
* -L [bind_address:]port:remote_socket
* -L local_socket:host:hostport
* -L local_socket:remote_socket

    * Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side.  This works by allocating a socket to listen to either a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket.  Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either host port hostport, or the Unix socket remote_socket, from the remote machine. Port forwardings can also be specified in the configuration file.  Only the superuser can forward privileged ports.  IPv6 addresses can be specified by enclosing the address in square brackets. By default, the local port is bound in accordance with the GatewayPorts setting.  However, an explicit bind_address may be used to bind the connection to a specific address.  The bind_address of “localhost” indicates that the listening port be bound for local use only, while an empty address or ‘*’ indicates that the port should be available from all interfaces.

* -f

   * Requests ssh to go to background just before command execution.  This is useful if ssh is going to ask for passwords or passphrases, but the user wants it in the background.  This implies -n.  The recommended way to start X11 programs at a remote site is with something like ssh -f host xterm. If the ExitOnForwardFailure configuration option is set to “yes”, then a client started with -f will wait for all remote port forwards to be successfully established before placing itself in the background.  Refer to the description of ForkAfterAuthentication in ssh_config(5) for details.  
  
  
In the command "ssh -L 80:127.0.0.1:80 Kyser@10.10.10.10 -fN", the first occurrence of "80" is the local port, and the second occurrence of "80" (in "127.0.0.1:80") is the destination port on the remote side.  
  
Specifically, the command is setting up a local port forwarding rule that maps port 80 on the local host to port 80 on the remote host via an SSH tunnel. This is indicated by the "-L 80:127.0.0.1:80" argument, where "80" is the local port and "127.0.0.1:80" is the destination address on the remote side.  
  
The first "80" in the command is the local port.