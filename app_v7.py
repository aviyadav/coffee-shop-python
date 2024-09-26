# v7
from app_v6 import CoffeeShop

def run_coffee_shop():
    shop = CoffeeShop()
    while True:
        print("\nWelcome to the Coffee Shop!")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Display Inventory")
        print("4. Replenish Inventory")
        print("5. Display Customer Points")
        print("6. Display Customer Orders")
        print("7. Apply Discount")
        print("8. Report Sales")
        print("9. Report Inventory")
        print("0. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            shop.display_menu()
        elif choice == "2":
            item = input("Enter the item: ")
            customer_name = input("Enter customer name: ")
            shop.take_order(item, customer_name)
        elif choice == "3":
            shop.display_inventory()
        elif choice == "4":
            item = input("Enter the item to replenish: ")
            quantity = int(input("Enter the quantity to add: "))
            shop.replenish_inventory(item, quantity)
        elif choice == "5":
            customer_name = input("Enter customer name: ")
            if customer_name in shop.customers:
                shop.customers[customer_name].display_points()
            else:
                print(f"{customer_name} is not a registered customer.")
        elif choice == "6":
            customer_name = input("Enter customer name: ")
            shop.display_customer_orders(customer_name)
        elif choice == "7":
            customer_name = input("Enter customer name: ")
            shop.apply_discount(customer_name)
        elif choice == "8":
            shop.report_sales()
        elif choice == "9":
            shop.report_inventory()
        elif choice == "0":
            print("Thank you for visiting the Coffee Shop!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    run_coffee_shop()