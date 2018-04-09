# How It Works

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

