# Daniel Lehmuth
# 1936204

import datetime

today_date = datetime.date.today()    # gets the current date

months = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5',
          'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10',
          'November': '11', 'December': '12'}

parsed_dates_list = []      # initialize empty list for parsed dates

user_file_name = input("Please enter file to open:\n")    # ask user for file name
with open(user_file_name, 'r') as date_file:             # open the user file and read lines
    lines = date_file.readlines()

for user_date in lines:
    if user_date != '-1':
        user_month_index = user_date.find(' ')         # Parsing strings according to Month DD, YYYY format
        user_month_str = user_date[0:user_month_index]     # incorrect format is ignored
        user_day_index = user_date.find(',')
        if user_day_index >= 1:
            user_day_str = user_date[(user_month_index + 1): user_day_index]
        else:
            user_day_str = " "
        user_year_index = user_date.rfind(' ')
        user_year_str = user_date[(user_year_index + 1)::]
        user_year_str = user_year_str.strip()   # strip unnecessary whitespace

# Final format check and compare input date to current date. Ignore future dates
        if (user_month_str in months) and (user_day_index >= 1) and (len(user_year_str) == 4):
            new_date = months[user_month_str] + "/" + user_day_str + "/" + user_year_str + "\n"
            test_date = datetime.date(int(user_year_str), int(months[user_month_str]), int(user_day_str))
            if test_date <= today_date:
                parsed_dates_list.append(new_date)  # add new date format to parsed date list
                print(new_date)
    else:
        break

with open('parsedDates.txt', 'w') as date_file:   # add parsed dates from list to new file
    for date in parsed_dates_list:
        date_file.write(date)
