import datetime

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://ryan_01:zxcv1122@microblog-application.tmwkt.mongodb.net/test")
app.db = client.microblog
entries = []


@app.route("/", methods=["GET", "POST"])
def home():
    # print([e for e in app.db.entries.find({})])
    if request.method == "POST":
        entry_content = request.form.get("content") # 接收 name = content
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))
        app.db.entries.insert({"content": entry_content, "date": formatted_date})
    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime(" %b %d")
        )
        for entry in entries
    ]
    return render_template("home.html", entries= entries_with_date)