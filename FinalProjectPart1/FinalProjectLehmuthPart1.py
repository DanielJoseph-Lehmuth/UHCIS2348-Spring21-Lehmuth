# Daniel Lehmuth
# 1936204

import csv  # import the needed modules
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

    def __init__(self, inventory_name='Inventory_initial'):
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

    def write_full_inventory(self, file_name):
        def sort_by_maker(list_name):  # this is used to sort by manufacturer
            maker_name = list_name[1]
            return maker_name

        with open(file_name, 'w', newline='') as this_file:  # this writes a new file for full inventory list
            full_inventory_file = csv.writer(this_file)
            row = []
            for list_item in self.inventory_list:
                small_row = [list_item.item_id, list_item.item_manufacturer, list_item.item_type, list_item.item_price,
                             list_item.item_service_date, list_item.item_damage_notation]
                row.append(small_row)
            sorted_rows = sorted(row, key=sort_by_maker)  # list gets sorted before writing
            full_inventory_file.writerows(sorted_rows)

    def write_item_type_inventory(self):
        def sort_by_id(list_name):  # this is used to sort by item ID number
            id_number = list_name[1]
            return id_number

        inventory_check_list = []  # used to parse items
        inventory_dict = {}  # dictionary used to group the id numbers by item type
        for list_item in self.inventory_list:
            if list_item.item_type not in inventory_dict:  # creates a new dictionary item if none exist
                inventory_dict[list_item.item_type] = [list_item.item_id]
                inventory_check_list.append(list_item.item_type)
            else:  # if one does, it appends the id number to the list
                inventory_dict[list_item.item_type].append(list_item.item_id)

        # next it iterates through the dictionary to create new file names based on item names
        for name in inventory_dict.keys():
            new_name = name.capitalize()
            new_cap_name = '{}Inventory.csv'.format(new_name)
            with open(new_cap_name, 'w', newline='') as item_file:
                item_inventory = csv.writer(item_file)
                if name in inventory_check_list:  # checks if name is in list. if it is it creates a nested list
                    temp_inventory_list = inventory_dict[name]
                    row = []
                    for list_item in self.inventory_list:  # iterates through the inventory to grab needed items
                        if list_item.item_id in temp_inventory_list:
                            small_row = [list_item.item_id, list_item.item_manufacturer, list_item.item_price,
                                         list_item.item_service_date, list_item.item_damage_notation]
                            row.append(small_row)
                    sorted_rows = sorted(row, key=sort_by_id)
                    item_inventory.writerows(sorted_rows)  # files are written based on item ID number

    def write_needs_service_date(self, file_name):
        def sort_by_date(list_name):  # used to sort by date
            the_date = list_name[4]
            return the_date

        today_is = datetime.date.today()  # get today's date
        with open(file_name, 'w', newline='') as my_date_file:  # creates a new csv file for the service dates
            date_file = csv.writer(my_date_file)
            date_dict = {}  # dictionaries and lists used to sort and parse the data
            parsed_dates_dict = {}
            date_list = []
            for list_item in self.inventory_list:
                # initial run through of the inventory to format dates and add to dictionary
                date_dict[list_item.item_id] = list_item.item_service_date.split('/')
            for id_num in date_dict.keys():  # used to parse dates that are older than today's date
                date_to_add = date_dict[id_num]
                compare_date = datetime.date(int(date_dict[id_num][2]), int(date_dict[id_num][0]),
                                             int(date_dict[id_num][1]))
                if today_is > compare_date:
                    parsed_dates_dict[id_num] = '/'.join(date_to_add)
            for list_item in self.inventory_list:  # used to generate a list filtered by the past service dates
                if list_item.item_id in parsed_dates_dict:
                    temp_date_list = [list_item.item_id, list_item.item_manufacturer, list_item.item_type,
                                      list_item.item_price, list_item.item_service_date, list_item.item_damage_notation]
                    date_list.append(temp_date_list)
            sorted_date_list = sorted(date_list, key=sort_by_date)  # sorts the list by dates
            date_file.writerows(sorted_date_list)  # writes to file

    def write_damaged_inventory_list(self, file_name):   # used to generate a damaged item csv
        def sort_by_price(list_name):   # used to help sort the list by price
            the_price = int(list_name[3])  # needs to convert the price from a str to a int before sorting
            return the_price

        with open(file_name, 'w', newline='') as my_damage_file:
            damage_item_file = csv.writer(my_damage_file)
            damage_list = []    # used to keep track of damaged items
            for list_item in self.inventory_list:   # goes through inventory checking if damage status is true
                if list_item.item_damage_status:
                    temp_damage_list = [list_item.item_id, list_item.item_manufacturer, list_item.item_type,
                                        list_item.item_price, list_item.item_service_date]  # if true appends to list
                    damage_list.append(temp_damage_list)
            sorted_damage_list = sorted(damage_list, key=sort_by_price, reverse=True)  # sorts the list by price
            damage_item_file.writerows(sorted_damage_list)  # writes the sorted list to the csv


inventory1 = InventoryList()  # beginning of code outside of the class methods

with open('ManufacturerList.csv', 'r') as my_file:  # first file opened used to start list of inventory
    manufacturer_doc = csv.reader(my_file)

    for item in manufacturer_doc:
        item1 = InventoryItem()
        item_values = []
        for value in item:  # assigns each value to the class variable
            item_values.append(value)
        item1.item_id = item_values[0]
        item1.item_manufacturer = item_values[1]
        item1.item_type = item_values[2]
        if len(item_values[3]) >= 1:
            item1.item_damage_status = True
            item1.item_damage_notation = item_values[3]  # use the original marking for the damage indicator
        inventory1.add_item(item1)

with open('PriceList.csv', 'r') as my_file:
    price_doc = csv.reader(my_file)  # price list used to add the price of each item

    for id_num_price in price_doc:
        inventory1.update_price(id_num_price[0], id_num_price[1])

with open('ServiceDatesList.csv', 'r') as my_file:  # used to add the service dates to each item
    date_doc = csv.reader(my_file)

    for id_num_date in date_doc:
        inventory1.update_date(id_num_date[0], id_num_date[1])

# now all the items are part of the inventory list with their correct info

# block of code to call of the instance methods needed to output desired files
inventory1.write_full_inventory('FullInventory.csv')
inventory1.write_item_type_inventory()  # file name is auto generated through the instance methods
inventory1.write_needs_service_date('PastServiceDateInventory.csv')
inventory1.write_damaged_inventory_list('DamagedInventory.csv')
print('All done!')
