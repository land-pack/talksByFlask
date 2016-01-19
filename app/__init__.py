from flask import Flask
from config import config
# pip install flask-bootstrap
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    from .talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)

    return app
