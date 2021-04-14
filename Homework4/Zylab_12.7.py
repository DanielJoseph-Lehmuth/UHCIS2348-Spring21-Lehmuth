# Daniel Lehmuth
# 1936204

def get_age():           # function used to get age from user
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')  # raises a value error if user inputs age that is out of range
    return age


def fat_burning_heart_rate(age):          # function used to calculate heart rate
    heart_rate = (220 - age) * 0.7
    return heart_rate


if __name__ == "__main__":   # used in Zylabs to check if the function is used correctly
    try:
        user_age = get_age()                         # the try block of the code
        user_rate = fat_burning_heart_rate(user_age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(user_age, user_rate))

    except ValueError as value:       # the program executes this block if the value error occurred
        print(value)
        print('Could not calculate heart rate info.\n')
