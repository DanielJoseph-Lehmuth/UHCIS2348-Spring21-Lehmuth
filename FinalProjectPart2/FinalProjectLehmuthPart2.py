# Daniel Lehmuth
# 1936204

import csv
import datetime


class InventoryItem:  # initialize a class for the inventory items
    def __init__(self, item_id='none', item_manufacturer='none', item_type='none', item_price=0, item_service_date='',
                 item_damage_status=False, item_damage_notation=''):
        self.item_id = item_id
        self.item_manufacturer = item_manufacturer
        self.item_type = item_type
        self.item_price = item_price
        self.item_service_date = item_service_date
        self.item_damage_status = item_damage_status
        self.item_damage_notation = item_damage_notation


class InventoryList:
    list_item = InventoryItem()

    def __init__(self, inventory_name='Inventory_initial'):  # this creates the inventory list
        self.inventory_name = inventory_name
        self.inventory_list = []

    def add_item(self, list_item):  # adds each inventory item to the list
        self.inventory_list.append(list_item)

    def update_price(self, id_num, item_price_update):  # adds/updates the price of an item by ID
        user_item_id = id_num
        user_price_update = item_price_update
        for list_item in self.inventory_list:
            if list_item.item_id == user_item_id:
                list_item.item_price = user_price_update

    def update_date(self, id_num, item_date_update):  # adds/updates the service date of an item
        user_item_id = id_num
        user_date_update = item_date_update
        for list_item in self.inventory_list:
            if list_item.item_id == user_item_id:
                list_item.item_service_date = user_date_update

    def search_inventory(self):  # this begins the class method for searching through the inventory

        def print_item(list_name):  # this is used to print a suggested item and is called later
            print('You may, also, consider: {}, {} {}, ${}\n'.format(list_name[0], list_name[1], list_name[2],
                                                                     list_name[3]))

        def most_expensive(name_of_list):  # This is used to sort items by price and is called later
            price_of_item = name_of_list[3]
            return price_of_item

        # This begins the interactive while loop. The user is prompted to enter an item and 'q' to quit.
        today_is = datetime.date.today()
        print("Welcome to the Interactive Inventory Query! Enter 'q' at any time to quit.\n")
        search_string = input('What item would you like to find by Manufacturer name and item type:\n')
        # If the user inputs 'q' before anything else, it quits the program and does not enter the loop
        if search_string == 'q':
            print('Maybe next time. Have a good day!')
        while search_string != 'q':
            search_list = search_string.split(' ')  # Takes user input and splits it into a list
            searched_item_list = []  # this is used for the item they are searching for
            suggested_item_list = []  # this is used to suggest an item that is similar to the searched item

            # This for loop goes through the inventory and compares it to user input.
            for list_item in self.inventory_list:
                small_list = [list_item.item_id, list_item.item_manufacturer, list_item.item_type, list_item.item_price,
                              list_item.item_service_date, list_item.item_damage_notation]
                man_type_list = [list_item.item_manufacturer, list_item.item_type]
                date_check = list_item.item_service_date.split('/')
                compare_date = datetime.date(int(date_check[2]), int(date_check[0]), int(date_check[1]))
                product_check = all(thing in search_list for thing in man_type_list)
                # If the manufacturer and item name match,
                # it checks to make sure the item is not damaged or past service date.
                # Then it appends the small_list to the searched_item_list.
                if product_check is True and list_item.item_damage_notation == '' and today_is < compare_date:
                    searched_item_list.append(small_list)
                # It also takes any matching item names and appends them to the suggested_item_list.
                if list_item.item_type in search_list and (list_item.item_damage_notation == '') and \
                        (today_is < compare_date) and list_item.item_manufacturer not in search_list:
                    suggested_item_list.append(small_list)

            if len(searched_item_list) < 1:  # If there are no matches in the inventory then it prints this statement
                print('No such item in inventory.\n')

            # This checks if there are items in the searched_item_list and the suggested_item_list.
            if len(searched_item_list) >= 1 and len(suggested_item_list) >= 1:
                # This most_expensive is called as a key and sorts the searched_item_list by highest price
                sorted_item_list = sorted(searched_item_list, key=most_expensive, reverse=True)
                user_selected_item = sorted_item_list[0]
                user_suggested_item = []  # used for the suggested item
                print("Your item is: {}, {} {}, ${}\n".format(user_selected_item[0], user_selected_item[1],
                                                              user_selected_item[2], user_selected_item[3]))
                closest_price = 1000000  # initializes closest price
                for alt_item in suggested_item_list:
                    # This for loop goes through the suggested_item_list and replaces the item with the closest price
                    # to user_suggested_item list.
                    item_price_difference = abs(alt_item[3] - user_selected_item[3])
                    if item_price_difference < closest_price:
                        closest_price = item_price_difference
                        user_suggested_item = alt_item
                # This calls print_alt_item to print user_suggested_item in the correct format
                print_item(user_suggested_item)

            # This part of the code executes if there is nothing in the search_list,
            # but there are some in the suggested_item_list.
            if len(suggested_item_list) >= 1 and len(search_list) > 1:
                if len(searched_item_list) < 1:
                    # This calls most_expensive as the key to sort the suggested_item_list with the highest price.
                    sorted_suggested_list = sorted(suggested_item_list, key=most_expensive, reverse=True)
                    sorted_suggested_item = sorted_suggested_list[0]
                    # This calls print_alt_item and prints the highest priced item in the correct format.
                    print_item(sorted_suggested_item)

            # This prompts the user for their next input to continue the while loop.
            search_string = input('What next item would you like to find by Manufacturer name and item type:\n')
            #  If the user inputs 'q' this message appears before the program quits.
            if search_string == 'q':
                print('Thank you, have a nice day!')


inventory1 = InventoryList()  # beginning of code outside of the class methods

with open('ManufacturerList.csv', 'r') as my_file:  # first file opened used to start list of inventory
    manufacturer_doc = csv.reader(my_file)

    for item in manufacturer_doc:
        item1 = InventoryItem()
        item_values = []
        for value in item:  # assigns each value to the class variable
            item_values.append(value)
        item1.item_id = item_values[0]
        item1.item_manufacturer = item_values[1].strip()
        item1.item_type = item_values[2]
        if len(item_values[3]) >= 1:
            item1.item_damage_status = True
            item1.item_damage_notation = item_values[3]  # use the original marking for the damage indicator
        inventory1.add_item(item1)

with open('PriceList.csv', 'r') as my_file:
    price_doc = csv.reader(my_file)  # price list used to add the price of each item

    for id_num_price in price_doc:
        inventory1.update_price(id_num_price[0], int(id_num_price[1]))

with open('ServiceDatesList.csv', 'r') as my_file:  # used to add the service dates to each item
    date_doc = csv.reader(my_file)

    for id_num_date in date_doc:
        inventory1.update_date(id_num_date[0], id_num_date[1])

# now all the items are part of the inventory list with their correct info

inventory1.search_inventory()  # this calls the class method to allow the user to search through the inventory
