# Daniel Lehmuth
# 1936204

current_month = int(input("Please enter the current month in number form:\n"))  # current date
current_day = int(input("Please enter the current day of the month:\n"))
current_year = int(input("Please enter the current year:\n"))

birth_month = int(input("Please enter your birth month in number form:\n"))  # birth date
birth_day = int(input("Please enter the day of the month you were born:\n"))
birth_year = int(input("Please enter the year you were born:\n"))
years_old = 0

print("")
print("Birthday calculator!")    # print user input data
print("")
print("Current day")
print("Month:", current_month)
print("Day:", current_day)
print("Year:", current_year)
print("")
print("Birthday")
print("Month:", birth_month)
print("Day:", birth_day)
print("Year:", birth_year)
print("")

if current_year < birth_year:    # error checking
    print("Invalid entry: Birth year hasn't happened yet.")
if current_year == birth_year and current_month < birth_month:
    print("Invalid entry: Birth month hasn't happened yet.")
if current_year == birth_year and current_month == birth_month and current_day < birth_day:
    print("Invalid entry: Birth day hasn't happened yet. So close!")
if current_day > 31 or current_day < 1 or birth_day > 31 or birth_day < 1:
    print("Invalid entry: Day is out of range for the month.")
if current_month > 12 or current_month < 1 or birth_month > 12 or birth_month < 1:
    print("Invalid entry: Month is out of range.")
if current_year < 1 or birth_year < 1:
    print("Invalid entry: The year did not exist.")

if current_year > birth_year and current_month >= birth_month and current_day > birth_day:   # age calculations
    years_old = current_year - birth_year
    print("You are {} years old.".format(years_old))
if current_year > birth_year and current_month < birth_month:
    years_old = current_year - birth_year - 1
    print("You are {} years old.".format(years_old))
if current_year >= birth_year and current_month == birth_month and current_day == birth_day:
    years_old = current_year - birth_year
    print("You are {} years old.".format(years_old))
    print("Happy birthday!")
