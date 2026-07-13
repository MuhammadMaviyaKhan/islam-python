from flask import Blueprint, render_template, request, jsonify, session
from flask_login import login_required, current_user
from app.models.user import TasbeehProgress
from app import db

bp = Blueprint("tasbeeh", __name__, url_prefix="/tasbeeh")


@bp.route("/")
def index():
    history = []
    if current_user.is_authenticated:
        history = TasbeehProgress.query.filter_by(user_id=current_user.id).order_by(
            TasbeehProgress.updated_at.desc()).limit(20).all()
    return render_template("main/tasbeeh.html", history=history)


@bp.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    name = data.get("name", "Tasbeeh")
    target = data.get("target", 33)
    count = data.get("count", 0)

    if current_user.is_authenticated:
        progress = TasbeehProgress.query.filter_by(
            user_id=current_user.id, name=name
        ).first()
        if progress:
            progress.count = count
            progress.target = target
            progress.updated_at = db.func.now()
        else:
            progress = TasbeehProgress(
                user_id=current_user.id, name=name,
                target=target, count=count
            )
            db.session.add(progress)
        db.session.commit()

    return jsonify({"success": True})
