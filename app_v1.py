class CoffeeShop:
    def __init__(self):
        self.menu = {
            'espresso': 3.50,
            'latte': 4.00,
            'cappuccino': 3.80,
            'macchiato': 3.75,
            'americano': 3.20
        }
        self.inventory = {
            "espresso": 1000,
            "latte": 500,
            "cappuccino": 1000,
            "macchiato": 500,
            "americano": 500,
        }
        # For simplicity we will use items in the menu but alternatively you could use:
        # self.inventory = {"coffee_beans": 1000, "milk": 500, "water": 1000, "cups": 500}
        self.sales = 0.0

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self, item):
        if item in self.menu:
            if self.check_inventory(item):
                self.process_order(item)
                print(f"Enjoy your {item}!")
            else:
                print("Sorry, we are out of stock for this item.")
        else:
            print("Sorry, that item is not on the menu.")

    def check_inventory(self, item):
        # Simplified inventory check for demonstration
        # In a real application, this would deduct items from inventory
        return True  # Assume always in stock for simplicity

    def process_order(self, item):
        self.sales += self.menu[item]
        # Deduct items from inventory (not implemented in this basic example)


# Example usage:
coffee_shop = CoffeeShop()
coffee_shop.display_menu()
coffee_shop.take_order('latte')
print(coffee_shop.sales)