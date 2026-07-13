from flask import Blueprint, render_template, request, jsonify
from app.models.content import Dua, Category
from app import db

bp = Blueprint("duas", __name__, url_prefix="/duas")


@bp.route("/")
def index():
    category_slug = request.args.get("category")
    query = request.args.get("q", "").strip()

    duas_query = Dua.query.filter_by(is_published=True)
    if category_slug:
        cat = Category.query.filter_by(slug=category_slug, content_type="dua").first()
        if cat:
            duas_query = duas_query.filter_by(category_id=cat.id)
    if query:
        duas_query = duas_query.filter(
            db.or_(Dua.title.ilike(f"%{query}%"), Dua.arabic.ilike(f"%{query}%"),
                   Dua.urdu.ilike(f"%{query}%"), Dua.english.ilike(f"%{query}%"))
        )

    duas = duas_query.order_by(Dua.title).all()
    categories = Category.query.filter_by(content_type="dua").order_by(Category.sort_order).all()

    return render_template("duas/index.html", duas=duas, categories=categories,
                           current_category=category_slug, query=query)


@bp.route("/<slug>")
def detail(slug):
    dua = Dua.query.filter_by(slug=slug, is_published=True).first_or_404()
    dua.view_count += 1
    db.session.commit()

    related = Dua.query.filter(
        Dua.id != dua.id, Dua.is_published == True,
        Dua.category_id == dua.category_id
    ).limit(4).all()

    return render_template("duas/detail.html", dua=dua, related=related)


@bp.route("/api/search")
def api_search():
    q = request.args.get("q", "").strip()
    if len(q) < 2:
        return jsonify([])
    duas = Dua.query.filter(
        Dua.is_published == True,
        db.or_(Dua.title.ilike(f"%{q}%"), Dua.arabic.ilike(f"%{q}%"),
               Dua.urdu.ilike(f"%{q}%"), Dua.english.ilike(f"%{q}%"))
    ).limit(10).all()
    return jsonify([{"id": d.id, "title": d.title, "slug": d.slug, "type": "dua"} for d in duas])
