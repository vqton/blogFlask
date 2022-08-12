from flask import render_template
from blog import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    return render_template("index.html", title="Home", user=user)


from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404
