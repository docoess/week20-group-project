from wtforms import StringField, FileField, IntegerField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

ALLOWED_EXTENSIONS = {"mp3", "ogg", "wav"}

class SongForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired()])
  album_id = IntegerField("Album Id", validators=[DataRequired()])
  song_file = FileField("Song File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
