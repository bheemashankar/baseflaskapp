from flask import redirect, url_for


def before_my_blueprint():
    if True:
        return redirect(url_for('onboard.welcome'))
