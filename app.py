from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8be8ee977461bc714355f66f4be67f81'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# creating the extension
db = SQLAlchemy(app)
# initialize the app with the extension
# db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User {}, Email: {}, Image: {}".format(self.username, self.email, self.image_file)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return "Post title: {}, Date: {}".format(self.title, self.date_posted)


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
    if form.email.data == "me@mail.com" and form.password.data == "password":
        flash("You have been logged in!", "success")
        return redirect(url_for('home'))
    else:
        flash("Login Unsuccessful! Check email and password", 'danger')

    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# (flask_blog) PS E:\Projects\flask_blog> python
# Python 3.10.11 | packaged by Anaconda, Inc. | (main, May 16 2023, 00:55:32) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from app import db, User, Post
# >>> app.app_context().push()
# (flask_blog) PS E:\Projects\flask_blog> python
# Python 3.10.11 | packaged by Anaconda, Inc. | (main, May 16 2023, 00:55:32) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>>
# >>> from app import User, Post
# >>> user_1 = User(username='sadhin',email='sadhin.mail.com',password='password')
# >>> db.session.add(user_1)
# >>> user_2 = User(username='jonedoe',email='jd.mail.com',password='password')
# >>> db.session.add(user_2)
# >>> db.session.commit()
# >>> User.query.all()
# [User sadhin, Email: sadhin.mail.com, Image: default.jpg, User jonedoe, Email: jd.mail.com, Image: default.jpg]
# >>> User.query.first()
# User sadhin, Email: sadhin.mail.com, Image: default.jpg
# >>> User.query.filter_by(username='jonedoe').all()
# [User jonedoe, Email: jd.mail.com, Image: default.jpg]
# >>> User.query.filter_by(username='jonedoe').first()
# User jonedoe, Email: jd.mail.com, Image: default.jpg
# >>> user = User.query.filter_by(username='sadhin').first()
# >>> user
# User sadhin, Email: sadhin.mail.com, Image: default.jpg
# >>> user.id
# 1
# >>> user
# User sadhin, Email: sadhin.mail.com, Image: default.jpg
# >>> user.post
# >>> user.posts
# []
# >>> user.id
# 1
# >>> post_1 = Post(title="Temp blog", content="First post content!", user_id= user.id)
# >>> post_2 = Post(title="Temp blog 2", content="Second post content!", user_id= user.id)
# >>> db.session.add()
# >>> db.session.add(post_1)
# >>> db.session.add(post_2)
# >>> db.session.commit()
# >>> user.posts
# [Post title: Temp blog, Date: 2023-06-18 14:21:30.055627, Post title: Temp blog 2, Date: 2023-06-18 14:21:30.055627]
# >>> for p in user.posts:
# ...     print(p.title)
# ...
# Temp blog
# Temp blog 2
# >>> p = Post.query.first()
# >>> p
# Post title: Temp blog, Date: 2023-06-18 14:21:30.055627
# >>> p.user_id
# 1
# >>> p.author
# User sadhin, Email: sadhin.mail.com, Image: default.jpg
# >>> db.drop_all()
# >>> db.create_all()
# >>> User.query.all()
# []
# >>> Post.query.all()
# []
