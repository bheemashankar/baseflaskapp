from flask import jsonify, render_template, redirect, url_for
from apps import app


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


@app.route('/', strict_slashes=False)
def root():
    return redirect(url_for('webapp.dashboard'))


@app.route('/api/v1/', strict_slashes=False)
def index():
    data = {}
    return jsonify(data)
