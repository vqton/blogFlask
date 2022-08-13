from flask import render_template, request, url_for, redirect, flash
from blog import app
from blog.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    return render_template(
        "index.html",
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    # form = LoginForm()
    form = LoginForm(request.form)
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404
