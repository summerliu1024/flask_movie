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
