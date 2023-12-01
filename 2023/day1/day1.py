from enum import Enum

# helper functions
def getFileName(part):
    if activePart == Part.test1:
        return 'testInput.txt'
    elif activePart == Part.test2:
        return 'testInput2.txt'
    else:
        return 'inputFile.txt'

class Part(Enum):
    test1=0
    test2=1
    part1=2
    part2=3
    bothParts=4

# CHANGE THIS IF NEEDED
activePart = Part.test2

# SOLUTION
input = open(getFileName(activePart), 'r')
lines = input.readlines()

# PART 1
print(activePart)
if activePart != Part.part2:
    sum = 0
    digits = []
    for line in lines:
        for char in line:
            if char.isdigit():
                digits.append(char)
        if len(digits) > 0:
            value = digits[0] + digits[-1]
            sum = sum + int(value)
            digits.clear()
    print("PART 1: Sum of all of the calibration values: " + str(sum))
    # PART 1 Answer: 55712

# I had to look on the reddit page, it seems a crucial detail not covered in the test cases is eighthree should be 83 not 8hree
# PART 2
stringNumbers = {'one': (3, '1'), 
                 'two': (3, '2'), 
                 'three': (5, '3'), 
                 'four': (4, '4'), 
                 'five': (4, '5'), 
                 'six': (3, '6'), 
                 'seven': (5, '7'), 
                 'eight': (5, '8'), 
                 'nine': (4, '9')}

if activePart != Part.part1:
    sum = 0
    digits = []
    newLine = ''
    wordsFound = 0
    for line in lines:
        line = line.replace('\n', '')
        newLine = line
        length = len(line)
        index = 0
        while index < length:
            for key, value in stringNumbers.items():
                if line[index:index+value[0]] == key:
                    indexOfNumber = newLine.find(key)
                    wordsFound += 1 # This offsets the addition of the number so it always gets placed within the word ...1two5... -> ...1t2wo5...
                    newLine = newLine[:index+wordsFound] + value[1] + newLine[index+wordsFound:]
            index+=1

        for char in newLine:
            if char.isdigit():
                digits.append(char)
        firstAndLast = digits[0] + digits[-1]
        wordsFound = 0
        sum = sum + int(firstAndLast)
        digits.clear()

    print("PART 2: Sum of all of the calibration values: " + str(sum))
    # PART 2 Answer: 55413

#Source: [AdventOfCode](https://adventofcode.com/2023/day/1)
