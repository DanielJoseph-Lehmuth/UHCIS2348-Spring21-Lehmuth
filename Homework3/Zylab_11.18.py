# Daniel Lehmuth
# 1936204

user_num_string = input()         # get user number list as string
num_list = user_num_string.split(" ")             # put each number as an element in a list

new_num_list = [int(num) for num in num_list]       # convert each string to an integer

new_num_list.sort()

for num in new_num_list:
    if num >= 0:                    # only print the non-negative numbers
        print(num, end=" ")
