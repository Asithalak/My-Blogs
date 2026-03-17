from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message='Title is required'),
        Length(max=200, message='Title must be less than 200 characters')
    ])
    content = TextAreaField('Content', validators=[
        DataRequired(message='Content is required')
    ], render_kw={"rows": 15})
    author = StringField('Author', validators=[
        Length(max=100, message='Author name must be less than 100 characters')
    ])
    published = BooleanField('Published', default=True)
    submit = SubmitField('Submit')
