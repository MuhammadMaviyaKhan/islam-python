from flask import Blueprint, render_template
from app.models.content import QuranVerse
from app import db

bp = Blueprint("quran", __name__, url_prefix="/quran")


@bp.route("/")
def index():
    surahs = db.session.query(QuranVerse.surah, db.func.count(QuranVerse.id)).group_by(QuranVerse.surah).all()
    surah_list = []
    for s in surahs:
        first = QuranVerse.query.filter_by(surah=s[0]).first()
        if first:
            surah_list.append({"number": s[0], "verses": s[1]})
    return render_template("quran/index.html", surahs=surah_list)


@bp.route("/<int:surah>")
def surah(surah):
    verses = QuranVerse.query.filter_by(surah=surah).order_by(QuranVerse.verse).all()
    return render_template("quran/surah.html", verses=verses, surah_num=surah)
