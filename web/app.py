import os

from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)

mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
mydb = client[db_name]
mycol = mydb["routers"]

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", data=mycol.find())

@app.route("/add", methods=["POST"])
def add_comment():
    IP = request.form.get("IP")
    Username = request.form.get("Username")
    Password = request.form.get("Password")

    if IP and Username and Password:
         mycol.insert_one({"IP": IP, "Username": Username, "Password": Password})
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = ObjectId(request.form.get("idx"))
        if idx:
            mycol.delete_one({"_id" : idx})
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    