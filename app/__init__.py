from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import config_map

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_map.get(config_name, config_map["default"]))

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes import main, auth, admin, duas, ziyarat, namaz, kalma, quran, articles, tasbeeh, prayers

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(duas.bp)
    app.register_blueprint(ziyarat.bp)
    app.register_blueprint(namaz.bp)
    app.register_blueprint(kalma.bp)
    app.register_blueprint(quran.bp)
    app.register_blueprint(articles.bp)
    app.register_blueprint(tasbeeh.bp)
    app.register_blueprint(prayers.bp)

    with app.app_context():
        from app.utils.context_processors import inject_globals
        app.context_processor(inject_globals)

        db.create_all()
        from app.utils.seed import seed_data
        seed_data()

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/500.html"), 500

    return app
