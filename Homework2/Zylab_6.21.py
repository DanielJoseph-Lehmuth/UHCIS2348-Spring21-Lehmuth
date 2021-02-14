# Daniel Lehmuth
# 1936204

a = int(input())    # First equation, ax + by = c
b = int(input())
c = int(input())

d = int(input())    # Second equation, dx + ey = f
e = int(input())
f = int(input())

solved = False      # Initialize if the equation is solved. It is not at this point.

for x in range(-10, 11):       # brute force equation
    for y in range(-10, 11):
        new_c = (a * x) + (b * y)
        new_f = (d * x) + (e * y)
        if new_c == c and new_f == f:
            solved = True                      # print x and y value and solved is true
            print(x, y)

if solved is False:                            # if solved is false
    print("No solution")
