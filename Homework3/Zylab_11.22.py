# Daniel Lehmuth
# 1936204

user_input = input()              # get user input
word_list = user_input.split(" ")    # convert user input into list

for word in word_list:                # iterate through list and count the occurrences of each word
    print(word, word_list.count(word))
