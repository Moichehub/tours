from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        from .routes import main, admin, auth
        app.register_blueprint(main)
        app.register_blueprint(admin, url_prefix='/admin')
        app.register_blueprint(auth)

        db.create_all()

    return app
