# Daniel Lehmuth
# 1936204

import math

wall_height = int(input("Enter wall height (feet):\n"))  # user input
wall_width = int(input("Enter wall width (feet):\n"))

wall_area = wall_height * wall_width  # calculation
print("Wall area: {} square feet".format(wall_area))

Gal_paint_needed = wall_area / 350  # calculation for the amount of paint in gallons needed to cover the wall
print("Paint needed: {:.2f} gallons".format(Gal_paint_needed))

Num_PaintCans = math.ceil(Gal_paint_needed)  # Round up and convert to integer
print("Cans needed: {} can(s)".format(int(Num_PaintCans)))
print("")

paint_color_dict = {'red': 35, 'blue': 25, 'green': 23}  # the color of the paint and its cost
user_paint_color = input("Choose a color to paint the wall:\n")

cost_of_paint = paint_color_dict[user_paint_color] * Num_PaintCans

print("Cost of purchasing {} paint: ${}".format(user_paint_color, cost_of_paint))
