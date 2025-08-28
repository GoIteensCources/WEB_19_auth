from flask import Flask,  render_template

from settings import DatabaseConfig, Session
from flask_login import LoginManager
from models.users import User
from routes import users

app = Flask(__name__)
app.config.from_object(DatabaseConfig)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.get(user_id)
    print(user)
    return user


@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(users.bp, url_prefix="/users")

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5050)
