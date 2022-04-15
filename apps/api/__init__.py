from flask import Blueprint


api_app = Blueprint('apiapp', __name__, url_prefix="/api/v1")

from apps.api import views
