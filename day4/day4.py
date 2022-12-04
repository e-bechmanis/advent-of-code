with open("day4input.txt", "r") as file:
    for line in file:
        if line != "\n":
            elfs = line.split(",")
            elf1 = set(range(int(elfs[0][0]), int(elfs[0][2]) + 1))
            elf2 = set(range(int(elfs[1][0]), int(elfs[1][2]) + 1))
            common_element = comp1.intersection(comp2)
            for elem in common_element:  # O(1) because loop will only run 1 time
                if ord(elem) > 96:  # if it's a lowercase letter
                    priority_total += ord(elem) - ord("a") + 1
                else:  # uppercase letter
                    priority_total += ord(elem) - ord("A") + 27
                break

print(priority_total)
