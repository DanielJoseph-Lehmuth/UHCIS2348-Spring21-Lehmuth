# Daniel Lehmuth
# 1936204

original_password = input()
new_password = ""           # initialize empty string for stronger password replacement

# letters to change to make password stronger
# i becomes !, a becomes @, m becomes M, B becomes 8, o becomes .

for letter in original_password:
    if letter == 'i':
        new_password += '!'
    elif letter == 'a':
        new_password += '@'
    elif letter == 'm':
        new_password += 'M'
    elif letter == 'B':
        new_password += '8'
    elif letter == 'o':
        new_password += '.'
    else:
        new_password += letter

new_password += 'q*s'       # append 'q*s' at end to increase strength

print(new_password)
