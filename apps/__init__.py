from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apps.middleware import before_web_blueprint, before_api_blueprint


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from apps.onboard import onboard_app
from apps.api import api_app
from apps.web import web_app

app.before_request_funcs = {
    'apiapp': [before_api_blueprint],
	'webapp': [before_web_blueprint]
}

app.register_blueprint(onboard_app)
app.register_blueprint(api_app)
app.register_blueprint(web_app)

db.create_all()

from apps import views
