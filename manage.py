from app import create_app, db
from app.models import Users
from flask_migrate import Migrate
from decouple import config

app = create_app(config('MODE'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Users=Users)
