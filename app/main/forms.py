from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BookForm(FlaskForm):
    title = StringField('Book Title')
    publisher= StringField('Published By:')
    category = SelectField('Select category', choices=[('ptextbook', 'Primary Text Books'), ('stextbook', 'Secondary Text Books'), ('novels', 'Novels'),('other','Other')])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Fill in the bio info', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    title = StringField('Title for you Book',validators=[Required()])
    publisher=StringField('Published By:')
    category = SelectField('Select category', choices=[('ptextbook', 'Primary Text Books'), ('stextbook', 'Secondary Text Books'), ('novels', 'Novels'),('other','Other')])
    submit = SubmitField('Update')