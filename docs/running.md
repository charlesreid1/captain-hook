# Running Captain Hook

To create the webhook endpoint,
modify `config.py` to set the bind
address and port.

```plain
$ cat config.py
BIND_IP = '0.0.0.0'
BIND_ADDR = '0.0.0.0'
BIND_PORT = 5000
```

**NOTE:** `BIND_IP` is not used to run the program,
it is just for printing endpoint information.

Next, run `listen.py` to run the actual
Flask application:

```plain
$ python hookserver.py
```

That's it!


