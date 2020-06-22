from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
migrate = Migrate(db)
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://m@localhost:5432/flaskr'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    migrate = Migrate(app,db)
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app