from config import IP, BIND_ADDR, BIND_PORT
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
            static_folder="static")

def display_intro():
    """Helper method to display introduction message."""
    message = "Webhook server online! Go to http://%s:%s"%(IP,BIND_PORT)
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
        """<html>""",
        """<head>""",
        """<title>bluebeard hook server</title>""",
        """<link rel="stylesheet" href="static/bootstrap.min.css" type="text/css" />""",
        """</head><body>""",
        """<div class="container"><div class="row">""",
        """<h2>Hello World</h2>""",
        """<p>This is Captain Hook the webhook server.</p>""",
        """<p>You can configure webhooks by setting the endpoint to <code>http://%s:%s/webhook</code>"""%(IP,BIND_PORT),
        """</div></div>""",
        """</body></html>"""
    ])

@app.route("/", methods=["GET"])
def index():
    """Endpoint for the root of the Flask app."""
    return display_html(request)

# These imports must go after the helper methods above

#from github_hooks import github_route
#app.register_blueprint(github_route)
#
#from gitea_hooks import gitea_route
#app.register_blueprint(gitea_route)

@app.route("/webhook", methods=["GET","POST"])
def tracking():
    if request.method == "POST":
        data = request.get_json()
        print("Webhook received!")
        print(data)
        return "OK"
    else:
        return display_html(request)


if __name__ == "__main__":
    display_intro()
    app.run( host = BIND_ADDR, 
             port = BIND_PORT)
