from flask import Flask, session, redirect, url_for
import os


app = Flask(__name__)


app.secret_key = os.getenv("SECRET_KEY", "is_a_very_secret_key")


@app.route("/login")
def login():
    # check in BD
    session["username"] = "admin"
    print("user saved in session")
    return redirect(url_for("index"))


@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return f'Ви ввійшли як {username}. <br><a href="/logout">Вийти</a>'
    return 'Ви не увійшли в систему. <br><a href="/login">Увійти</a>'


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5050)
