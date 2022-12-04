priority_total = 0

with open("day3input.txt", "r") as file:
    rucksacks = file.read().splitlines()
    threshold = 2
    teams, team = [], []

    # dividing all rucksacks into teams of 3
    for i in range(len(rucksacks)):
        team.append(set(rucksacks[i]))
        if i == threshold:
            threshold += 3
            teams.append(team)
            team = []

    # calculating priorities
    for team in teams:
        common_elem = team[0].intersection(team[1])
        final_common = common_elem.intersection(team[2])
        for elem in final_common:
            if ord(elem) > 96:  # if it's a lowercase letter
                priority_total += ord(elem) - ord("a") + 1
            else:  # uppercase letter
                priority_total += ord(elem) - ord("A") + 27
            break

print(priority_total)
