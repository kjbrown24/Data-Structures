from datastructures.linkedlist import LinkedList
from projects.project3.Drink import Drink
class Customer_Order:
    def __init__(self, name):
        self._order = LinkedList(data_type= Drink)
        self.name = name

    def add_drink(self, drink) -> None:
        customize = input("Do you want customization? (Y)es or (N)o:")
        if customize == 'Y':
            customization_description = input("please take customization request")
            drink.customization == customization_description
        self._order.append(drink)

    def remove_drink(self, drink) ->None:
        self._order.remove(drink)

    def restart_order(self,drink) -> None:
        self._order.clear()
    
    def repeat_order(self) -> None:
        for order in self._order:
            print(order)
    
    def total(self) -> float:
        sum = 0
        for order in self._order:
            sum += order.price
        return sum
    def total_sold(self) -> int:
        sum = 0
        for order in self._order:
            sum += order.price
        return


