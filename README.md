# b-captain-hook

Captain Hook is a webhook server that listens for 
incoming webhooks from Gitea and does stuff with them.

[Gitea Documentation - Webhooks](https://docs.gitea.io/en-us/webhooks/) 

## Required Software

Captain Hook runs a flask server that listens for webhook requests from Gitea.

To use Captain Hook, you need to install the following:

* python 3
* flask
* flask-gitea-hookserver

And of course, you need a Gitea instance.

To install flask you can do a simple `pip install flask`.

To install `flask-gitea-hookserver` visit either link below and read the INSTALLING.md document:

* [charlesreid1/flask-gitea-hookserver](https://git.charlesreid1.com/charlesreid1/flask-gitea-hookserver) on git.charlesreid1.com - see INSTALLING.md
* [charlesreid1/flask-gitea-hookserver](https://github.com/charlesreid1/flask-gitea-hookserver) on Github - see INSTALLING.md

## How Captain Hook Works

Gitea webhooks are JSON payloads that are sent to a URL endpoint
when certain events occur. The JSON payload contains information
about what occurred and where. 

Gitea sends the payload to a URL endpoint. It's our job to run
a server that will listen at that endpoint and decide what to do
with the request.

That's where Captain Hook comes in.

Captain Hook listens for incoming webhooks from Gitea,
and is the central controller that decides what to do.

Captain Hook runs on krash.

## Creating the API

### Create a Flask App

To run a Gitea API server, 
start by creating a flask application `app`:

```
from flask import Flask
from flask.ext.hookserver import Hooks

app = Flask(__name__)
```

Next, add configuration options if desired:

```
app.config['VALIDATE_SIGNATURE'] = True
app.config['GITHUB_WEBHOOKS_KEY'] = 'xxxxxxxx'
```

Now create a Hooks object to create a webhooks server
that's linked to `app` and available at `https://yoursite.com/desired/webhooks/path`:

```
hooks = Hooks(app, url='/desired/webhooks/path')
```

### Add Route Decorators

To handle different webhooks, use decorators to associate a given function
with a given incoming webhook. 

Example from [flask-hookserver docs](https://flask-hookserver.readthedocs.io/en/latest/):

```
@hooks.hook('ping')
def ping(data, delivery):
    print(data['zen'])
    return 'pong'


@hooks.hook('push')
def new_code(data, delivery):
    print('New push to %s' % data['ref'])
    return 'Thanks'
```
