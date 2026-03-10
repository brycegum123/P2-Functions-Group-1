# Function: choose_team
# Jordan Harris
# Description: Displays a menu of teams and allows the user to select one.
# If a team name is passed in, that team will be removed from the list so it
# cannot be selected again (used when choosing the opponent).


def choose_team(sExcludeTeam = ""):
   lTeams = ["BYU", "Utah", "UCLA", "USC", "Stanford", "Oregon", "Washington", "Arizona"]


   if sExcludeTeam in lTeams:
       lTeams.remove(sExcludeTeam)


   print("Choose a team:")
   for iIndex in range(len(lTeams)):
       print(str(iIndex + 1) + ". " + lTeams[iIndex])


   iChoice = int(input("Enter the number of your choice: "))


   while iChoice < 1 or iChoice > len(lTeams):
       print("Invalid choice. Try again.")
       iChoice = int(input("Enter the number of your choice: "))


   return lTeams[iChoice - 1]
