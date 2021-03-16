# Daniel Lehmuth
# 1936204

class ItemToPurchase:          # class for item to purchase
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_item_cost = self.item_price * self.item_quantity
        return print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, int(self.item_price),
                                                int(total_item_cost)))


if __name__ == "__main__":        # the main program code

    item1 = ItemToPurchase()       # first instance of ItemToPurchase class

    print("Item 1")
    item1.item_name = input("Enter the item name:\n")         # get user input
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    item2 = ItemToPurchase()        # second instance of ItemToPurchase class

    print()
    print("Item 2")
    item2.item_name = input("Enter the item name:\n")          # get user input
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    # add the total
    total_cost = int(item1.item_price * item1.item_quantity) + int(item2.item_price * item2.item_quantity)

    print()
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: ${}".format(total_cost))
