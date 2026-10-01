from decouple import config

from app import create_app

app = create_app(config("MODE"))