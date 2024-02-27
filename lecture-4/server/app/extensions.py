from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
db = SQLAlchemy()
migrate = Migrate()