# Daniel Lehmuth
# 1936204

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1   # raises ValueError if its a string and not an integer
        if int(age) is False:
            raise ValueError()
        else:
            print('{} {}'.format(name, age))
    except ValueError:                  # if ValueError occurs then it outputs age as '0'
        print('{} 0'.format(name))

    # Get next line
    parts = input().split()
    name = parts[0]
