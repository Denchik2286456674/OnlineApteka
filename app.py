from flask import Flask, render_template
from sql_queries import ShopDB

app = Flask(__name__)
db = ShopDB()


@app.route("/")
def index():
    items = db.get_all_items()

    return render_template("index.html, items=items")

if __name__ =="main":
    app.config['TAMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)