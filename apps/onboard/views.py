from flask import Flask, render_template
from apps.onboard import onboard_app


@onboard_app.route('/welcome', methods=["GET"], strict_slashes=False)
def welcome():
    return render_template('onboard/welcome.html')


@onboard_app.route('/onboard', methods=["GET", "POST"], strict_slashes=False)
def onboard():
    return render_template('onboard/register.html')