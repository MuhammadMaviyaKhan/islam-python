from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    dark_mode = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    bookmarks = db.relationship("Bookmark", back_populates="user", lazy="dynamic", cascade="all, delete-orphan")
    reading_history = db.relationship("ReadingHistory", back_populates="user", lazy="dynamic", cascade="all, delete-orphan")
    tasbeeh_progress = db.relationship("TasbeehProgress", back_populates="user", lazy="dynamic", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    content_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="bookmarks")

    __table_args__ = (db.UniqueConstraint("user_id", "content_type", "content_id"),)


class ReadingHistory(db.Model):
    __tablename__ = "reading_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    content_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200))
    last_read = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="reading_history")


class TasbeehProgress(db.Model):
    __tablename__ = "tasbeeh_progress"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100))
    target = db.Column(db.Integer, default=33)
    count = db.Column(db.Integer, default=0)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="tasbeeh_progress")
