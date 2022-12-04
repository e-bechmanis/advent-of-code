total_errors = 0

with open("day4input.txt", "r") as file:
    for line in file:
        if line != "\n":
            elfs = line.strip().split(",")
            elfs_final = [elf.split("-") for elf in elfs]
            elf1 = set(range(int(elfs_final[0][0]), int(elfs_final[0][1]) + 1))
            elf2 = set(range(int(elfs_final[1][0]), int(elfs_final[1][1]) + 1))
            elf1_common = elf1.intersection(elf2)
            elf2_common = elf2.intersection(elf1)
            if len(elf1_common) == len(elf2) or len(elf2_common) == len(elf1):
                total_errors += 1

print(total_errors)
