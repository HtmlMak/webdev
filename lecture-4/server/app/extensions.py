from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
api = Api()