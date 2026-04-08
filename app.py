from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog_list")
def blog_list():
    posts = [
        {"title": "제목1", "content": "내용1"},
        {"title": "제목2", "content": "내용2"},
        {"title": "제목3", "content": "내용3"},
    ]
    df = pd.read_csv("data.csv", encoding="cp949", sep="\t")
    df.columns = ["title", "content"]
    print(df.head())
    for index, row in df.iterrows():
        posts.append({"title": row["title"], "content": row["content"]})
    return render_template("blog_list_simple.html",
                           posts=posts)

@app.route("/about")
def about():
    return render_template("about_me.html")

app.run(debug=True)
