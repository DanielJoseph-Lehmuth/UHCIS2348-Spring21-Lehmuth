# Daniel Lehmuth
# 1936204

# This function is used to sort user inputted numbers into a selection sorted list
def selection_sort_descend_trace(num_list):
    num_list = [int(s) for s in num_list]  # first converts the strings to integers
    for i in range(len(num_list) - 1):
        large_num = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] > num_list[large_num]:  # if j is bigger than large_num, j becomes the new value of large_num
                large_num = j

        temp = num_list[i]    # this block swaps num_list[i] and num_list[large_num]
        num_list[i] = num_list[large_num]
        num_list[large_num] = temp

        for num in num_list:  # this for loop prints each iteration on a line
            if num != num_list[-1]:
                print(num, end=" ")
            else:
                print(num, "")

    return num_list


if __name__ == "__main__":
    user_input = input()
    numbers = user_input.split(" ")  # takes the user input and turns it into a list
    selection_sort_descend_trace(numbers)  # this calls the function defined above
