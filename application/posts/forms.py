from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[('P', 'Programming'), ('S', 'Science'), ('M', 'Machine Learning'), ('O', 'Other Tech')], default='O')
    submit = SubmitField('Post')
