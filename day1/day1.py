file = open("day1input.txt", "r")

arr = []
elem = 0

for line in file:
    if line != "\n":
        elem += int(line)
    else:
        arr.append(elem)
        elem = 0

arr.sort()
print(arr[len(arr) - 1])  # the highest amount of calories

print(sum(arr[-3:]))  # sum of last 3 elements
