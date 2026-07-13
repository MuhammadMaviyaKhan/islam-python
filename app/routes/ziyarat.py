from flask import Blueprint, render_template, request
from app.models.content import Ziyarat
from app import db

bp = Blueprint("ziyarat", __name__, url_prefix="/ziyarat")


@bp.route("/")
def index():
    query = request.args.get("q", "").strip()
    ziyarats = Ziyarat.query.filter_by(is_published=True)
    if query:
        ziyarats = ziyarats.filter(
            db.or_(Ziyarat.title.ilike(f"%{query}%"), Ziyarat.arabic.ilike(f"%{query}%"),
                   Ziyarat.urdu.ilike(f"%{query}%"), Ziyarat.english.ilike(f"%{query}%"))
        )
    ziyarats = ziyarats.order_by(Ziyarat.title).all()
    return render_template("ziyarat/index.html", ziyarats=ziyarats, query=query)


@bp.route("/<slug>")
def detail(slug):
    ziyarat = Ziyarat.query.filter_by(slug=slug, is_published=True).first_or_404()
    ziyarat.view_count += 1
    db.session.commit()
    return render_template("ziyarat/detail.html", ziyarat=ziyarat)
