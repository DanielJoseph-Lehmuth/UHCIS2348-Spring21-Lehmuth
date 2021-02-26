# Daniel Lehmuth
# 1936204

word = input()
new_word = word.replace(" ", "")

reverse_word = new_word[::-1]

if reverse_word == new_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
