with open("day4input.txt", "r") as file:
    for line in file:
        if line != "\n":
            elfs = line.split(",")
            elf1 = [i for i in range(int(line[0]):int(line[2]) + 1)]
            comp1 = set(line[: len(line) // 2])  # O(n) complexity
            comp2 = set(line[len(line) // 2 :])  # O(n) complexity
            common_element = comp1.intersection(comp2)
            for elem in common_element:  # O(1) because loop will only run 1 time
                if ord(elem) > 96:  # if it's a lowercase letter
                    priority_total += ord(elem) - ord("a") + 1
                else:  # uppercase letter
                    priority_total += ord(elem) - ord("A") + 27
                break

print(priority_total)
