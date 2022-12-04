total_errors = 0

with open("day4input.txt", "r") as file:
    for line in file:
        if line != "\n":
            elves = line.strip().split(",")
            elves_final = [elf.split("-") for elf in elves]
            elf1 = set(range(int(elves_final[0][0]), int(elves_final[0][1]) + 1))
            elf2 = set(range(int(elves_final[1][0]), int(elves_final[1][1]) + 1))
            elves_common = elf1.intersection(elf2)
            if len(elves_common) > 0:
                total_errors += 1

print(total_errors)
