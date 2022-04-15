from flask import Blueprint


onboard_app = Blueprint('onboard', __name__)

from apps.onboard import views