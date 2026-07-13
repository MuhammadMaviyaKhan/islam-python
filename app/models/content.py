from app import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False, index=True)
    content_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Dua(db.Model):
    __tablename__ = "duas"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    arabic = db.Column(db.Text, nullable=False)
    urdu = db.Column(db.Text)
    english = db.Column(db.Text)
    transliteration = db.Column(db.Text)
    reference = db.Column(db.Text)
    audio_file = db.Column(db.String(200))
    pdf_file = db.Column(db.String(200))
    is_published = db.Column(db.Boolean, default=True)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = db.relationship("Category", backref="duas", lazy=True)


class Ziyarat(db.Model):
    __tablename__ = "ziyarats"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    arabic = db.Column(db.Text, nullable=False)
    urdu = db.Column(db.Text)
    english = db.Column(db.Text)
    transliteration = db.Column(db.Text)
    reference = db.Column(db.Text)
    audio_file = db.Column(db.String(200))
    is_published = db.Column(db.Boolean, default=True)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    image = db.Column(db.String(200))
    author = db.Column(db.String(100))
    is_published = db.Column(db.Boolean, default=True)
    is_featured = db.Column(db.Boolean, default=False)
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = db.relationship("Category", backref="articles", lazy=True)


class NamazGuide(db.Model):
    __tablename__ = "namaz_guides"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False, index=True)
    prayer_type = db.Column(db.String(50), nullable=False)
    rakats = db.Column(db.String(50))
    purpose = db.Column(db.Text)
    steps = db.Column(db.Text, nullable=False)
    tasbihat = db.Column(db.Text)
    tashahhud = db.Column(db.Text)
    salam = db.Column(db.Text)
    arabic = db.Column(db.Text)
    notes = db.Column(db.Text)
    sort_order = db.Column(db.Integer, default=0)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class QuranVerse(db.Model):
    __tablename__ = "quran_verses"

    id = db.Column(db.Integer, primary_key=True)
    surah = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.Integer, nullable=False)
    arabic = db.Column(db.Text, nullable=False)
    translation = db.Column(db.Text)
    urdu_translation = db.Column(db.Text)
    reference = db.Column(db.String(100))


class Hadith(db.Model):
    __tablename__ = "hadiths"

    id = db.Column(db.Integer, primary_key=True)
    arabic = db.Column(db.Text)
    urdu = db.Column(db.Text)
    english = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(200), nullable=False)
    reference = db.Column(db.String(200))
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Kalma(db.Model):
    __tablename__ = "kalmas"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    arabic = db.Column(db.Text, nullable=False)
    urdu = db.Column(db.Text)
    english = db.Column(db.Text)
    transliteration = db.Column(db.Text)
    reference = db.Column(db.Text)
    audio_file = db.Column(db.String(200))
    is_published = db.Column(db.Boolean, default=True)


class IslamicEvent(db.Model):
    __tablename__ = "islamic_events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    hijri_date = db.Column(db.String(50), nullable=False)
    gregorian_date = db.Column(db.Date)
    event_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    is_public_holiday = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Page(db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    meta_description = db.Column(db.Text)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
