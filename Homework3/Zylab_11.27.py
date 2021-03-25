# Daniel Lehmuth
# 1936204

player_count = 1                  # initialize needed list and dictionary for the roster
team_roster_dict = {}
jersey_num_list = []

while player_count <= 5:                # while loop to add the first five players
    player_num = int(input("Enter player {}'s jersey number:\n".format(player_count)))
    player_rate = int(input("Enter player {}'s rating:\n".format(player_count)))
    print()
    team_roster_dict[player_num] = player_rate
    jersey_num_list.append(player_num)
    player_count += 1

jersey_num_list.sort()

print("ROSTER")
for jersey_num in jersey_num_list:                 # for loop to print the player in ascending order by jersey number
    print("Jersey number: {}, Rating: {}".format(jersey_num, team_roster_dict[jersey_num]))
print()

user_option = ""

while user_option != 'q':       # implement user options. 'q' is to quit
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    user_option = input("Choose an option:\n")

    if user_option == 'o':         # output team roster option
        jersey_num_list.sort()
        print("ROSTER")
        for jersey_num in jersey_num_list:
            print("Jersey number: {}, Rating: {}".format(jersey_num, team_roster_dict[jersey_num]))
        print()

    if user_option == 'a':          # add new player to roster option
        player_num = int(input("Enter a new player's jersey number:\n"))
        player_rate = int(input("Enter the player's rating:\n"))
        print()
        team_roster_dict[player_num] = player_rate
        jersey_num_list.append(player_num)

    if user_option == 'd':          # remove player from roster option
        num_to_delete = int(input("Enter a jersey number:\n"))
        del team_roster_dict[num_to_delete]
        jersey_num_list.remove(num_to_delete)

    if user_option == 'u':                      # update player rating option
        update_jersey_num = int(input("Enter a jersey number:\n"))
        update_player_rate = int(input("Enter a new rating:\n"))
        if update_jersey_num in jersey_num_list:
            team_roster_dict[update_jersey_num] = update_player_rate

    if user_option == 'r':   # output player ratings that are above user input
        rate_above = int(input("Enter a rating:\n"))
        print()
        print("ABOVE", rate_above)
        for jersey_num in jersey_num_list:
            if team_roster_dict[jersey_num] > rate_above:
                print("Jersey number: {}, Rating: {}".format(jersey_num, team_roster_dict[jersey_num]))
        print()
