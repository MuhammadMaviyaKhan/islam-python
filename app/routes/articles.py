from flask import Blueprint, render_template, request
from app.models.content import Article, Category
from app import db

bp = Blueprint("articles", __name__, url_prefix="/articles")


@bp.route("/")
def index():
    category_slug = request.args.get("category")
    articles = Article.query.filter_by(is_published=True)
    if category_slug:
        cat = Category.query.filter_by(slug=category_slug, content_type="article").first()
        if cat:
            articles = articles.filter_by(category_id=cat.id)
    articles = articles.order_by(Article.created_at.desc()).all()
    categories = Category.query.filter_by(content_type="article").all()
    return render_template("articles/index.html", articles=articles, categories=categories)


@bp.route("/<slug>")
def detail(slug):
    article = Article.query.filter_by(slug=slug, is_published=True).first_or_404()
    article.view_count += 1
    db.session.commit()
    return render_template("articles/detail.html", article=article)
