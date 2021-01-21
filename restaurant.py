from ingredient import Ingredient
from main import Burger, Wrap
from order import Order


class Restaurant():

	def __init__(self):
		self._orders = []
		self._inventory = {}
		self._num = 1

	@property
	def orders(self):
		return self._orders

	@property
	def num(self):
		return self._num

	def inventory(self):
		return self._inventory

	@num.setter
	def num(self, num):
		self._num = num

	def addOrder(self, order):
		self._orders.append(order)

	def removeOrder(self, order):
		self._orders.remove(order)

	def orderComplete(self, order):
		if order in self._orders:
			order.setStatus('Order ready for collection.')

	def orderStatus(self, order):
		return order.getStatus()

	def makeBurger(self):
		burger = Burger()
		# self._orders.append(burger)
		return burger

	def makeWrap(self):
		wrap = Wrap()
		# self._orders.append(wrap)
		return wrap

	def createOrder(self):
		order = Order()
		order.setID(self._num)
		order.setStatus('We are processing your order.')
		self._orders.append(order)
		self._num += 1
		return order

	def addMain(self, order, main):
		order.addMain(main)

	def addInventory(self, ingredient, amount, price):
		if ingredient in self._inventory:
			self._inventory[ingredient] += int(amount)
		else:
			ingredient = Ingredient(ingredient, price)
			self._inventory[ingredient] = int(amount)

	def addIngredient(self, item, main, amount):
		for stock in self._inventory:
			if stock.getName() == item and self._inventory[stock] >= amount:
				main.addIngredient(stock, amount)
				self._inventory[stock] -= amount

	def addToOrder(self, item, ID, amount):
		for order in self._orders:
			if order.getID() == ID:
				order.addMain(item, amount)

	def getOrderByID(self, ID):
		for order in self._orders:
			if order.getID() == ID:
				return order

	def setInventory(self, inventory):
		self._inventory = inventory

	def getIngredientByName(self, ingredient):
		for item in self._inventory:
			if item.getName().lower() == ingredient.lower():
				return item

	def removeInventory(self, ingredient, amount):
		if ingredient in self._inventory:
			self._inventory[ingredient] -= int(amount)
			if self._inventory[ingredient] < 0:
				self._inventory[ingredient] = 0
