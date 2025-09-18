from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User, Item

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        name = request.form.get("name", "").strip()
        password = request.form.get("password", "").strip()
        if not email or not name or not password:
            flash("All fields are required.", "error")
            return render_template("register.html")
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return render_template("register.html")
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.dashboard"))
        flash("Invalid credentials.", "error")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@bp.route("/dashboard")
@login_required
def dashboard():
    items = Item.query.filter_by(owner_id=current_user.id).all()
    return render_template("dashboard.html", items=items)

@bp.route("/items/create", methods=["POST"])
@login_required
def create_item():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if not title:
        flash("Title is required.", "error")
        return redirect(url_for("main.dashboard"))
    item = Item(title=title, description=description, owner_id=current_user.id)
    db.session.add(item)
    db.session.commit()
    flash("Item created.", "success")
    return redirect(url_for("main.dashboard"))

@bp.route("/items/<int:item_id>/update", methods=["POST"])
@login_required
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.owner_id != current_user.id:
        flash("Unauthorized.", "error")
        return redirect(url_for("main.dashboard"))
    item.title = request.form.get("title", item.title).strip()
    item.description = request.form.get("description", item.description).strip()
    db.session.commit()
    flash("Item updated.", "success")
    return redirect(url_for("main.dashboard"))

@bp.route("/items/<int:item_id>/delete", methods=["POST"])
@login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.owner_id != current_user.id:
        flash("Unauthorized.", "error")
        return redirect(url_for("main.dashboard"))
    db.session.delete(item)
    db.session.commit()
    flash("Item deleted.", "success")
    return redirect(url_for("main.dashboard"))
