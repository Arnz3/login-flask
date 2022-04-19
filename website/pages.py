from flask import Blueprint, render_template
from flask_login import current_user, login_required

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")

@pages.route("/account")
@login_required
def account():
    return render_template("account.html", user=current_user, email=current_user.email)