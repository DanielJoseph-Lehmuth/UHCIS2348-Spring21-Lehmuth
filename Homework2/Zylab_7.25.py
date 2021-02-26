# Daniel Lehmuth
# 1936204

def exact_change(user_total):
    user_dollars = 0
    user_quarters = 0
    user_dimes = 0
    user_nickels = 0
    user_pennies = 0

    if user_total <= 0:
        print("no change")

    if user_total >= 100:  # Calculate the number of dollars
        user_dollars = user_total // 100
        if user_dollars >= 2:
            print("{} dollars".format(int(user_dollars)))
        else:
            print("{} dollar".format(int(user_dollars)))
    user_total = user_total % 100

    if user_total >= 25:  # Calculate the number of quarters
        user_quarters = user_total // 25
        if user_quarters >= 2:
            print("{} quarters".format(int(user_quarters)))
        else:
            print("{} quarter".format(int(user_quarters)))
    user_total = user_total % 25

    if user_total >= 10:  # Calculate the number of dimes
        user_dimes = user_total // 10
        if user_dimes >= 2:
            print("{} dimes".format(int(user_dimes)))
        else:
            print("{} dime".format(int(user_dimes)))
    user_total = user_total % 10

    if user_total >= 5:  # Calculate the number of nickels
        user_nickels = user_total // 5
        print("{} nickel".format(int(user_nickels)))  # User will never have more than 1 nickel for exact change
    user_total = user_total % 5

    if user_total >= 1:  # Calculate the number of pennies
        user_pennies = user_total // 1
        if user_pennies >= 2:
            print("{} pennies".format(int(user_pennies)))
        else:
            print("{} penny".format(int(user_pennies)))

    return user_dollars, user_quarters, user_dimes, user_nickels, user_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
