# v6

class Customer:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.orders = []

    def add_points(self, points):
        self.points += points

    def remove_points(self, points):
        if self.points >= points:
            self.points -= points
            print(f"{points} points deducted from {self.name}. Remaining points: {self.points}")
        else:
            print(f"Not enough points to deduct {points} points from {self.name}.")

    def display_points(self):
        print(f"{self.name}'s Points: {self.points}")

    def add_order(self, order):
        self.orders.append(order)

    def display_orders(self):
        print(f"{self.name}'s Order History:")
        for order in self.orders:
            print(order)

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
            self.record_order(customer_name, item)
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

    def record_order(self, customer_name, item):
        if customer_name in self.customers:
            self.customers[customer_name].add_order(item)
        else:
            self.customers[customer_name] = Customer(customer_name)
            self.customers[customer_name].add_order(item)

    def display_customer_points(self, customer_name):
        if customer_name in self.customers:
            self.customers[customer_name].display_points()
        else:
            print(f"{customer_name} is not a registered customer.")

    def display_customer_orders(self, customer_name):
        if customer_name in self.customers:
            self.customers[customer_name].display_orders()
        else:
            print(f"{customer_name} is not a registered customer.")

    def apply_discount(self, customer_name):
        if customer_name in self.customers:
            if (
                self.customers[customer_name].points >= 100
            ):  # Example: 100 points = 10% discount
                discount_percent = 10
                discount_amount = self.sales * (discount_percent / 100)
                self.sales -= discount_amount
                self.customers[customer_name].remove_points(
                    100
                )  # Deduct 100 points for 10% discount
                print(
                    f"{customer_name} received a {discount_percent}% discount! New total: ${self.sales:.2f}"
                )
            else:
                print(f"{customer_name} does not have enough points for a discount.")
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
coffee_shop.take_order("latte", "Alice")
coffee_shop.take_order("espresso", "Bob")
coffee_shop.display_customer_orders("Alice")
coffee_shop.display_inventory()
coffee_shop.replenish_inventory("latte", 200)
coffee_shop.report_sales()
coffee_shop.apply_discount("Alice")
coffee_shop.report_sales()
coffee_shop.report_inventory()
print(coffee_shop.customers)

# Display Alice's points
if "Alice" in coffee_shop.customers:
    coffee_shop.customers["Alice"].display_points()
else:
    print("Alice is not a registered customer.")

