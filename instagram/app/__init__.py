from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from app.main import main as main_buleprint
    app.register_blueprint(main_buleprint)

    import app.exceptions as app_exception
    app.register_error_handler(404, app_exception.page_not_found)
    app.register_error_handler(500, app_exception.server_error)

    return app
