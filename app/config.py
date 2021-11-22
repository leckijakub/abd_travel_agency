import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '40eb81e6ea0d2f23cc20863b210801ab'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True # ustawienie na 'True' przydatne do zadań wykładowych i przy pracy nad sprawozdaniem 2
