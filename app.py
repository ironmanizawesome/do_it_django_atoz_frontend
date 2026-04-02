from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog_list")
def blog_list():
    return render_template("blog_list.html")

@app.route("/about")
def about():
    return render_template("about_me.html")

app.run(debug=True)