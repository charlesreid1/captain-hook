from flask import Blueprint, render_template, abort

"""
Gitea Webhook Endpoint
"""

gitea_route = Blueprint('simple_page', __name__,
                        template_folder='templates')

gitea_route = Blueprint('gitea_route', __name__)

@gitea_route.route('/gitea')
def gitea():
    """Endpoint for receiving gitea webhooks."""
    if request.method == "POST":
        data = request.get_json()
        print("Webhook received!")
        print(data)
        return "OK"
    else:
        return display_html(request)


