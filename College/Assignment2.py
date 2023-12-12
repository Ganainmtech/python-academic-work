# Setting variables at the beginning of the program
validInt = False
anotherGame = 'y'
teamsPlayed = 1
userTeamPointsTotal = 0
userHighestGoals = 0

# Getting the user's team name
userTeam = input("Enter your team name: ")

# Until 3 different teams are played keep looping
for teamsPlayed in range(3):

    # Resetting the total number of user goals per game
    userGoalsTotal = 0
    # Resetting points for the new games
    userTeamPoints = 0
    # Resetting the count of how many games are played
    gamesPlayed = 0
    # Finding out the other team code
    otherTeam = input("Enter the other team code: ")

    # Finding out the game information while games are played
    while anotherGame == 'y':
        validInt = False
        while not validInt:
            try:
                # Getting the user team goals
                userGoals = int(input("Goals scored by " + userTeam + " in match: "))

            except ValueError:
                print("\nError - please enter the goals scored by the user team.")
            else:
                validInt = True

        # Getting the other teams goals
        otherTeamGoals = int(input("Goals scored by " + otherTeam + " in match: "))

        # Calculating amount of points given to user team against first the team
        if userGoals > otherTeamGoals:
            userTeamPoints += 3
        elif userGoals == otherTeamGoals:
            userTeamPoints += 1

        # Calculating the highest goal scored from all games
        if userGoals > userHighestGoals:
            userHighestGoals = userGoals

        # Calculating total goals per game
        userGoalsTotal += userGoals

        # Counting number of games played against a team
        gamesPlayed += 1

        # Prompting the user if there was another game played
        anotherGame = input("\nWas there another game? (y/n): ")

    # While there are no games being played do this
    while anotherGame == 'n':
        # Display output of last game
        print(f"\n{'Opposition team code:':<80}{otherTeam:>10}"
              f"\n{'Games Played:':<80}{gamesPlayed:>10}"
              f"\n{'Goals for:':<80}{userGoalsTotal:>10}"
              f"\n{'Points:':<80}{userTeamPoints:>10}\n")

        # Total points from all the games played against the teams
        userTeamPointsTotal += userTeamPoints

        # Counting number of teams played against the user's team
        teamsPlayed += 1

        # Automatically setting up the next team to be played
        anotherGame = 'y'

# Display final user game data
print(f"\n{'Users team name:':<80}{userTeam:>10}"
      f"\n{'Points:':<80}{userTeamPointsTotal:>10}"
      f"\n{'Highest number of goals scored by users team in a single match:':<80}{userHighestGoals:>10}")