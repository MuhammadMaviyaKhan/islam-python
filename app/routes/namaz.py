from flask import Blueprint, render_template
from app.models.content import NamazGuide

bp = Blueprint("namaz", __name__, url_prefix="/namaz")


@bp.route("/")
def index():
    prayers = NamazGuide.query.filter_by(is_published=True).order_by(NamazGuide.sort_order).all()
    daily = [p for p in prayers if p.prayer_type in ("daily", "weekly")]
    other = [p for p in prayers if p.prayer_type not in ("daily", "weekly")]
    return render_template("namaz/index.html", daily_prayers=daily, other_prayers=other)


@bp.route("/<slug>")
def detail(slug):
    prayer = NamazGuide.query.filter_by(slug=slug, is_published=True).first_or_404()
    return render_template("namaz/detail.html", prayer=prayer)


@bp.route("/wudu")
def wudu():
    return render_template("namaz/wudu.html")


@bp.route("/ghusl")
def ghusl():
    return render_template("namaz/ghusl.html")


@bp.route("/tayammum")
def tayammum():
    return render_template("namaz/tayammum.html")
