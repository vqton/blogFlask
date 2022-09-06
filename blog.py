# from blog import app
from blog import db, app, cli
from blog.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
