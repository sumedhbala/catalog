from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField,
    SelectField,
)
from wtforms.validators import DataRequired, Required, Email, EqualTo, ValidationError
from app.models.models import Catalog, Items, User


class AddCategoryForm(FlaskForm):
    category = StringField("Category Name", validators=[DataRequired()])
    submit = SubmitField("Add")


class AddItemForm(FlaskForm):

    category = SelectField("Category", validators=[Required()], coerce=int)
    item = StringField("Item Name", validators=[DataRequired()])
    item_description = TextAreaField()
    submit = SubmitField("Add")

    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id, c.name) for c in Catalog.query.all()]


class EditItemForm(FlaskForm):
    category = StringField("Category", render_kw={"readonly": True})
    item = StringField("Item Name", validators=[DataRequired()])
    item_description = TextAreaField()
    submit = SubmitField("Modify")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")
