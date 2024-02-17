from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])
    assigned_to = SelectField("Assigned to", choices=[('cha', 'Charina'), ('dan','Danilyn'), ('abby','Abegeil')], validators=[DataRequired()])
    description = CKEditorField("Task Description", validators=[DataRequired()])
    due_date = StringField('Due Date', validators=[DataRequired()])
    status = SelectField("Assigned to", choices=[('pending', 'Pending'), ('done','Done')], validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Create Account")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")
