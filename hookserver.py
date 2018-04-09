from .config import BIND_IP, BIND_ADDR, BIND_PORT
from os import environ
from flask import Flask, request


"""
Captain Hook Server

This runs a flask server with 
various hook endpoints.

We use flask blueprints to 
define webhooks in a modular way.
"""


app = Flask(__name__, 
            static_folder
            host=BIND_ADDR, 
            port=BIND_PORT)

def display_intro():
    """Helper method to display introduction message."""
    message = "Webhook server online! Go to http://%s:%s"%(BIND_HOST,BIND_PORT)
    print(message)

def display_html(request):
    """
    Helper method to display message in HTML format.

    :param request: HTTP request from flask
    :type  request: werkzeug.local.LocalProxy
    :returns message in HTML format
    :rtype basestring
    """
    url_root = request.url_root
    return "".join([
        """<h2>Hello World</h2>"""
        """<p>This is Captain Hook. You can configure webhooks """
        """by setting the endpoint to http://%s:%s/webhook"""%(HOST_IP,HOST_PORT)
    ])

@app.route("/", methods=["GET"])
def index():
    """Endpoint for the root of the Flask app."""
    return display_html(request)

# These imports must go after the helper methods above

from github_hooks import github_route
app.register_blueprints(github_route)

from gitea_hooks import gitea_route
app.register_blueprints(gitea_route)

if __name__ == "__main__":
    display_intro()
    app.run()

