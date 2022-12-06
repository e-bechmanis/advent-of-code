with open("day6input.txt", "r") as file:
    i = 0
    arr = []
    while True:  # while there are characters to read
        char = file.read(1)  # read 1 character
        i += 1
        arr.append(char)
        if i > 14:
            unique_set = set(arr[-14:])
            if len(arr[-14:]) == len(unique_set):
                print(unique_set)
                print(i)
                break
