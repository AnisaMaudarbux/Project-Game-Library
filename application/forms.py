from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
class AddItem(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired()])
    publ = StringField('Publisher', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    hours = IntegerField('Hours Played', validators=[DataRequired()])
    submit = SubmitField('Add Item')

class EditItem(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired()])
    publ = StringField('Publisher', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    hours = IntegerField('Hours Played', validators=[DataRequired()])
    submit = SubmitField('Update Item')