from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/profile")
def profile():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "profile.csv"))
    profile_data = {}
    for _, row in df.iterrows():
        category = row["category"]
        if category not in profile_data:
            profile_data[category] = []
        profile_data[category].append({"label": row["label"], "value": row["value"]})
    return render_template("profile.html", profile_data=profile_data)

app.run(debug=True)