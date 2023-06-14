from flask import Flask, render_template, url_for
from froms import RegistationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8be8ee977461bc714355f66f4be67f81'
allposts = [
    {
        'author': "Sadhin",
        'title': "Blog post 1",
        'content': "First post content",
        'date_posted': "April 20 2023"
    },
    {
        'author': "Jone Doe",
        'title': "Blog post 2",
        'content': "Second post content",
        'date_posted': "May 10 2023"
    }
]


@app.route("/")
def home():
    return render_template("home.html", posts=allposts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Loin", form=form)


if __name__ == '__main__':
    app.run(debug=True)
