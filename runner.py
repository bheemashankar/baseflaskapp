# from flask import Flask
# from apiapp import api_app
# from webapp import web_app

# app = Flask(__name__)

# app.register_blueprint(api_app, url_prefix="/api/v1")
# app.register_blueprint(web_app)

# app.run(debug=True)


from apps import app

app.run(debug=True)