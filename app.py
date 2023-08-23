from flask import Flask, render_template
from sql_queries import AptekaDB

app = Flask(__name__)
db = AptekaDB()

@app.route("/")
def index():
    items = db.get_all_items()

    return render_template("index.html", item=item)

@app.route("/item/<item_id>")
def item(item_id):
    item = db.get_items(item_id)

    return render_template("item.html", item=item)

@app.route("/order/<item_id>", methods=["GET", "POST"])
def order(item_id):
    item = db.get_item(item_id)

    return render_template("order.html", item=item)

if __name__ =="__main__":
    app.config['TAMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)