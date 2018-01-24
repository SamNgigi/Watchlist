from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[
                        Required('This is required')])
    review = TextAreaField('Movie review', validators=[
                           Required('This is required')])
    submit = SubmitField('Submit')
