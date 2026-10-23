from flask import Flask, render_template, request
import random
 
app = Flask(__name__)

@app.route("/")
def index():
     itemliste = ["mus", "iphone", "valve", "uno", "3ds"]

     if request.method == "POST":
        nivaa = request.form.get("nivaa")
        items = request.form.get("items")
        return render_template("index.html", items=items, nivaa=nivaa)



@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
 app.run(debug=True)