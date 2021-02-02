# Daniel Lehmuth
# 1936204

# user input for recipe
lemon_juiceAmt = int(input("Enter amount of lemon juice (in cups):\n"))

waterAmt = int(input("Enter amount of water (in cups):\n"))

agave_nectarAmt = float(input("Enter amount of agave nectar (in cups):\n"))

servingNum = int(input("How many servings does this make?\n"))

print("")  # spacing used between prompts and output

print("Lemonade ingredients - yields {:.2f} servings".format(servingNum))
print("{:.2f} cup(s) lemon juice".format(lemon_juiceAmt))
print("{:.2f} cup(s) water".format(waterAmt))
print("{:.2f} cup(s) agave nectar".format(agave_nectarAmt))

print("")
servingsWanted = int(input("How many servings would you like to make?\n"))
print("")

# Calculations for amount of lemonade wanted
totalservings = servingsWanted / servingNum
lemon_juiceWanted = totalservings * lemon_juiceAmt
waterWanted = totalservings * waterAmt
agave_nectarWanted = totalservings * agave_nectarAmt

# print desired amount
print("Lemonade ingredients - yields {:.2f} servings".format(servingsWanted))
print("{:.2f} cup(s) lemon juice".format(lemon_juiceWanted))
print("{:.2f} cup(s) water".format(waterWanted))
print("{:.2f} cup(s) agave nectar".format(agave_nectarWanted))

# convert to gallons
lemon_juiceGal = lemon_juiceWanted / 16
waterGal = waterWanted / 16
agave_nectarGal = agave_nectarWanted / 16

# print conversion with space
print("")
print("Lemonade ingredients - yields {:.2f} servings".format(servingsWanted))
print("{:.2f} gallon(s) lemon juice".format(lemon_juiceGal))
print("{:.2f} gallon(s) water".format(waterGal))
print("{:.2f} gallon(s) agave nectar".format(agave_nectarGal))
