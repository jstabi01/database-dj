"""Forms for playlist app."""

from wtforms import StringField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, URL


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField("Playlist Name", validators=[InputRequired()])
    description = StringField("Playlist Description",
                              validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField("Song Title", validators=[InputRequired()])
    artist = StringField("Artist", validators=[InputRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
