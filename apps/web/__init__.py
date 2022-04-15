from flask import Blueprint


web_app = Blueprint('webapp', __name__, url_prefix="/web")

from apps.web import views