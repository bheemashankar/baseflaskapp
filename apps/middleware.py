from flask import redirect, url_for


def is_onboard_done():
    if True:
        return True
    return False


def before_web_blueprint():
    if is_onboard_done():
        return redirect(url_for('onboard.welcome'))

def before_api_blueprint():
    if is_onboard_done():
        return redirect(url_for('index'))
