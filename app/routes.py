from flask import render_template, redirect, url_for, flash
from app import app, db
from flask import request, jsonify
from app.models.models import Catalog, Items, User
from forms import (
    AddCategoryForm,
    AddItemForm,
    EditItemForm,
    LoginForm,
    RegistrationForm,
)
from flask_login import current_user, login_user, logout_user, login_required
import json
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
def index():
    catalogs = [{"id": c.id, "name": c.name} for c in Catalog.query.all()]
    items = [{"name": i.name, "id": i.id} for i in Items.query.all()]
    return render_template("index.html", title="Home", categories=catalogs, items=items)


@app.route("/category/items", methods=["GET"])
def get_items_for_category():
    category_id = request.args.get("category")
    category_items = Items.query.filter_by(catalog_id=category_id)
    return jsonify([{"id": i.id, "name": i.name} for i in category_items])

@app.route("/items.json", methods=["GET"])
def get_items():
    items = Items.query.all()
    return jsonify([i.as_dict() for i in items])


@app.route("/category/item", methods=["GET"])
def get_item_description():
    item_id = request.args.get("item")
    item = Items.query.filter_by(id=item_id).first()
    return render_template(
        "item.html", item=item.name, description=item.description, id=item_id
    )


@app.route("/category/add", methods=["GET", "POST"])
@login_required
def add_category():
    form = AddCategoryForm()
    if form.validate_on_submit():
        catalog_entry = Catalog(form.category.data)
        db.session.add(catalog_entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_category.html", form=form)


@app.route("/items/add", methods=["GET", "POST"])
@login_required
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        item_entry = Items(
            form.item.data, form.item_description.data, form.category.data
        )
        db.session.add(item_entry)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_add_item.html", form=form)


@app.route("/items/edit", methods=["GET", "POST"])
@login_required
def edit_item():
    item_id = request.args.get("item")
    item = Items.query.filter_by(id=item_id).first()
    form = EditItemForm()
    if form.validate_on_submit():
        item.name = form.item.data
        item.description = form.item_description.data
        db.session.commit()
        return redirect(url_for("index"))
    category = Catalog.query.filter_by(id=item.catalog_id).first()
    form.category.data = category.name
    form.item.data = item.name
    form.item_description.data = item.description
    return render_template("edit_add_item.html", form=form)


@app.route("/items/delete", methods=["POST"])
@login_required
def delete_item():
    item_id = request.args.get("item")
    item = Items.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
            return redirect(next_page)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data, email=form.email.data, password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)
