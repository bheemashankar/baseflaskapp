from flask import Blueprint


web_app = Blueprint('webapp', __name__)

from apps.web import views