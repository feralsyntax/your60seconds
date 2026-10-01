from decouple import config

database_url = config("DATABASE_URL")

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1,
    )


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = config("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email config_options
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
    SUBJECT_PREFIX = "thePitcher"
    SENDER_EMAIL = config("MAIL_USERNAME")


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True


class ProdConfig(Config):
    """
    production configuration child class
    """

    DEBUG = False


config_options = {"development": DevConfig, "production": ProdConfig}
