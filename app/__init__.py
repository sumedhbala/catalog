from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import configure_app


app = Flask(__name__, static_url_path="/static")
configure_app(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
login = LoginManager(app)
login.login_view = "login"

from app import routes, models

# if __name__ == '__main__':
#     app.run()
