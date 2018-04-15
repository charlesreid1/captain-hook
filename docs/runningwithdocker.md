# Running Captain Hook in Docker

Captain Hook is a simple Python flask app.
To run it in Docker, we just need a Python
flask container.

We use [jfloff/alpine-python](https://github.com/jfloff/alpine-python) 
to create a flask application.

The Dockerfile in this directory 
creates a lightweight container
and installs flask on the first run.



