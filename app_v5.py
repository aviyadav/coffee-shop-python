# v5

class Customer:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def display_points(self):
        print(f"{self.name}'s Points: {self.points}")

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

        self.sales = 0.0
        self.customers = {}

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self, item, customer_name):
        if item in self.menu:
            if self.check_inventory(item):
                self.process_order(item, customer_name)
                print(f"Enjoy your {item}, {customer_name}!")
            else:
                print("Sorry, we are out of stock for this item.")
        else:
            print("Sorry, that item is not on the menu.")

    def check_inventory(self, item):
        if item in self.inventory:
            if self.inventory[item] > 0:
                return True
            else:
                return False
        else:
            return False

    def process_order(self, item, customer_name):
        if self.check_inventory(item):
            self.sales += self.menu[item]
            self.deduct_inventory(item)
            self.update_customer_points(customer_name, self.menu[item])
        else:
            print("Sorry, we are out of stock for this item.")

    def deduct_inventory(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            self.inventory[item] -= 1
        else:
            print(f"Error: Cannot deduct {item} from inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

    def replenish_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
            print(f"Added {quantity} units of {item} to inventory.")
        else:
            print("That item does not exist in the inventory.")

    def update_customer_points(self, customer_name, amount_spent):
        if customer_name in self.customers:
            self.customers[customer_name].add_points(int(amount_spent * 10)) # Reward 10 points for each dollar spent
        else:
            self.customers[customer_name] = Customer(customer_name)
            self.customers[customer_name].add_points(int(amount_spent * 10))

    def display_customer_points(self, customer_name):
        if customer_name in self.customers:
            self.customers[customer_name].display_points()
        else:
            print(f"{customer_name} is not a registered customer.")


    def report_sales(self):
        print(f"Total Sales: ${self.sales:.2f}")

    def report_inventory(self):
        total_items = sum(self.inventory.values())
        print(f"Total Inventory Items: {total_items}")

# Example usage:
coffee_shop = CoffeeShop()
coffee_shop.display_menu()
coffee_shop.take_order('latte', 'Alice')
coffee_shop.display_customer_points('Alice')
coffee_shop.display_inventory()
coffee_shop.replenish_inventory('latte', 200)
coffee_shop.report_sales()
coffee_shop.report_inventory()