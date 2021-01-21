from abc import ABC


class Main(ABC):
    def __init__(self, price):
        self._ingredients = {}
        self._price = price

    def getIngredients(self):
        return self._ingredients

    def addIngredient(self, ingredient, amount):
        if amount < 0:
            print("cannot add" + str(amount) + ingredient.getName())
            return

        if ingredient in self._ingredients:
            self._ingredients[ingredient] += amount
        else:
            self._ingredients[ingredient] = amount

    def removeIngredient(self, ingredient, amount):
        if amount <= 0:
            print("cannot delete" + str(amount) + ingredient.getName())
            return

        if ingredient in self._ingredients:
            self._ingredients[ingredient] -= amount
        else:
            return

        if self._ingredients[ingredient] <= 0:
            self._ingredients.pop(ingredient)

    def getPrice(self):
        cost = self._price
        for ingredient in self._ingredients:
            cost += ingredient.getPrice() * self._ingredients[ingredient]
        return cost


class Burger(Main):
    def __init__(self):
        super().__init__(0)


class Wrap(Main):
    def __init__(self):
        super().__init__(0)
