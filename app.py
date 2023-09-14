from flask import Flask
from flask_smorest import Api
from routes import blp as RoutesBlueprint
def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Dummy Api"
    app.config['SECRET_KEY'] = 'key'
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    #app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api = Api(app)
    api.register_blueprint(RoutesBlueprint)

    return app
