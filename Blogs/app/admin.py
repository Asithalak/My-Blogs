from flask_admin.contrib.sqla import ModelView
from app.models import Post

def setup_admin(admin, db):
    """Setup Flask-Admin views"""
    admin.add_view(ModelView(Post, db.session, name='Posts'))
