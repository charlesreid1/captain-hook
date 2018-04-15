# Running Captain Hook

Captain Hook is an executable script
and should be run in the background 
or in a container as a service.

To create the webhook endpoint,
modify `config.py` to set the bind
address and port.

```plain
$ cat config.py
IP = 'A.B.C.D'
BIND_ADDR = '0.0.0.0'
BIND_PORT = 5000
```

**NOTE:** `IP` is not used in the program.

Now run `listen.py` to run the actual Flask application:

```plain
$ python hookserver.py
```

That's it!

