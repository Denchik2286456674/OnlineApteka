from flask import Flask, render_template
from sql_queries import AptekaDB

app = Flask(__name__)
db = AptekaDB()

app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    categories = db.get_categories()
    items = db.get_all_items()

    return render_template("index.html", items=items, categories=categories)

@app.route("/item/<item_id>")
def item(item_id):
    icategories = db.get_categories()
    item = db.get_item(item_id)

    return render_template("item.html", item=item, categories=categories)

@app.route("/category/<id>")
def category(id):
    categories = db.get_categories()
    items = db.get_category_items(id)

    return render_template("category.html", items=items, categories=categories)

@app.route("/order/<item_id>", methods=["GET", "POST"])
def order(item_id):
    categories = db.get_categories()
    item = db.get_item(item_id)
    if request.method == 'POST':
        #try:
            db.add_order(item[0],
                        request.form["name"], 
                        request.form["phone"],
                        request.form["email"],
                        request.form["city"],
                        request.form["address"],
                        item[5])
            flash("Додано до замовлення!", "alert-dark")
            return redirect(url_for('index'))
        #except:
            flash("Помилка оформлення замовлення!", "alert_danger")
 
    return render_template("order.html", item=item, categories=categories)

if __name__ =="__main__":
    app.config['TAMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)