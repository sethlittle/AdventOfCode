from enum import Enum
import numpy as np

input = open('inputDay9.txt', 'r')
lines = input.readlines()

part1 = False

class Direction(Enum):
    L = "left"
    R = "right"
    D = "down"
    U = "up"

def checkIfNextToEachOther(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <=1:
        return (0,0)
    elif head[0] == tail[0] and head[1] == tail[1] - 2: # head is two below tail
        return (0,-1) 
    elif head[0] == tail[0] + 1 and head[1] == tail[1] - 2: # head is two below and one to the right of tail
        return (1,-1)
    elif head[0] == tail[0] - 1 and head[1] == tail[1] - 2: # head is two below and one to the left of tail
        return (-1,-1)
    elif head[0] == tail[0] - 2 and head[1] == tail[1]: # head is two to the left of tail
        return (-1,0)
    elif head[0] == tail[0] - 2 and head[1] == tail[1] - 1:
        return (-1,-1)
    elif head[0] == tail[0] - 2 and head[1] == tail[1] + 1:
        return (-1,1)
    elif head[0] == tail[0] and head[1] == tail[1] + 2: #head is two above tail
        return (0,1)
    elif head[0] == tail[0] - 1 and head[1] == tail[1] + 2: 
        return (-1,1)
    elif head[0] == tail[0] + 1 and head[1] == tail[1] + 2:
        return (1,1)
    elif head[0] == tail[0] + 2 and head[1] == tail[1]: #head is two to the right of tail
        return (1,0)
    elif head[0] == tail[0] + 2 and head[1] == tail[1] + 1:
        return (1,1)
    elif head[0] == tail[0] + 2 and head[1] == tail[1] - 1:
        return (1,-1)
    elif head[0] == tail[0] + 2 and head[1] == tail[1] + 2:
        return (1,1)
    elif head[0] == tail[0] - 2 and head[1] == tail[1] + 2:
        return (-1,1)
    elif head[0] == tail[0] + 2 and head[1] == tail[1] - 2:
        return (1,-1)
    elif head[0] == tail[0] - 2 and head[1] == tail[1] - 2:
        return (-1,-1)

mapDict = {}

# head 0 and tail is len - 1
knots = []
def getKnots(count):
    for i in range(0, count):
        knots.append((0,0))

if part1:
    getKnots(2)
else:
    getKnots(10)

mapDict[knots[len(knots) - 1]] = 1
countVisited = 1

for line in lines:
    input = line.strip().split(" ")
    for i in range(0, int(input[1])):
        if Direction[input[0]].value == "left":
            knots[0] = (knots[0][0] - 1, knots[0][1])
        elif Direction[input[0]].value == "right":
            knots[0] = (knots[0][0] + 1, knots[0][1])
        elif Direction[input[0]].value == "down":
            knots[0] = (knots[0][0], knots[0][1] - 1)
        elif Direction[input[0]].value == "up":
            knots[0] = (knots[0][0], knots[0][1] + 1)
        for j in range(1, len(knots)):
            moveKnot = checkIfNextToEachOther(knots[j-1], knots[j])
            if moveKnot != (0,0):
                knots[j] = (knots[j][0] + moveKnot[0], knots[j][1] + moveKnot[1])

            if j == len(knots) -1:
                if knots[j] not in mapDict:
                    countVisited += 1
                    mapDict[knots[j]] = 1

if part1:
    print("Part One Answer:", countVisited) #6212
else:
    print("Part Two Answer:", countVisited) #2522
