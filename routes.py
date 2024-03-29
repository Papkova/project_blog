from . import app
from .models.database import session
from .models.user import User
from flask import request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user


@app.route("/main")
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]

        user = session.query(User).where(User.username == username).first()

        if user:
            flash("Цей користувач вже існує!")
            return redirect("login")

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        try:
            session.add(new_user)
            session.commit()
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
        finally:
            session.close()
            return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        remember = True if request.form["remember"] else False

        user = session.query(User).where(User.username == username).first()
        if not user or not check_password_hash(user.password, password):
            flash("Будь ласка, перевірте свій логін та пароль і спробуйте знову!")
            return redirect("/login")
        login_user(user=user, remember=remember)
        return redirect(url_for("main"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("main")