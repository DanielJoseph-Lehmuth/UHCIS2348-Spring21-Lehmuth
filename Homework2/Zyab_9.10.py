# Daniel Lehmuth
# 1936204

import csv

user_file = input()         # user input needed for file name

with open(user_file, 'r') as my_file:    # opens and reads file. delimiter is assumed to be a ','
    word_list = csv.reader(my_file)

    output_list = []    # empty list needed to ensure there are no repeat words

    for row in word_list:           # goes through the list of words
        for word in row:
            if word not in output_list:
                output_list.append(word)         # appends word to new list if it is not already in there
                tally = row.count(word)          # counts the amount of times a word appears in the original list
                print(word, tally)
