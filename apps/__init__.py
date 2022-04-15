from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from apps.api import api_app
from apps.web import web_app

app.register_blueprint(api_app)
app.register_blueprint(web_app)

db.create_all()
