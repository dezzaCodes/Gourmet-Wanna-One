from abc import ABC


class Item(ABC):
	def __init__(self, name, price):
		self._name = name
		self._price = price

	def getName(self):
		return self._name

	def getPrice(self):
		return self._price


class Ingredient(Item):
	def __init__(self, name, price):
		super().__init__(name, price)
#
# class Side(Item):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self._size = size
#
#     @property
#     def size(self):
#         return self._size
#
#     @size.setter
#     def size(self, size):
#         self._size = size
#
#
# class Bun(Item):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#
#
# class Patty(Item):
#     def __init__(self, name, price):
#         super().__init__(name, price)
