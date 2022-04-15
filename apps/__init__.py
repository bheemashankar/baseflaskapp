from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from apps.middleware import before_my_blueprint


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


@app.route('/', strict_slashes=False)
def root():
    return redirect(url_for('webapp.dashboard'))


from apps.onboard import onboard_app
from apps.api import api_app
from apps.web import web_app

app.before_request_funcs = {
    'apiapp': [before_my_blueprint],
	'webapp': [before_my_blueprint]
}

app.register_blueprint(onboard_app)
app.register_blueprint(api_app)
app.register_blueprint(web_app)

db.create_all()
