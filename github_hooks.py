from flask import Blueprint, render_template, abort

"""
Github Webhook Endpoint

Also see

    https://bitbucket.org/atlassianlabs/webhook-listener/src/master/listener.py
"""

github_route = Blueprint('github_route', __name__)

@github_route.route('/github')
def github():
    """Endpoint for receiving github webhooks."""
    if request.method == "POST":
        data = request.get_json()
        print("Webhook received!")
        print(data)
        return "OK"
    else:
        return display_html(request)

