from app import create_app, db
from app.models import Post

app = create_app()

with app.app_context():
    # Check if there are any posts
    post_count = Post.query.count()
    print(f"Current number of posts: {post_count}")

    # Create a sample post if database is empty
    if post_count == 0:
        print("\nCreating sample blog post...")
        sample_post = Post(
            title="Welcome to My Personal Blog!",
            content="""# Welcome!

Thank you for visiting my personal blog. This is my first blog post!

## Features

This blog has several great features:

- **Markdown Support** - Write posts using Markdown syntax
- **Rich Formatting** - Use headers, lists, bold, italic, and more
- **Easy Management** - Create, edit, and delete posts easily
- **Responsive Design** - Works great on mobile and desktop
- **Admin Panel** - Manage all posts from the admin interface

## Getting Started

To create a new post, simply:

1. Click on "Create Post" in the navigation menu
2. Fill in the title and content (using Markdown)
3. Add your author name (optional)
4. Choose whether to publish immediately
5. Submit!

## Code Example

You can even include code blocks:

```python
def hello_world():
    print("Hello from my blog!")
    return "Welcome"
```

## Conclusion

I hope you enjoy reading my blog posts. Stay tuned for more updates!

*Happy reading!*
            """,
            author="Blog Admin",
            published=True
        )
        sample_post.set_slug()
        db.session.add(sample_post)
        db.session.commit()

        print(f"[OK] Sample post created successfully!")
        print(f"  Title: {sample_post.title}")
        print(f"  Slug: {sample_post.slug}")
        print(f"  Created at: {sample_post.created_at}")

        # Create a second post
        tech_post = Post(
            title="Python Flask: A Powerful Web Framework",
            content="""# Python Flask

Flask is a lightweight and powerful web framework for Python.

## Why Flask?

Flask is popular because it's:

- **Simple** - Easy to learn and use
- **Flexible** - You control the components
- **Extensible** - Rich ecosystem of extensions
- **Well-documented** - Great documentation and community

## Example Application

This blog itself is built with Flask! Here are the main components:

### Database (SQLAlchemy)
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

### Routes
```python
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
```

### Models
```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
```

## Learn More

Check out the [official Flask documentation](https://flask.palletsprojects.com/) to learn more!
            """,
            author="Tech Enthusiast",
            published=True
        )
        tech_post.set_slug()
        db.session.add(tech_post)
        db.session.commit()

        print(f"[OK] Second sample post created successfully!")
        print(f"  Title: {tech_post.title}")
        print(f"  Slug: {tech_post.slug}")

    else:
        print("\nPosts already exist in database:")
        posts = Post.query.all()
        for post in posts:
            print(f"  - {post.title} by {post.author}")

    print(f"\n[OK] Database verification complete!")
    print(f"[OK] Total posts in database: {Post.query.count()}")
