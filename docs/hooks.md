# The Many Hooks of Captain Hook

A webhook is, generally, any endpoint URL that accepts
a JSON payload and returns a success or error code.

For Captain Hook specifically, a webhook is an endpoint URL
like `https://hooks.charlesreid1.com/service/action`
that has two parts:

* Service - what is the service that sends the "trigger"?
    (that is, the JSON payload containing information about
    the event that was triggered.)

* Action - different repositories and webhooks will be 
    set up with different actions (building a site,
    running tests, sending messages, etc.).
    These should be built into the URL.

These are "best practices" for Captain Hook.







## Adding Hooks

To organize hooks in a modular way,
we implement webhook endpoints in 
flask using [flask blueprints](http://flask.pocoo.org/docs/0.11/blueprints/).

# Creating Endpoints: Gitea Example

```
https://hooks.charlesreid1.com/github
```

Too vague!

# Creating Endpoints: Github Example

Suppose we decide we want to create an endpoint 
that listens for webhooks coming from Github.
Then we might create a hook endpoint like,

```
https://hooks.charlesreid1.com/github
```

But that's way too vague! 
There are a dozen kinds of webhooks,
and a dozen actions we might take with each.

Instead, construct the endpoint using the 
pattern `/<service>/<action>` and use the
information in the paylod to 


```
https://hooks.charlesreid1.com/github/
```







o
