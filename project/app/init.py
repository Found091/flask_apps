from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

db = SQLAlchemy()

def create_app(config_class=None):

    app = Flask(__name__)

    if config_class is None:
        config_class = os.getenv('FLASK_ENV', 'development').capitalize() + 'Config'
        try:
            app.config.from_object(f'config.{config_class}')
        except ImportError:
            app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)

    # Register blueprints
    from .views import views
    app.register_blueprint(views, url_prefix='/')


    return app
