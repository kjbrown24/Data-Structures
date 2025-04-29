from projects.project3.Menu import Menu
from projects.project3.Customer_Order import Customer_Order
def main():
    menu = Menu
    print(Menu)
    customer_order = Customer_Order
    more == 'Y'
    while more == 'Y':
        start = input('what drinks would you like today?')
        if start ==1:
                customer_order.add_drink(menu.get_drink(0))
        elif start == 2:
            customer_order.add_drink(menu.get_drink(1))
        elif start == 3:
            customer_order.add_drink(menu.get_drink(2))
        elif start == 4:
            customer_order.add_drink(menu.get_drink(3))
        elif start == 5:
            customer_order.add_drink(menu.get_drink(4))
        more = input('Would you like to order another? (Y)es or (N)o')
        pass#repeat loop above 
        customer_order.repeat_order


if __name__ == '__main__':
    main()
