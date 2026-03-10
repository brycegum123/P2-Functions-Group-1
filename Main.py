# Import functions from Soccer.py
from Soccer import introduction, display_menu, display_record, choose_team

def main():

    # Call introduction function (Bryce)
    sPlayerName = introduction()

    # Call menu function (Bryce)
    sChoice = display_menu()

    iWins= 0
    iLosses= 0
    sHomeTeam= ""
    # Basic menu logic
    if sChoice == "1":
        print("Starting the season...")
        print()
        sHomeTeam =choose_team()
        sAwayTeam = choose_team(sHomeTeam)  
        print("Home Team:", sHomeTeam)
        print("Opponent:", sAwayTeam)
    elif sChoice == "2":
        print("Displaying record:", display_record(sHomeTeam, iWins, iLosses))

    elif sChoice == "3":
        print("Goodbye " + sPlayerName)


# Run the program
main()
