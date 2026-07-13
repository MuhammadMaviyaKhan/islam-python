from flask import Blueprint, render_template, request, jsonify
from app.models.content import IslamicEvent
from datetime import datetime
import requests
import json

bp = Blueprint("prayers", __name__, url_prefix="")


@bp.route("/prayer-times")
def prayer_times():
    from config import Config
    lat = request.args.get("lat", "33.6844")
    lng = request.args.get("lng", "73.0479")
    method = request.args.get("method", "1")

    try:
        resp = requests.get(
            f"{Config.PRAYER_TIMES_API}/{int(datetime.utcnow().timestamp())}",
            params={"latitude": lat, "longitude": lng, "method": method},
            timeout=5,
        )
        timings = resp.json().get("data", {}).get("timings", {})
    except Exception:
        timings = {}

    return render_template("main/prayer_times.html", timings=timings,
                           lat=lat, lng=lng)


@bp.route("/islamic-calendar")
def islamic_calendar():
    month = request.args.get("month", datetime.utcnow().month)
    year = request.args.get("year", datetime.utcnow().year)
    events = IslamicEvent.query.order_by(IslamicEvent.hijri_date).all()
    return render_template("main/islamic_calendar.html", events=events)


@bp.route("/qibla")
def qibla():
    from config import Config
    lat = request.args.get("lat", "33.6844")
    lng = request.args.get("lng", "73.0479")
    direction = None

    try:
        resp = requests.get(Config.QIBLA_API, params={"latitude": lat, "longitude": lng}, timeout=5)
        data = resp.json()
        direction = data.get("data", {}).get("direction")
    except Exception:
        pass

    return render_template("main/qibla.html", direction=direction, lat=lat, lng=lng)


@bp.route("/api/prayer-times")
def api_prayer_times():
    from config import Config
    lat = request.args.get("lat", "33.6844")
    lng = request.args.get("lng", "73.0479")
    try:
        resp = requests.get(
            f"{Config.PRAYER_TIMES_API}/{int(datetime.utcnow().timestamp())}",
            params={"latitude": lat, "longitude": lng, "method": "1"},
            timeout=5,
        )
        return jsonify(resp.json().get("data", {}))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
