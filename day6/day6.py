input = open('inputDay6.txt', 'r')
lines = input.readlines()

buffer = []
index = 0
part1 = False

bufferSize = 4 if part1 else 14

def isArrayUnique(array):
    buffer = []
    for item in array:
        for otherElement in buffer:
            if item == otherElement:
                return False
        buffer.append(item)
    return True

for line in lines:
    for character in line:
        if len(buffer) != bufferSize:
            buffer.insert(0, character)
            index += 1
        else:
            if isArrayUnique(buffer):
                print(buffer) 
                if part1: 
                    # ['b', 't', 'p', 'q']
                    print("Part 1: Index of first different 4 elements: " + str(index)) #1723
                else:
                    # ['g', 'f', 'r', 'q', 'v', 'b', 'p', 'n', 'm', 'c', 'j', 't', 'h', 'w']
                    print("Part 2: Index of start of first message: " + str(index)) #3708
                break
            else:
                buffer.pop()
                buffer.insert(0, character)
                index += 1

#Source: [AdventOfCode](https://adventofcode.com/2022/day/6)
