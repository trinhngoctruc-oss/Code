from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from backend.app.config import config

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    
    # Register blueprints
    from backend.app.routes import articles_bp, categories_bp, comments_bp, search_bp
    app.register_blueprint(articles_bp, url_prefix='/api/articles')
    app.register_blueprint(categories_bp, url_prefix='/api/categories')
    app.register_blueprint(comments_bp, url_prefix='/api/comments')
    app.register_blueprint(search_bp, url_prefix='/api/search')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app