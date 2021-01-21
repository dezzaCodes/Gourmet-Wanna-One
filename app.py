from flask import Flask, request, render_template
from restaurant import Restaurant
import pickle

app = Flask(__name__, template_folder='templates')

restaurant = Restaurant()
order = None
userID = None

pickle_in = open("ingredients.pickle", "rb")
inventory = pickle.load(pickle_in)
restaurant.setInventory(inventory)


@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('base.html')


@app.route("/order", methods=['GET', 'POST'])
def order():
	global main
	global order
	global userID

	if request.method == 'POST':
		if "burger" in request.form:
			order = restaurant.createOrder()
			userID = order.getID()
			# main = restaurant.makeBurger()
			return render_template('order.html', main="Burger")

		if "custom" in request.form:
			main = restaurant.makeBurger()
			return render_template('order.html', inventory=restaurant.inventory(), main="Burger")

		if "cheeseburger" in request.form:
			pass

		if "wrap" in request.form:
			order = restaurant.createOrder()
			userID = order.getID()
			main = restaurant.makeWrap()
			return render_template('order.html', inventory=restaurant.inventory(), main="Wrap")

		if "main" in request.form:
			for key in request.form.keys():
				if key != "main":
					restaurant.addIngredient(key, main, int(request.form[key]))
			pickle_out = open("ingredients.pickle", "wb")
			pickle.dump(restaurant.inventory(), pickle_out)
			pickle_out.close()
			restaurant.addToOrder(main, userID, 1)
			for order in restaurant.orders:
				if len(order.getMain()) == 0:
					restaurant.orders.remove(order)
			return render_template('order.html')
	return render_template('order.html')


@app.route("/inventory", methods=['GET', 'POST'])
def inventory():
	if request.method == "POST":
		if "add" in request.form:
			ingredient = request.form['ingredient']
			amount = request.form['amount']
			ingredient = restaurant.getIngredientByName(str(ingredient))
			if ingredient is None:
				ingredient = request.form['ingredient']
			price = request.form['price']
			if price == '':
				price = 0
			restaurant.addInventory(ingredient, int(amount), int(price))

		if "remove" in request.form:
			ingredient = request.form['ingredient']
			amount = request.form['amount']
			ingredient = restaurant.getIngredientByName(str(ingredient))
			restaurant.removeInventory(ingredient, int(amount), int(price))

		if "plus" in request.form:
			for key, val in request.form.items():
				print(key, val)
				if key != "plus":
					ingredient = restaurant.getIngredientByName(key)
					amount = val
					restaurant.addInventory(ingredient, int(amount), 0)

		if "minus" in request.form:
			for key, val in request.form.items():
				print(key, val)
				if key != "minus":
					ingredient = restaurant.getIngredientByName(key)
					amount = val
					restaurant.removeInventory(ingredient, int(amount))

		pickle_out = open("ingredients.pickle", "wb")
		pickle.dump(restaurant.inventory(), pickle_out)
		pickle_out.close()
	return render_template('inventory.html', inventory=restaurant.inventory())


@app.route("/staff", methods=['GET', 'POST'])
def staff():
	if request.method == "POST":
		if "update" in request.form:
			orderID = request.form['update']
			order = restaurant.getOrderByID(int(orderID))
			restaurant.orderComplete(order)
			return render_template('staff.html', orders=restaurant.orders)

		if "delete" in request.form:
			orderID = request.form['delete']
			order = restaurant.getOrderByID(int(orderID))
			restaurant.removeOrder(order)
			return render_template('staff.html', orders=restaurant.orders)

	return render_template('staff.html', orders=restaurant.orders)


@app.route("/status", methods=['GET', 'POST'])
def status():
	if request.method == "POST":
		if "status" in request.form:
			orderID = request.form['orderID']
			order = restaurant.getOrderByID(int(orderID))
			status = order.getStatus()
			return render_template('status.html', status=status)
	return render_template('status.html')


app.run(debug=True)
