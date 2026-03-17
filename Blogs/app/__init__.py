from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from config import Config
import markdown

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Blog Admin', template_mode='bootstrap4')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    # Custom Jinja2 filter for Markdown rendering
    @app.template_filter('markdown')
    def render_markdown(text):
        return markdown.markdown(text, extensions=['fenced_code', 'tables'])

    # Import models and admin views
    from app import models
    from app.admin_views import setup_admin
    setup_admin(admin, db)

    # Register routes
    from app import routes
    app.register_blueprint(routes.bp)

    return app
