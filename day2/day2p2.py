# X - loose (0 points)
# Y - draw  (3 points)
# Z - win   (6 points)

with open("day2input.txt", "r") as games:
    gamesList = games.read().splitlines()

total_score = 0

for game in gamesList:
    if game[2] == "X":  # If I need to loose
        if game[0] == "A":  # If 1st player chose rock
            total_score += 3  # I choose scissors
        elif game[0] == "B":  # 1st player - paper
            total_score += 1  # I choose rock
        elif game[0] == "C":  # 1st player - scissors
            total_score += 2  # I choose paper
    elif game[2] == "Y":  # If I go for a draw
        total_score += 3
        if game[0] == "A":
            total_score += 1
        elif game[0] == "B":
            total_score += 2
        elif game[0] == "C":
            total_score += 3
    else:  # I need to win
        total_score += 6
        if game[0] == "A":  # If 1st player chose rock
            total_score += 2  # I choose paper
        elif game[0] == "B":  # 1st player - paper
            total_score += 3  # I choose scissors
        elif game[0] == "C":  # 1st player - scissors
            total_score += 1  # I choose rock
print(total_score)
