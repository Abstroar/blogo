from flask import *

import datetime
import requests


app = Flask(__name__)

@app.route("/<int:id>")
def pos(id):
    dat = requests.get("https://api.npoint.io/20a580117f0366cee8e0").json()

    return render_template("post.html", data=dat[id])



@app.route("/")
def hello_ok():
    dat = requests.get("https://api.npoint.io/20a580117f0366cee8e0").json()

    return render_template("index.html",data=dat)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)

