class Order():

    def __init__(self):
        self._mains = {}
        self._sides = {}
        self._status = ''
        self._ID = None

    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID

    def setStatus(self, status):
        self._status = status

    def getMain(self):
        return self._mains

    def getSide(self):
        return self._sides

    def getStatus(self):
        return self._status

    def addMain(self, item, amount):
        if amount <= 0:
            return

        if item in self._mains:
            self._mains[item] += amount
        else:
            self._mains[item] = amount

    def removeMain(self, item, amount):
        if amount <= 0:
            return

        if item in self._mains:
            self._mains[item] -= amount
        else:
            return

        if self._mains[item] <= 0:
            self._mains.pop(item)

    def addSide(self, item, amount):
        if amount <= 0:
            return

        if item in self._sides:
            self._sides[item] += amount
        else:
            self._sides[item] = amount

    def removeSide(self, item, amount):
        if amount <= 0:
            return

        if item in self._sides:
            self._sides[item] -= amount
        else:
            return

        if self._sides[item] <= 0:
            self._sides.pop(item)

    def getPrice(self):
        cost = 0
        for item in self._mains:
            cost += item.getPrice() * self._mains[item]

        for item in self._sides:
            cost += item.getPrice() * self._sides[item]

        return cost
