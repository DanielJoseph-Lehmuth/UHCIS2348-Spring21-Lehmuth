# Daniel Lehmuth
# 1936204

# Global variable
num_calls = 0


def partition(user_ids_part, i, k):
    #  Pick middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids_part[midpoint]

    #  Initialize variables needed
    done = False
    low = i
    high = k
    while not done:
        #  Increment low while user_ids_part[low] < pivot
        while user_ids_part[low] < pivot:
            low = low + 1
        #  Decrement high while pivot < user_ids_part[high]
        while pivot < user_ids_part[high]:
            high = high - 1
        # if there are one or less items then all elements are partitioned
        if low >= high:
            done = True
        else:
            # this block swaps the low index and the high index and updates variables high and low
            temp = user_ids_part[low]
            user_ids_part[low] = user_ids_part[high]
            user_ids_part[high] = temp
            low = low + 1
            high = high - 1
    return high


def quicksort(user_ids_qs, i, k):
    global num_calls
    num_calls += 1
    if i >= k:
        return
# The data is partitioned using j as the element used to separate the list
    j = partition(user_ids_qs, i, k)

    quicksort(user_ids_qs, i, j)  # this sorts the lower partition
    quicksort(user_ids_qs, j + 1, k)  # this sorts the higher partition
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)  # initial call for quicksort

    print(num_calls)  # prints the number of calls to quicksort

    for user_id in user_ids:    # prints the sorted user ids
        print(user_id)
