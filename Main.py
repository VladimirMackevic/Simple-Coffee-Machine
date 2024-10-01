# Resources in a coffee machine
water = 1000
beans = 100
milk = 1000
coins = 10.00


# Definition of a class
class Coffee:
    def __init__(self, name, water, beans, milk, price, number):
        self.name = name
        self.water = water
        self.beans = beans
        self.milk = milk
        self.price = price
        self.number = number

    def __str__(self):
        return f'{self.name} {self.water} {self.beans} {self.milk} {self.price:.2f} {self.number}'


# Objects of the menu
latte = Coffee('Latte', 20, 10, 80, 2.00, 1)
black = Coffee('Black coffee', 100, 30, 0, 1.00, 2)
cappuccino = Coffee('Cappuccino', 50, 20, 50, 1.50, 3)


# Coffee name list, idk, maybe a more efficient way to list coffee is possible
coffee_list = [latte.name, black.name, cappuccino.name]


# Dictionary, idk, I am bad with them
coffee_dictionary = {latte.number: latte, black.number: black, cappuccino.number: cappuccino}


# Basically the logic part
def menu_interface():
    global water, beans, milk, coins
    x = int(input('Select 1 for coffee list, select 2 for resources\n'))
    if x == 2:
        print(f'water {water}\nBeans {beans}\nMilk {milk}\nCoins {round(coins, 2)}')
        y = int(input('Press 1 to refill, and press any key to go back\n'))
        if y == 1:
            water = 1000
            beans = 100
            milk = 1000
            coins = 10.00
            menu_interface()
        else:
            menu_interface()
    elif x == 1:
        for coffee in coffee_list:
            print(coffee)
        y = int(input('Select number\n'))
        if y in coffee_dictionary:
            y2 = float(input(f'Please insert {coffee_dictionary[y].price} coins '))
            while y2 < coffee_dictionary[y].price:
                additional_coins = float(input(f'Please insert {round(coffee_dictionary[y].price - y2, 2)} coins '))
                y2 += additional_coins
            if y2 == coffee_dictionary[y].price and water >= coffee_dictionary[y].water and beans >= coffee_dictionary[y].beans and milk >= coffee_dictionary[y].milk:
                coins += y2
                water -= coffee_dictionary[y].water
                milk -= coffee_dictionary[y].milk
                beans -= coffee_dictionary[y].beans
                input('Enjoy your Coffee! ')
                menu_interface()
            elif y2 > coffee_dictionary[y].price and y2 <= coins and water >= coffee_dictionary[y].water and beans >= coffee_dictionary[y].beans and milk >= coffee_dictionary[y].milk:
                coins += y2
                water -= coffee_dictionary[y].water
                milk -= coffee_dictionary[y].milk
                beans -= coffee_dictionary[y].beans
                y3 = float(y2 - coffee_dictionary[y].price)
                coins -= y3
                input(f'Enjoy your Coffee! Change {round(y3, 2)} ')
                menu_interface()
            elif y2 > coffee_dictionary[y].price and y2 > coins:
                input('Too many coins inserted ')
                menu_interface()
            elif y2 >= coffee_dictionary[y].price and water < coffee_dictionary[y].water:
                input('Not enough resources ')
                menu_interface()
            elif y2 >= coffee_dictionary[y].price and beans < coffee_dictionary[y].beans:
                input('Not enough resources ')
                menu_interface()
            elif y2 >= coffee_dictionary[y].price and milk < coffee_dictionary[y].milk:
                input('Not enough resources ')
                menu_interface()
        else:
            menu_interface()


menu_interface()



