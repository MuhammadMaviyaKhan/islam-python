from flask import session
from datetime import datetime
from app import db
from app.models.content import QuranVerse, Hadith, Category


def inject_globals():
    daily_verse = QuranVerse.query.order_by(db.func.random()).first()
    daily_hadith = Hadith.query.filter_by(is_featured=True).order_by(db.func.random()).first()
    if not daily_hadith:
        daily_hadith = Hadith.query.order_by(db.func.random()).first()
    categories = Category.query.order_by(Category.sort_order).all()
    return {
        "now": datetime.utcnow(),
        "daily_verse": daily_verse,
        "daily_hadith": daily_hadith,
        "categories": categories,
        "dark_mode": session.get("dark_mode", False),
    }
