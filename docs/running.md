# Running Captain Hook

Captain Hook is an executable script
and should be run in the background 
or in a container as a service.

To create the webhook endpoint,
modify `hook_config.py` to set the bind
address and port.

```plain
$ cat hook_config.py
IP = 'A.B.C.D'
BIND_ADDR = '0.0.0.0'
BIND_PORT = 5000
```

**NOTE:** `IP` is not used in the program.

Now run `hook_server.py` to run the hook server 
Flask application:

```plain
$ python hook_server.py
```

That's it!

