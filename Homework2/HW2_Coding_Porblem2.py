# Daniel Lehmuth
# 1936204

import datetime

today_date = datetime.date.today()    # gets the current date

months = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5',
          'June': '6', 'July': '7', 'August': '8', 'September': '9', 'October': '10',
          'November': '11', 'December': '12'}

print("Correct format for the date is: Month DD, YYYY")   # instructions for user
user_date = input("Please enter date. Input -1 to exit:\n")

while user_date != '-1':
    user_month_index = user_date.find(' ')         # Parsing strings according to Month DD, YYYY format
    user_month_str = user_date[0:user_month_index]     # incorrect format is ignored
    user_day_index = user_date.find(',')
    if user_day_index >= 1:
        user_day_str = user_date[(user_month_index + 1): user_day_index]
    else:
        user_day_str = ""
    user_year_index = user_date.rfind(' ')
    user_year_str = user_date[(user_year_index + 1)::]

    if (user_month_str in months) and (user_day_index >= 1) and (len(user_year_str) == 4):
        new_date = months[user_month_str] + "/" + user_day_str + "/" + user_year_str
        test_date = datetime.date(int(user_year_str), int(months[user_month_str]), int(user_day_str))
        if test_date <= today_date:
            print(new_date)               # compare input date to current date and ignore future dates

    user_date = input("Please enter date. Input -1 to exit:\n")
