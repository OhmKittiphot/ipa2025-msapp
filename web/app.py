from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
mydb = client["router"]
mycol = mydb["routerdevice"]

@app.route("/")
def main():
    return render_template("index.html", data=mycol.find())

@app.route("/add", methods=["POST"])
def add_comment():
    IP = request.form.get("IP")
    Username = request.form.get("Username")
    Password = request.form.get("Password")

    if IP and Username and Password:
         mycol.insert_one({"IP": IP, "Username": Username, "Password": Password})
    return redirect(url_for("main"))

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
    app.run(host="0.0.0.0", port=8090)
    