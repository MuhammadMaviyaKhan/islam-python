from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class DuaForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 200)])
    slug = StringField("Slug", validators=[DataRequired(), Length(2, 200)])
    category_id = SelectField("Category", coerce=int)
    arabic = TextAreaField("Arabic", validators=[DataRequired()])
    urdu = TextAreaField("Urdu")
    english = TextAreaField("English")
    transliteration = TextAreaField("Transliteration")
    reference = TextAreaField("Reference")
    audio_file = FileField("Audio File", validators=[FileAllowed(["mp3", "wav", "ogg"])])
    pdf_file = FileField("PDF File", validators=[FileAllowed(["pdf"])])
    is_published = BooleanField("Published", default=True)
    submit = SubmitField("Save")


class ArticleForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 200)])
    slug = StringField("Slug", validators=[DataRequired(), Length(2, 200)])
    category_id = SelectField("Category", coerce=int)
    content = TextAreaField("Content", validators=[DataRequired()])
    summary = TextAreaField("Summary")
    image = FileField("Image", validators=[FileAllowed(["jpg", "jpeg", "png", "webp"])])
    author = StringField("Author")
    is_published = BooleanField("Published", default=True)
    is_featured = BooleanField("Featured", default=False)
    submit = SubmitField("Save")


class NamazForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 100)])
    slug = StringField("Slug", validators=[DataRequired(), Length(2, 100)])
    prayer_type = StringField("Prayer Type", validators=[DataRequired()])
    rakats = StringField("Rakats")
    purpose = TextAreaField("Purpose")
    steps = TextAreaField("Steps", validators=[DataRequired()])
    tasbihat = TextAreaField("Tasbihat")
    tashahhud = TextAreaField("Tashahhud")
    salam = TextAreaField("Salam")
    arabic = TextAreaField("Arabic")
    notes = TextAreaField("Notes")
    sort_order = IntegerField("Sort Order", default=0)
    is_published = BooleanField("Published", default=True)
    submit = SubmitField("Save")


class CategoryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 100)])
    slug = StringField("Slug", validators=[DataRequired(), Length(2, 100)])
    content_type = SelectField("Content Type", choices=[
        ("dua", "Dua"), ("article", "Article"), ("ziyarat", "Ziyarat")
    ])
    description = TextAreaField("Description")
    sort_order = IntegerField("Sort Order", default=0)
    submit = SubmitField("Save")
