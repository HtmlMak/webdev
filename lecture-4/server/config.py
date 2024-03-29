import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "fdsgkdf1gj")
    PORT = os.environ.get('PORT', 5000)
    DEBUG_TB_PROFILER_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')