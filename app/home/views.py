from flask import render_template, redirect, url_for

from . import home


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/login")
def login():
    return render_template("home/login.html")


@home.route("/logout")
def logout():
    """点击退出 进入登录页面"""
    return redirect(url_for("home.login"))


@home.route("/register")
def register():
    return render_template("home/register.html")

@home.route("/user")
def user():
    return render_template("home/user.html")

@home.route("/pwd")
def pwd():
    return render_template("home/pwd.html")

@home.route("/comments")
def comments():
    return render_template("home/comments.html")

@home.route("/loginlog")
def loginlog():
    return render_template("home/loginlog.html")

@home.route("/moviecol")
def moviecol():
    return render_template("home/moviecol.html")
