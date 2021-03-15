# Daniel Lehmuth
# 1936204

class Team:                    # Class initialized
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):                    # added get_win_percentage method
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == "__main__":       # needed for zylab test
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:                       # determine if team has winning average or not
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
