import math

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
    for line in file:
        if line == "\n":
            break
        stacks.append(line.strip())
    i = 1
    schema = []
    for stack in stacks:
        if i < len(stack):
            if stack[i] != " ":

