import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "178973483"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    # MAIL_USER_TLS = os.environ.get("MAIL_USER_TLS") is not None
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # ADMINS = ["vuquangton@outlook.com"]

    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = "587"
    MAIL_USER_TLS = 1
    MAIL_USERNAME = "vuquangton@gmail.com"
    MAIL_PASSWORD = "fc4ff69_gmail"
    ADMINS = ["vuquangton@outlook.com"]
