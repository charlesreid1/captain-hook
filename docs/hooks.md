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
that listens for webhooks coming from Github,
and uses them to trigger the deployment of 
static web content.

We might think to create a hook endpoint like,

```
https://hooks.charlesreid1.com/github
```

But that's way too vague! 
There are a dozen kinds of webhooks,
and a dozen actions we might take with each.

Instead, construct the endpoint using the 
pattern `/<service>/<action>`, e.g.,

```
https://hooks.charlesreid1.com/github/build-static-site
```

The flask endpoint would then be set up to extract
the name and URL of the repository from the JSON 
payload that is sent, perform any verification 
necessary, and perform a git pull to deploy
the site.

Alternatively, you might wish to add a parameter to the 
webhook endpoint, such as an alternative name.
For example, we may want to deploy a repository at

```
https://github.com/charlesreid1/dumb-project-for-boss
```

to a static site that is available at a URL like:

```
https://<static-page-url>/cool-project
```

In that case, you could create an endpoint that takes a parameter:

```
https://hooks.charlesreid1.com/github/build-static-site/cool-project
```

This is associated with the `dumb-project-for-boss` project on Github
because the final webhook is installed into that project.

