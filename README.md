# b-captain-hook

Captain Hook is a webhook server that listens for 
incoming webhooks from gitea and does stuff with them.

[gitea webhooks info](https://docs.gitea.io/en-us/webhooks/) 

gitea sends a payload url to an endpoint, so we need to 
have a service listening for and accepting and parsing
json at a particular web address.


