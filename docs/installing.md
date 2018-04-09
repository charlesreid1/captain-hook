# Installing Captain Hook

### Required Software

Captain Hook runs a flask server that listens for webhook requests from Gitea.

To use Captain Hook, you must have the following:

* Python 3
* Flask

And of course, you need something to generate web hooks.

### Installing Required Software

Clone a local copy of the repo:

```
$ git clone https://git.charlesreid1.com/bots/b-captain-hook
$ cd b-captain-hook
```

Now install required software:

```
$ pip install -r requirements.txt
```

Captain Hook itself is an executable script 
so it does not need to be installed.
It runs a server so it should be run as a 
system service.

