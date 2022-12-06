with open("day6input.txt", "r") as file:
    i = 0
    arr = []
    while True:  # while there are characters to read
        char = file.read(1)  # read 1 character
        i += 1
        arr.append(char)
        if i > 4:
            unique_set = set(arr[-4:])
            if len(arr[-4:]) == len(unique_set):
                print(unique_set)
                print(i)
                break
