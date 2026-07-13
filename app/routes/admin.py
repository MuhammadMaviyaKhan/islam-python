from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_required, current_user
from functools import wraps
from app.models.user import User
from app.models.content import (
    Dua, Ziyarat, Article, Category, NamazGuide,
    Hadith, Kalma, IslamicEvent, Page, QuranVerse
)
from app.forms.admin_forms import DuaForm, ArticleForm, NamazForm, CategoryForm
from app import db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

bp = Blueprint("admin", __name__, url_prefix="/admin")


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash("Admin access required.", "error")
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return decorated


@bp.route("/")
@admin_required
def dashboard():
    stats = {
        "users": User.query.count(),
        "duas": Dua.query.count(),
        "ziyarats": Ziyarat.query.count(),
        "articles": Article.query.count(),
        "prayers": NamazGuide.query.count(),
    }
    return render_template("admin/dashboard.html", stats=stats)


@bp.route("/duas")
@admin_required
def list_duas():
    duas = Dua.query.order_by(Dua.created_at.desc()).all()
    return render_template("admin/list_duas.html", items=duas, type="dua")


@bp.route("/duas/create", methods=["GET", "POST"])
@admin_required
def create_dua():
    form = DuaForm()
    form.category_id.choices = [(0, "None")] + [
        (c.id, c.name) for c in Category.query.filter_by(content_type="dua").all()
    ]
    if form.validate_on_submit():
        dua = Dua(
            title=form.title.data, slug=form.slug.data,
            category_id=form.category_id.data or None,
            arabic=form.arabic.data, urdu=form.urdu.data,
            english=form.english.data, transliteration=form.transliteration.data,
            reference=form.reference.data, is_published=form.is_published.data,
        )
        if form.audio_file.data:
            f = form.audio_file.data
            filename = secure_filename(f.filename)
            f.save(str(current_app.config["UPLOAD_FOLDER"] / "audio" / filename))
            dua.audio_file = filename
        if form.pdf_file.data:
            f = form.pdf_file.data
            filename = secure_filename(f.filename)
            f.save(str(current_app.config["UPLOAD_FOLDER"] / "pdf" / filename))
            dua.pdf_file = filename
        db.session.add(dua)
        db.session.commit()
        flash("Dua created.", "success")
        return redirect(url_for("admin.list_duas"))
    return render_template("admin/edit_dua.html", form=form, editing=False)


@bp.route("/duas/edit/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_dua(id):
    dua = Dua.query.get_or_404(id)
    form = DuaForm(obj=dua)
    form.category_id.choices = [(0, "None")] + [
        (c.id, c.name) for c in Category.query.filter_by(content_type="dua").all()
    ]
    if form.validate_on_submit():
        dua.title = form.title.data
        dua.slug = form.slug.data
        dua.category_id = form.category_id.data or None
        dua.arabic = form.arabic.data
        dua.urdu = form.urdu.data
        dua.english = form.english.data
        dua.transliteration = form.transliteration.data
        dua.reference = form.reference.data
        dua.is_published = form.is_published.data
        db.session.commit()
        flash("Dua updated.", "success")
        return redirect(url_for("admin.list_duas"))
    return render_template("admin/edit_dua.html", form=form, editing=True, dua=dua)


@bp.route("/duas/delete/<int:id>")
@admin_required
def delete_dua(id):
    dua = Dua.query.get_or_404(id)
    db.session.delete(dua)
    db.session.commit()
    flash("Dua deleted.", "success")
    return redirect(url_for("admin.list_duas"))


@bp.route("/articles")
@admin_required
def list_articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template("admin/list_articles.html", items=articles)


@bp.route("/articles/create", methods=["GET", "POST"])
@admin_required
def create_article():
    form = ArticleForm()
    form.category_id.choices = [(0, "None")] + [
        (c.id, c.name) for c in Category.query.filter_by(content_type="article").all()
    ]
    if form.validate_on_submit():
        article = Article(
            title=form.title.data, slug=form.slug.data,
            category_id=form.category_id.data or None,
            content=form.content.data, summary=form.summary.data,
            author=form.author.data, is_published=form.is_published.data,
            is_featured=form.is_featured.data,
        )
        db.session.add(article)
        db.session.commit()
        flash("Article created.", "success")
        return redirect(url_for("admin.list_articles"))
    return render_template("admin/edit_article.html", form=form, editing=False)


@bp.route("/articles/edit/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_article(id):
    article = Article.query.get_or_404(id)
    form = ArticleForm(obj=article)
    form.category_id.choices = [(0, "None")] + [
        (c.id, c.name) for c in Category.query.filter_by(content_type="article").all()
    ]
    if form.validate_on_submit():
        article.title = form.title.data
        article.slug = form.slug.data
        article.category_id = form.category_id.data or None
        article.content = form.content.data
        article.summary = form.summary.data
        article.author = form.author.data
        article.is_published = form.is_published.data
        article.is_featured = form.is_featured.data
        db.session.commit()
        flash("Article updated.", "success")
        return redirect(url_for("admin.list_articles"))
    return render_template("admin/edit_article.html", form=form, editing=True, article=article)


@bp.route("/articles/delete/<int:id>")
@admin_required
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash("Article deleted.", "success")
    return redirect(url_for("admin.list_articles"))


@bp.route("/namaz")
@admin_required
def list_namaz():
    prayers = NamazGuide.query.order_by(NamazGuide.sort_order).all()
    return render_template("admin/list_namaz.html", items=prayers)


@bp.route("/namaz/edit/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_namaz(id):
    prayer = NamazGuide.query.get_or_404(id)
    form = NamazForm(obj=prayer)
    if form.validate_on_submit():
        form.populate_obj(prayer)
        db.session.commit()
        flash("Prayer guide updated.", "success")
        return redirect(url_for("admin.list_namaz"))
    return render_template("admin/edit_namaz.html", form=form, prayer=prayer)


@bp.route("/users")
@admin_required
def list_users():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template("admin/list_users.html", users=users)


@bp.route("/categories")
@admin_required
def list_categories():
    categories = Category.query.order_by(Category.content_type, Category.sort_order).all()
    return render_template("admin/list_categories.html", categories=categories)


@bp.route("/categories/create", methods=["GET", "POST"])
@admin_required
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = Category(
            name=form.name.data, slug=form.slug.data,
            content_type=form.content_type.data,
            description=form.description.data,
            sort_order=form.sort_order.data,
        )
        db.session.add(cat)
        db.session.commit()
        flash("Category created.", "success")
        return redirect(url_for("admin.list_categories"))
    return render_template("admin/edit_category.html", form=form)


@bp.route("/categories/delete/<int:id>")
@admin_required
def delete_category(id):
    cat = Category.query.get_or_404(id)
    db.session.delete(cat)
    db.session.commit()
    flash("Category deleted.", "success")
    return redirect(url_for("admin.list_categories"))


@bp.route("/pages")
@admin_required
def list_pages():
    pages = Page.query.order_by(Page.title).all()
    return render_template("admin/list_pages.html", pages=pages)


@bp.route("/hadith")
@admin_required
def list_hadith():
    hadiths = Hadith.query.order_by(Hadith.created_at.desc()).all()
    return render_template("admin/list_hadith.html", hadiths=hadiths)


@bp.route("/backup")
@admin_required
def backup():
    import shutil
    from config import Config
    backup_path = Config.BASE_DIR / "database" / f"backup_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.db"
    shutil.copy2(Config.BASE_DIR / "database" / "shia.db", backup_path)
    flash(f"Database backed up to {backup_path.name}", "success")
    return redirect(url_for("admin.dashboard"))
