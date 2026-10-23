from flask import Flask, render_template, request
import random
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order", methods=['GET','POST'])
def order():
    itemliste = ["mus", "iphone", "valve", "uno", "3ds"]
    if request.method == "POST":
        produkt = request.form.get("produkt")
        items = request.form.get("items")
        navn = request.form.get("navn")
        email = request.form.get("email")
        pnummer = request.form.get("pnummer")
        
        
        print(produkt)
        print(items)
        return render_template("resultat.html", items=items, produkt=produkt, navn=navn, pnummer=pnummer, email=email)
    return render_template("orders.html", itemliste=itemliste)


@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
 app.run(debug=True)