from flask import Blueprint, render_template, request, jsonify
from app.models.content import (
    Dua, Ziyarat, Article, QuranVerse, Hadith, Kalma,
    IslamicEvent, NamazGuide, Page
)
from app import db
from datetime import datetime

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    featured_duas = Dua.query.filter_by(is_published=True).order_by(db.func.random()).limit(4).all()
    featured_ziyarats = Ziyarat.query.filter_by(is_published=True).order_by(db.func.random()).limit(3).all()
    featured_articles = Article.query.filter_by(is_published=True, is_featured=True).limit(3).all()
    kalmas = Kalma.query.filter_by(is_published=True).all()
    return render_template("main/index.html",
                           featured_duas=featured_duas,
                           featured_ziyarats=featured_ziyarats,
                           featured_articles=featured_articles,
                           kalmas=kalmas)


@bp.route("/search")
def search():
    q = request.args.get("q", "").strip()
    if not q or len(q) < 2:
        return render_template("main/search.html", query=q, results=None)

    duas = Dua.query.filter(
        Dua.is_published == True,
        db.or_(Dua.title.ilike(f"%{q}%"), Dua.arabic.ilike(f"%{q}%"),
               Dua.urdu.ilike(f"%{q}%"), Dua.english.ilike(f"%{q}%"))
    ).limit(10).all()

    ziyarats = Ziyarat.query.filter(
        Ziyarat.is_published == True,
        db.or_(Ziyarat.title.ilike(f"%{q}%"), Ziyarat.arabic.ilike(f"%{q}%"),
               Ziyarat.urdu.ilike(f"%{q}%"), Ziyarat.english.ilike(f"%{q}%"))
    ).limit(10).all()

    articles = Article.query.filter(
        Article.is_published == True,
        db.or_(Article.title.ilike(f"%{q}%"), Article.content.ilike(f"%{q}%"),
               Article.summary.ilike(f"%{q}%"))
    ).limit(10).all()

    kalmas = Kalma.query.filter(
        Kalma.is_published == True,
        db.or_(Kalma.title.ilike(f"%{q}%"), Kalma.arabic.ilike(f"%{q}%"),
               Kalma.urdu.ilike(f"%{q}%"), Kalma.english.ilike(f"%{q}%"))
    ).all()

    return render_template("main/search.html", query=q,
                           duas=duas, ziyarats=ziyarats,
                           articles=articles, kalmas=kalmas)


@bp.route("/about")
def about():
    return render_template("main/about.html")


@bp.route("/contact")
def contact():
    return render_template("main/contact.html")


@bp.route("/toggle-dark-mode")
def toggle_dark_mode():
    from flask import session
    session["dark_mode"] = not session.get("dark_mode", False)
    return jsonify({"dark_mode": session["dark_mode"]})


@bp.route("/sitemap.xml")
def sitemap():
    pages = [
        {"loc": "/", "priority": "1.0"},
        {"loc": "/namaz", "priority": "0.9"},
        {"loc": "/namaz/wudu", "priority": "0.8"},
        {"loc": "/namaz/ghusl", "priority": "0.8"},
        {"loc": "/namaz/tayammum", "priority": "0.8"},
        {"loc": "/duas", "priority": "0.9"},
        {"loc": "/ziyarat", "priority": "0.9"},
        {"loc": "/kalma", "priority": "0.8"},
        {"loc": "/nade-ali", "priority": "0.8"},
        {"loc": "/tasbeeh", "priority": "0.7"},
        {"loc": "/prayer-times", "priority": "0.7"},
        {"loc": "/islamic-calendar", "priority": "0.7"},
        {"loc": "/qibla", "priority": "0.6"},
        {"loc": "/articles", "priority": "0.7"},
        {"loc": "/about", "priority": "0.5"},
        {"loc": "/contact", "priority": "0.5"},
    ]

    for dua in Dua.query.filter_by(is_published=True).all():
        pages.append({"loc": f"/duas/{dua.slug}", "priority": "0.6"})
    for ziyarat in Ziyarat.query.filter_by(is_published=True).all():
        pages.append({"loc": f"/ziyarat/{ziyarat.slug}", "priority": "0.6"})
    for article in Article.query.filter_by(is_published=True).all():
        pages.append({"loc": f"/articles/{article.slug}", "priority": "0.6"})

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in pages:
        xml += f'  <url><loc>https://shiaislam.com{p["loc"]}</loc><priority>{p["priority"]}</priority></url>\n'
    xml += "</urlset>"

    return (xml, 200, {"Content-Type": "application/xml"})


@bp.route("/robots.txt")
def robots():
    text = "User-agent: *\nDisallow: /admin/\nAllow: /\nSitemap: https://shiaislam.com/sitemap.xml\n"
    return (text, 200, {"Content-Type": "text/plain"})


@bp.route("/page/<slug>")
def page(slug):
    page = Page.query.filter_by(slug=slug, is_published=True).first_or_404()
    return render_template("main/page.html", page=page)
