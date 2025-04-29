from datastructures.array import Array
from projects.project3.Drink import Drink
class Menu:
    def __init__(self):
        self._menu = Array(starting_sequenc = [], data_type = Drink)
        self._menu.append(Drink())
        self._menu.append(Drink())
        self._menu.append(Drink())
        self._menu.append(Drink())
        self._menu.append(Drink())

    def get_drink(self, num: int) ->Drink:
        return self._menu[num]

    def __str__(self):
        print(self._menu)
