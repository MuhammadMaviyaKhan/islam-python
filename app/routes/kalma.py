from flask import Blueprint, render_template
from app.models.content import Kalma

bp = Blueprint("kalma", __name__, url_prefix="/kalma")


@bp.route("/")
def index():
    kalmas = Kalma.query.filter_by(is_published=True).all()
    return render_template("kalma/index.html", kalmas=kalmas)
