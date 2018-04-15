# Planning

Start by determining some information about your 
Captain Hook instance:

* What is network architecture? 
    * Are we integrating Captain Hook into existing subdomain?

* Who can trigger the web hook?
    * How to verify identity?
    * How to track source of webhook requests?
    * Creation of secret tokens?

* Plan out the routes:
    * What services?
    * What actions for each service?


## Planning: Authentication

**Short version: set up auth tokens.**

Let's talk about the question of who can trigger the web hook.

Suppose we decide we want to create an endpoint
listening for incoming Github webhooks 
that are triggered by commits to a repository
containing static content for a site.

Each time the incoming webhook hits our flask server,
we want to clone a fresh copy of the repository on
the local machine and move it to the live http 
hosting directory.

If we blindly set up our Captain Hook to receive an 
incoming webhook, blindly clone a copy of whatever url
is in the payload, and start hosting it, then anyone
who discovers our public webhook could send their own
directory of content they want to host using our web
server. Here's a repo full of pr0n links. Yikes!!!

How to resolve this?

1. The guiding principle is 
    <s>trust, but verify</s> **trust no one, verify everything.**
    Webhooks mix code execution with the internet,
    so be careful. Captain Hook should perform verification
    on _all data_ before running commands. Check the URL matches the service,
    check the user or organization is whitelisted or trusted, 
    check the IP address of the source of the request,
    check etc.

1. Webhook providers should offer a way to add a secret token 
    to the webhook request it sends. This is a way of 
    authenticating the request, as well as keeping track
    of which webhooks triggered which events (if you have 
    a common webhook that can be triggered by multiple 
    services, or multiple users, for example.)

1. If possible, establish encrypted connections directly
    with the web service. (VPN, stunnel, etc.)
    This is out of your control with third party services,
    but if you run your own gitea instance, you can set up
    a VPN between Captain Hook and the gitea server,
    and have the listener discard any requests not coming 
    from inside the VPN.

1. Verify IP address blocks, a la 
    [nickfrostatx/flask-hookserver](https://github.com/nickfrostatx/flask-hookserver).

