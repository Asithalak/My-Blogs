from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import db
from app.models import Post
from app.forms import PostForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Homepage showing all published posts"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True)\
        .order_by(Post.created_at.desc())\
        .paginate(page=page, per_page=5, error_out=False)
    return render_template('index.html', posts=posts)

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

