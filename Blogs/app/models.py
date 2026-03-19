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


class DailyUpdate(db.Model):
    """Daily updates/thoughts/announcements"""
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    work_type = db.Column(db.String(100))  # Type of work (coding, design, meeting, etc.)
    duration_hours = db.Column(db.Float, default=0)  # Hours spent
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<DailyUpdate {self.id}: {self.message[:30]}>'

    def time_ago(self):
        """Return human-readable time ago"""
        now = datetime.utcnow()
        diff = now - self.created_at

        seconds = diff.total_seconds()
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24

        if seconds < 60:
            return "just now"
        elif minutes < 60:
            return f"{int(minutes)} minute{'s' if minutes >= 2 else ''} ago"
        elif hours < 24:
            return f"{int(hours)} hour{'s' if hours >= 2 else ''} ago"
        elif days < 7:
            return f"{int(days)} day{'s' if days >= 2 else ''} ago"
        else:
            return self.created_at.strftime('%b %d, %Y')


class NotificationSettings(db.Model):
    """Notification settings for SMS/WhatsApp alerts"""
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    enabled = db.Column(db.Boolean, default=True)
    notify_on_new_work = db.Column(db.Boolean, default=True)
    notify_on_completion = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<NotificationSettings {self.phone_number}>'


class DailyPlanner(db.Model):
    """Daily planner with time slots and priorities"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)  # One planner per day
    goals = db.Column(db.Text)  # Today's goals
    notes = db.Column(db.Text)  # Daily notes
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    time_slots = db.relationship('TimeSlot', backref='planner', lazy=True, cascade='all, delete-orphan')
    priorities = db.relationship('Priority', backref='planner', lazy=True, cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', backref='planner', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<DailyPlanner {self.date}>'


class TimeSlot(db.Model):
    """Time slot for daily schedule"""
    id = db.Column(db.Integer, primary_key=True)
    planner_id = db.Column(db.Integer, db.ForeignKey('daily_planner.id'), nullable=False)
    time_range = db.Column(db.String(20), nullable=False)  # e.g., "06:00-07:00"
    task = db.Column(db.String(200))
    work_type = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TimeSlot {self.time_range}: {self.task}>'


class Priority(db.Model):
    """Top priority task"""
    id = db.Column(db.Integer, primary_key=True)
    planner_id = db.Column(db.Integer, db.ForeignKey('daily_planner.id'), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Priority {self.task}>'


class Appointment(db.Model):
    """Appointment/meeting"""
    id = db.Column(db.Integer, primary_key=True)
    planner_id = db.Column(db.Integer, db.ForeignKey('daily_planner.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(20))  # e.g., "2:00 PM"
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Appointment {self.title} at {self.time}>'
