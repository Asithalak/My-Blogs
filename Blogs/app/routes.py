from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime, date
from app import db
from app.models import Post, DailyUpdate, NotificationSettings, DailyPlanner, TimeSlot, Priority, Appointment
from app.forms import PostForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Homepage showing all published posts and today's schedule"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True)\
        .order_by(Post.created_at.desc())\
        .paginate(page=page, per_page=5, error_out=False)

    # Get today's planner
    today = date.today()
    planner = DailyPlanner.query.filter_by(date=today).first()

    return render_template('index.html', posts=posts, planner=planner, today=today)

@bp.route('/post/<slug>')
def post(slug):
    """Display single post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('post.html', post=post)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    """Create new post"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=form.author.data or 'Anonymous',
            published=form.published.data
        )
        post.set_slug()
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.post', slug=post.slug))
    return render_template('create_post.html', form=form)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit existing post"""
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        old_title = post.title
        post.title = form.title.data
        post.content = form.content.data
        post.author = form.author.data or 'Anonymous'
        post.published = form.published.data

        # Update slug if title changed
        if old_title != post.title:
            post.set_slug()

        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('main.post', slug=post.slug))

    return render_template('edit_post.html', form=form, post=post)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    """Delete post"""
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/upload-profile', methods=['POST'])
def upload_profile():
    """Upload profile picture"""
    if 'profile_image' not in request.files:
        flash('No file selected!', 'danger')
        return redirect(request.referrer or url_for('main.index'))

    file = request.files['profile_image']

    if file.filename == '':
        flash('No file selected!', 'danger')
        return redirect(request.referrer or url_for('main.index'))

    # Check file extension
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    filename = secure_filename(file.filename)
    file_ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''

    if file_ext not in allowed_extensions:
        flash('Invalid file type! Please upload PNG, JPG, JPEG, or GIF.', 'danger')
        return redirect(request.referrer or url_for('main.index'))

    # Save as profile.{ext}
    upload_folder = os.path.join('app', 'static', 'images')
    os.makedirs(upload_folder, exist_ok=True)

    # Remove old profile images
    for ext in allowed_extensions:
        old_file = os.path.join(upload_folder, f'profile.{ext}')
        if os.path.exists(old_file):
            os.remove(old_file)

    # Save new profile image
    filepath = os.path.join(upload_folder, f'profile.{file_ext}')
    file.save(filepath)

    flash('Profile picture updated successfully!', 'success')
    return redirect(request.referrer or url_for('main.index'))


@bp.route('/daily-update/add', methods=['POST'])
def add_daily_update():
    """Add a new daily update"""
    message = request.form.get('message', '').strip()
    work_type = request.form.get('work_type', '').strip()
    duration = request.form.get('duration', '0')

    if not message:
        flash('Please enter a message!', 'danger')
        return redirect(request.referrer or url_for('main.index'))

    if len(message) > 500:
        flash('Message too long! Maximum 500 characters.', 'danger')
        return redirect(request.referrer or url_for('main.index'))

    try:
        duration_hours = float(duration) if duration else 0
    except ValueError:
        duration_hours = 0

    update = DailyUpdate(
        message=message,
        work_type=work_type or 'General',
        duration_hours=duration_hours
    )
    db.session.add(update)
    db.session.commit()

    # Send notification
    send_notification(update)

    flash('Daily update added successfully!', 'success')
    return redirect(request.referrer or url_for('main.index'))


def send_notification(update):
    """Send SMS notification about new work update"""
    try:
        settings = NotificationSettings.query.filter_by(enabled=True).first()
        if not settings or not settings.notify_on_new_work:
            return

        # Format message
        msg = f"📢 New Work Update!\n"
        msg += f"Task: {update.message[:100]}\n"
        if update.work_type:
            msg += f"Type: {update.work_type}\n"
        if update.duration_hours > 0:
            msg += f"Duration: {update.duration_hours}h\n"
        msg += f"Time: {update.time_ago()}"

        # For now, just log the notification
        # To enable SMS, integrate with Twilio or similar service
        print(f"\n{'='*50}")
        print(f"📱 SMS NOTIFICATION TO: {settings.phone_number}")
        print(f"{'='*50}")
        print(msg)
        print(f"{'='*50}\n")

        # TODO: Integrate Twilio for actual SMS
        # from twilio.rest import Client
        # client = Client(account_sid, auth_token)
        # client.messages.create(
        #     body=msg,
        #     from_=twilio_number,
        #     to=settings.phone_number
        # )

    except Exception as e:
        print(f"Notification error: {e}")



@bp.route('/daily-update/get')
def get_daily_updates():
    """Get active daily updates (API endpoint)"""
    updates = DailyUpdate.query.filter_by(active=True)\
        .order_by(DailyUpdate.created_at.desc())\
        .limit(10)\
        .all()

    return jsonify([
        {
            'id': u.id,
            'message': u.message,
            'work_type': u.work_type,
            'duration_hours': u.duration_hours,
            'created_at': u.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'time_ago': u.time_ago()
        } for u in updates
    ])


@bp.route('/daily-update/delete/<int:id>', methods=['POST'])
def delete_daily_update(id):
    """Delete a daily update"""
    update = DailyUpdate.query.get_or_404(id)
    db.session.delete(update)
    db.session.commit()

    flash('Daily update deleted!', 'success')
    return redirect(request.referrer or url_for('main.index'))


@bp.route('/notification-settings', methods=['GET', 'POST'])
def notification_settings():
    """Manage notification settings"""
    settings = NotificationSettings.query.first()

    if request.method == 'POST':
        phone = request.form.get('phone_number', '').strip()
        enabled = request.form.get('enabled') == 'on'
        notify_new = request.form.get('notify_on_new_work') == 'on'
        notify_complete = request.form.get('notify_on_completion') == 'on'

        if not phone:
            flash('Please enter a phone number!', 'danger')
            return redirect(url_for('main.notification_settings'))

        if settings:
            settings.phone_number = phone
            settings.enabled = enabled
            settings.notify_on_new_work = notify_new
            settings.notify_on_completion = notify_complete
        else:
            settings = NotificationSettings(
                phone_number=phone,
                enabled=enabled,
                notify_on_new_work=notify_new,
                notify_on_completion=notify_complete
            )
            db.session.add(settings)

        db.session.commit()
        flash('Notification settings updated!', 'success')
        return redirect(url_for('main.notification_settings'))

    return render_template('notification_settings.html', settings=settings)


@bp.route('/work-stats')
def work_stats():
    """Get work statistics (API endpoint)"""
    from datetime import timedelta
    from sqlalchemy import func

    # Get stats for today
    today = datetime.utcnow().date()
    today_start = datetime.combine(today, datetime.min.time())

    today_updates = DailyUpdate.query.filter(
        DailyUpdate.created_at >= today_start
    ).all()

    total_hours_today = sum(u.duration_hours for u in today_updates)

    # Get stats by work type
    work_by_type = db.session.query(
        DailyUpdate.work_type,
        func.sum(DailyUpdate.duration_hours).label('total_hours'),
        func.count(DailyUpdate.id).label('count')
    ).filter(
        DailyUpdate.created_at >= today_start
    ).group_by(DailyUpdate.work_type).all()

    return jsonify({
        'today': {
            'total_hours': total_hours_today,
            'task_count': len(today_updates),
            'by_type': [
                {
                    'type': wt[0] or 'General',
                    'hours': float(wt[1] or 0),
                    'count': wt[2]
                } for wt in work_by_type
            ]
        }
    })


# ============= Daily Planner Routes =============

@bp.route('/planner/save', methods=['POST'])
def save_planner():
    """Save daily planner data"""
    try:
        data = request.get_json()
        planner_date = datetime.strptime(data.get('date'), '%Y-%m-%d').date()

        # Get or create planner for this date
        planner = DailyPlanner.query.filter_by(date=planner_date).first()
        if not planner:
            planner = DailyPlanner(date=planner_date)
            db.session.add(planner)

        # Update goals and notes
        planner.goals = data.get('goals', '')
        planner.notes = data.get('notes', '')

        # Clear existing items
        TimeSlot.query.filter_by(planner_id=planner.id).delete()
        Priority.query.filter_by(planner_id=planner.id).delete()
        Appointment.query.filter_by(planner_id=planner.id).delete()

        # Add time slots
        for slot_data in data.get('time_slots', []):
            if slot_data.get('task'):
                slot = TimeSlot(
                    planner=planner,
                    time_range=slot_data['time_range'],
                    task=slot_data['task'],
                    work_type=slot_data.get('work_type', 'General'),
                    completed=slot_data.get('completed', False)
                )
                db.session.add(slot)

        # Add priorities
        for idx, priority_data in enumerate(data.get('priorities', [])):
            if priority_data.get('task'):
                priority = Priority(
                    planner=planner,
                    task=priority_data['task'],
                    completed=priority_data.get('completed', False),
                    order=idx
                )
                db.session.add(priority)

        # Add appointments
        for appt_data in data.get('appointments', []):
            if appt_data.get('title'):
                appt = Appointment(
                    planner=planner,
                    title=appt_data['title'],
                    time=appt_data.get('time', ''),
                    completed=appt_data.get('completed', False)
                )
                db.session.add(appt)

        db.session.commit()
        return jsonify({'success': True, 'message': 'Planner saved successfully!'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400


@bp.route('/planner/get/<date_str>')
def get_planner(date_str):
    """Get planner data for a specific date"""
    try:
        planner_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        planner = DailyPlanner.query.filter_by(date=planner_date).first()

        if not planner:
            return jsonify({
                'exists': False,
                'date': date_str,
                'time_slots': [],
                'priorities': [],
                'appointments': [],
                'goals': '',
                'notes': ''
            })

        return jsonify({
            'exists': True,
            'date': date_str,
            'time_slots': [
                {
                    'time_range': slot.time_range,
                    'task': slot.task,
                    'work_type': slot.work_type,
                    'completed': slot.completed
                } for slot in planner.time_slots
            ],
            'priorities': [
                {
                    'task': p.task,
                    'completed': p.completed
                } for p in sorted(planner.priorities, key=lambda x: x.order)
            ],
            'appointments': [
                {
                    'title': a.title,
                    'time': a.time,
                    'completed': a.completed
                } for a in planner.appointments
            ],
            'goals': planner.goals or '',
            'notes': planner.notes or ''
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


