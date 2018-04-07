# b-captain-hook

Captain Hook is a webhook server that listens for 
incoming webhooks from gitea and does stuff with them.

[gitea webhooks info](https://docs.gitea.io/en-us/webhooks/) 

gitea sends a payload url to an endpoint, so we need to 
have a service listening for and accepting and parsing
json at a particular web address.

## flask api

flask gitea api server

```
from flask import Flask
from flask.ext.hookserver import Hooks

app = Flask(__name__)
app.config['GITHUB_WEBHOOKS_KEY'] = 'xxxxxxxx'

# Request checking options
app.config['VALIDATE_IP'] = False
app.config['VALIDATE_SIGNATURE'] = True

hooks = Hooks(app, url='/desired/webhooks/path')
```


