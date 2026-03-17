from datetime import datetime
from app import db
import re

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), default='Anonymous')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Post {self.title}>'

    @staticmethod
    def generate_slug(title):
        """Generate URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')

    def set_slug(self):
        """Set slug from title, ensuring uniqueness"""
        base_slug = self.generate_slug(self.title)
        slug = base_slug
        counter = 1
        while Post.query.filter_by(slug=slug).first() is not None:
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
