from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired
class AddItem(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired()])
    publ = StringField('Publisher', validators=[DataRequired()])
    genre = DateField('Genre', validators=[DataRequired()])
    hours = SelectField('Hours Played', validators=[DataRequired()])
    submit = SubmitField('Add Item')

class EditItem(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired()])
    publ = StringField('Publisher', validators=[DataRequired()])
    genre = DateField('Genre', format='%Y-%m-%d', validators=[DataRequired()])
    hours = SelectField('Hours Played', choices=[('todo', 'To-Do'), ('done', 'Done')], validators=[DataRequired()])
    submit = SubmitField('Update Item')