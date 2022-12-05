# This class represents a queue. I will be pushing items to the back of the queue and popping them from the front
class Queue:
    def __init__(self, capacity=10):
        self.the_queue = [None] * capacity
        self.start = 0
        self.back = 0
        self.slots_used = 0
        self.cap = capacity

    def grow(self):
        newcap = self.cap * 2
        newqueue = [None] * newcap
        i = self.start
        j = 0
        while j < self.slots_used:
            newqueue[j] = self.the_queue[i]
            i = (i + 1) % self.cap
            j += 1
        self.start = 0
        self.back = self.slots_used
        self.cap = newcap
        self.the_queue = newqueue

    def enqueue(self, v):
        if self.slots_used == self.cap:
            self.grow()
        self.the_queue[self.back] = v
        self.back = (self.back + 1) % self.cap
        self.slots_used += 1

    def dequeue(self):
        if self.slots_used != 0:
            self.start = (self.start + 1) % self.cap
            self.slots_used -= 1

    def front(self):
        if self.slots_used > 0:
            return self.the_queue[self.start]
        return None


with open("day5input.txt", "r") as file:
    stacks = []
    instructions = []

    for line in file:
        if line == "\n":
            break
        stacks.append(line.strip())

    # Making sure the schema outlined in input file is transformed into queues
    schema = [Queue() for i in range((len(stacks[0]) // 4) + 1)]
    for stack in stacks:
        i = 1
        j = 0
        while i < len(stack):
            if stack[i] != " ":
                schema[j].enqueue(stack[i])
            i += 4
            j += 1

    # Reading instructions into array
    for line in file:
        temp = line.strip().replace("move ", "").split(" from ")
        temp2 = [str.split(" to ") for str in temp]
        instructions.append(temp2[0] + temp2[1])

    # Making moves
    for instruction in instructions:
