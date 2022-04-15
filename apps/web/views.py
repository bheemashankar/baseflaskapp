from flask import render_template
from apps.web import web_app


@web_app.route('/heartbeat', strict_slashes=False)
def heartbeat():
    return ""


@web_app.route('/dashboard', strict_slashes=False)
def dashboard():
    return render_template('web/dashboard.html')



