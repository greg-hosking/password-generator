from flask import Flask


def create_app():
    """
    TODO: write function documentation
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret Key'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
