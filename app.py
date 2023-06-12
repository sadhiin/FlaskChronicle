from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
