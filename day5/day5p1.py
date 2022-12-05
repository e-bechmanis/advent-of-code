with open("day5input.txt", "r") as file:
    stacks = []
    instructions = []

    for line in file:
        if line == "\n":
            break
        stacks.append(line.strip())

    # Making sure the schema outlined in input file is transformed into stacks
    schema = [[] for i in range((len(stacks[0]) // 4) + 1)]
    for stack in stacks:
        i = 1
        j = 0
        while i < len(stack):
            if stack[i] != " ":
                schema[j].append(stack[i])
            i += 4
            j += 1

    for each in schema:
        each.reverse()

    # Keep reading file to save instructions into array
    for line in file:
        temp = line.strip().replace("move ", "").split(" from ")
        temp2 = [str.split(" to ") for str in temp]
        instructions.append(temp2[0] + temp2[1])

    # Making moves
    for instruction in instructions:
        for i in range(int(instruction[0])):
            arrlen = len(schema[int(instruction[1]) - 1])
            temp = schema[int(instruction[1]) - 1][arrlen - 1]
            schema[int(instruction[1]) - 1].pop()
            schema[int(instruction[2]) - 1].append(temp)

    for queue in schema:
        print(queue[len(queue) - 1], end="")
