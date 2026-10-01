from decouple import config


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = config('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email config_options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'thePitcher'
    SENDER_EMAIL = config("MAIL_USERNAME")


class ProdConfig(Config):
    """
    production configuration child class
    """

    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')

    pass


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
