# Personal Blog Website

A simple and elegant personal blog built with Python Flask, featuring Markdown support, admin panel, and responsive design.

## Features

- 📝 Create, edit, and delete blog posts
- 📖 Markdown support for rich text formatting
- 🎨 Clean and responsive design with Bootstrap 5
- 🔧 Admin panel for easy content management
- 🔍 SEO-friendly URLs with automatic slug generation
- 📱 Mobile-friendly responsive layout
- 🔒 CSRF protection on all forms
- 💾 SQLite database (no server required)

## Technology Stack

- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Migrate** - Database migrations
- **Flask-WTF** - Forms with CSRF protection
- **Flask-Admin** - Admin interface
- **Markdown** - Rich text formatting
- **Bootstrap 5** - Responsive CSS framework
- **SQLite** - File-based database

## Project Structure

```
Blogs/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── models.py                # Database models (Post)
│   ├── routes.py                # URL routes and views
│   ├── forms.py                 # WTForms
│   ├── admin.py                 # Flask-Admin setup
│   ├── templates/               # Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── post.html
│   │   ├── create_post.html
│   │   └── edit_post.html
│   └── static/
│       └── css/
│           └── style.css        # Custom styles
├── instance/
│   └── blog.db                  # SQLite database
├── config.py                    # Configuration
├── run.py                       # Application entry point
├── requirements.txt             # Dependencies
├── .env                         # Environment variables
└── README.md                    # This file
```

## Installation

### 1. Navigate to the project directory

```bash
cd d:/My-Blogs/Blogs
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**On Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Initialize the database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Running the Application

### Start the development server

```bash
python run.py
```

The blog will be available at: **http://localhost:5000/**

### Access Points

- **Homepage**: http://localhost:5000/
- **Create Post**: http://localhost:5000/create
- **Admin Panel**: http://localhost:5000/admin

## Usage Guide

### Creating a Blog Post

1. Navigate to http://localhost:5000/create or click "Create Post" in the navigation
2. Fill in the form:
   - **Title**: Your post title (required)
   - **Content**: Your post content with Markdown (required)
   - **Author**: Your name (optional, defaults to "Anonymous")
   - **Published**: Check to publish immediately
3. Click "Submit"

### Markdown Syntax Guide

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point 1
- Bullet point 2

1. Numbered item 1
2. Numbered item 2

[Link text](https://example.com)

`inline code`

\`\`\`
code block
\`\`\`
```

### Editing a Post

1. Open any blog post
2. Click the "Edit Post" button
3. Modify the content
4. Click "Update Post"

### Deleting a Post

1. Open any blog post
2. Click the "Delete Post" button
3. Confirm the deletion

### Using the Admin Panel

1. Navigate to http://localhost:5000/admin
2. Click on "Posts" to see all posts in a table view
3. You can create, edit, search, and delete posts from here

## Database Management

### Create a new migration (after model changes)

```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

### Reset the database

```bash
# Delete the database file
rm instance/blog.db

# Re-initialize
flask db upgrade
```

## Configuration

The application can be configured via environment variables in the `.env` file:

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///path/to/database.db  # Optional
```

## Deployment

For production deployment, you should:

1. Set a strong `SECRET_KEY` in `.env`
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
   ```
3. Use a production database like PostgreSQL
4. Set `DEBUG=False` in config
5. Use a reverse proxy like Nginx

## Troubleshooting

### Port already in use

If port 5000 is already in use, modify `run.py` and change the port:

```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Database errors

If you encounter database errors, try:

```bash
rm instance/blog.db
flask db upgrade
```

### Module not found errors

Make sure your virtual environment is activated and dependencies are installed:

```bash
source venv/Scripts/activate
pip install -r requirements.txt
```

## Future Enhancements

Possible features to add:

- User authentication for admin access
- Categories and tags for posts
- Comments system
- Search functionality
- Image upload support
- Draft posts (unpublished)
- RSS feed
- Social media sharing buttons
- SEO meta tags

## License

This project is open source and available for personal use.

## Support

For issues or questions, please check the troubleshooting section above.

---

**Built with Flask and Python** 🐍
