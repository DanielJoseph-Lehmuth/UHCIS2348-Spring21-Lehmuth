# Daniel Lehmuth
# 1936204

class ItemToPurchase:          # class for item to purchase
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description    # added item description

    def print_item_cost(self):
        total_item_cost = self.item_price * self.item_quantity
        return print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, int(self.item_price),
                                                int(total_item_cost)))

    def print_item_description(self):                   # added print item description method
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:                              # added new class shopping cart

    shopping_cart_item = ItemToPurchase()

    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, shopping_cart_item):
        self.cart_items.append(shopping_cart_item)

    def remove_item(self, item):
        item_count = 0
        for shopping_cart_item in self.cart_items:
            if shopping_cart_item.item_name == item:
                self.cart_items.remove(shopping_cart_item)
            if shopping_cart_item.item_name != item:
                item_count += 1
        if item_count == len(self.cart_items):
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, shopping_cart_item):
        item_count = 0
        user_item_name = input("Enter the item name:\n")
        user_quantity = int(input("Enter the new quantity:\n"))
        for shopping_cart_item in self.cart_items:
            if shopping_cart_item.item_name == user_item_name:
                shopping_cart_item.item_quantity = user_quantity
            if shopping_cart_item.item_name != user_item_name:
                item_count += 1
        if item_count == len(self.cart_items):
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for shopping_cart_item in self.cart_items:
            num_items_in_cart += shopping_cart_item.item_quantity
        return num_items_in_cart

    def get_cost_of_cart(self):
        cost_of_cart = 0
        for shopping_cart_item in self.cart_items:
            cost_of_cart += (shopping_cart_item.item_price * shopping_cart_item.item_quantity)
        return int(cost_of_cart)

    def print_total(self):
        total_cost = 0
        for item in self.cart_items:
            item.print_item_cost()
            total_cost += item.item_price
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY\n')

    def print_description(self):
        for item in self.cart_items:
            item.print_item_description()


if __name__ == "__main__":        # the main program code

    def print_menu():                   # Print menu options function
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

    cart1 = ShoppingCart()          # Make ShoppingCart object

    cart1.customer_name = input("Enter customer's name:\n")   # get customer name and today's date
    cart1.current_date = input("Enter today's date:\n")
    print()
    print("Customer name:", cart1.customer_name)
    print("Today's date:", cart1.current_date)
    print()

    print_menu()        # calling print_menu function

    user_input = input("Choose an option:\n")      # prompt user for input, repeats if not menu option

    while user_input != "q":  # Quit menu option
        if user_input == "q":
            break
        if user_input == 'o':                       # menu option "o" outputting shopping cart
            num_items = cart1.get_num_items_in_cart()
            print('OUTPUT SHOPPING CART')
            print("{}'s Shopping Cart - {}".format(cart1.customer_name, cart1.current_date))
            print("Number of Items: {}".format(num_items))
            print()
            if num_items == 0:
                cart1.print_total()
            else:
                cart1.print_total()
                print()
            print("Total: ${}".format(cart1.get_cost_of_cart()))
            print()
            print_menu()

        if user_input == 'i':          # menu option "i" outputting item descriptions
            num_items = cart1.get_num_items_in_cart()
            print()
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            print("{}'s Shopping Cart - {}".format(cart1.customer_name, cart1.current_date))
            print()
            print('Item Descriptions')
            if num_items == 0:
                print("SHOPPING CART IS EMPTY\n")
            else:
                cart1.print_description()
            print()
            print_menu()

        if user_input == 'a':          # menu option 'a' adding item to cart
            item1 = ItemToPurchase()
            print()
            print("ADD ITEM TO CART")
            add_item_name = input("Enter the item name:\n")
            add_item_description = input("Enter the item description:\n")
            add_item_price = int(input("Enter the item price:\n"))
            add_item_quantity = int(input("Enter the item quantity:\n"))

            item1.item_name = add_item_name
            item1.item_description = add_item_description
            item1.item_price = add_item_price
            item1.item_quantity = add_item_quantity
            cart1.add_item(item1)
            print()
            print_menu()

        if user_input == "r":               # option 'r' remove item from cart
            print()
            print("REMOVE ITEM FROM CART")
            item_to_remove = input("Enter name of item to remove:\n")
            cart1.remove_item(item_to_remove)
            print()
            print_menu()

        if user_input == 'c':          # menu "c" option change item quantity
            item1 = ItemToPurchase()
            print()
            print('CHANGE ITEM QUANTITY')
            cart1.modify_item(item1)
            print()
            print_menu()

        user_input = input("Choose an option:\n")
