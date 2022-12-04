# Scores for choosing a shape 1 for Rock (A or X), 2 for Paper (B or Y), and 3 for Scissors (C or Z)
# Scores for outcome: 0 for loss, 3 for draw, 6 for win

# ROCK      A   X
# PAPER     B   Y
# SCISSORS  C   Z

with open("day2input.txt", "r") as games:
    gamesList = games.read().splitlines()

total_score = 0

for game in gamesList:
    if game[2] == "X":  # If I choose rock
        total_score += 1
        if game[0] == "A":
            total_score += 3
        elif game[0] == "C":
            total_score += 6
    elif game[2] == "Y":  # If I chose paper
        total_score += 2
        if game[0] == "A":
            total_score += 6
        elif game[0] == "B":
            total_score += 3
    else:  # If I chose scissors
        total_score += 3
        if game[0] == "B":
            total_score += 6
        elif game[0] == "C":
            total_score += 3
print(total_score)
