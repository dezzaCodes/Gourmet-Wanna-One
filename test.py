from ingredient import Ingredient
from main import Burger
from order import Order
from restaurant import Restaurant

tomato = Ingredient('tomato', 0.5)
lettuce = Ingredient('lettuce', 0.3)
patty = Ingredient('patty', 3)
coke = Ingredient('coke', 2)

burger = Burger()
burger.addIngredient(tomato, 3)
burger.addIngredient(lettuce, 2)
burger.addIngredient(patty, 1)

burger.removeIngredient(tomato, 0)
burger.removeIngredient(tomato, 17)

print(burger.getPrice())

derrick = Order()
derrick.addMain(burger, 3)
derrick.addSide(coke, 1)

print(derrick.getID())
print(derrick.getStatus())


mcd = Restaurant()
mcd.addOrder(derrick)

print(derrick.getID())
print(derrick.getStatus())

print(derrick.getPrice())