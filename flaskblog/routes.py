from flask import render_template, url_for, flash, redirect, request
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

allposts = [
    {
        'author': "Sadhin",
        'title': "Blog post 1",
        'content': "First post content",
        'date_posted': "April 20, 2023"
    },
    {
        'author': "Jone Doe",
        'title': "Blog post 2",
        'content': "Second post content",
        'date_posted': "May 10, 2023"
    }
]


@app.route("/")
def home():
    return render_template("home.html", posts=allposts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), "success")
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.email.data == "me@mail.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful! Check email and password", 'danger')

    return render_template("login.html", title="Login", form=form)

