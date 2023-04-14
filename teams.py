import random

def split_players_into_teams(players):
    """Splits players into two random teams."""
    random.shuffle(players)  # Shuffle the list of players randomly
    team1 = players[:len(players)//2]  # First half of players for Team 1
    team2 = players[len(players)//2:]  # Second half of players for Team 2
    return team1, team2

# List of players
players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8"]

# Call the function to split players into teams
team1, team2 = split_players_into_teams(players)

# Display the results
print("Team 1:", team1)
print("Team 2:", team2)
