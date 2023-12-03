#!/usr/bin/env python3

import argparse
import time

sum = 0
gearRatiosSum = 0
numLines = 0
mapOfFoundNumbers = {}
# lineIndex-charIndex: number

def getEntireNumber(line, charIndex, lineIndex):
    leftIndex = charIndex
    rightIndex = charIndex
    # search left
    for i in range(charIndex - 1, -1, -1):
        if not line[i].isdigit():
            leftIndex = i + 1
            break
        elif i == 0:
            leftIndex = 0
            break
            
    # search right
    for i in range(charIndex + 1, len(line)):
        if not line[i].isdigit():
            rightIndex = i - 1
            break
        elif i == len(line) - 1:
            rightIndex = len(line) - 1
            break
    key = str(lineIndex) + '-' + str(leftIndex)
    entireNumber = int(line[leftIndex:rightIndex + 1])
    if key in mapOfFoundNumbers.keys():
        if mapOfFoundNumbers[key] != entireNumber:
            print('key: ' + key)
            print('newNumber: ' + str(entireNumber))
            print('existingNumber: ' + str(mapOfFoundNumbers[key]))
            raise Exception('Found a different number at the same index')
        return (entireNumber, False)
    else:
        mapOfFoundNumbers[key] = entireNumber
        return (entireNumber, True)

def checkSurroundingCharacters(lines, lineIndex, charIndex):
    # check all the surrounding characters to determine if one of them is a number
    # if so, and if it hasnt been added previously, add it to the sum
    # if not, do nothing
    global sum
    global numLines
    entireNumberData = (0, False)
    # 0 1 2
    # 3 x 4 
    # 5 6 7
    adjacentNumbers = {'topLeft': 0, 'top': 0, 'topRight': 0, 'left': 0, 'right': 0, 'bottomLeft': 0, 'bottom': 0, 'bottomRight': 0}
    adjacentNumbersFound = 0

    # check left
    if charIndex > 0:
        if lines[lineIndex][charIndex - 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex], charIndex - 1, lineIndex)
            if entireNumberData[1]:
                adjacentNumbers['left'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check top left
    if charIndex > 0 and lineIndex > 0:
        if lines[lineIndex - 1][charIndex - 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex - 1], charIndex - 1, lineIndex - 1)
            if entireNumberData[1]:
                adjacentNumbers['topLeft'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check right
    if charIndex < len(lines[lineIndex]) - 1:
        if lines[lineIndex][charIndex + 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex], charIndex + 1, lineIndex)
            if entireNumberData[1]:
                adjacentNumbers['right'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check top right
    if charIndex < len(lines[lineIndex]) - 1 and lineIndex > 0:
        if lines[lineIndex - 1][charIndex + 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex - 1], charIndex + 1, lineIndex - 1)
            if entireNumberData[1]:
                adjacentNumbers['topRight'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check top
    if lineIndex > 0:
        if lines[lineIndex - 1][charIndex].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex - 1], charIndex, lineIndex - 1)
            if entireNumberData[1]:
                adjacentNumbers['top'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check bottom
    if lineIndex < numLines - 1:
        if lines[lineIndex + 1][charIndex].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex + 1], charIndex, lineIndex + 1)
            if entireNumberData[1]:
                adjacentNumbers['bottom'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check bottom left
    if charIndex > 0 and lineIndex < numLines - 1:
        if lines[lineIndex + 1][charIndex - 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex + 1], charIndex - 1, lineIndex + 1)
            if entireNumberData[1]:
                adjacentNumbers['bottomLeft'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    # check bottom right
    if charIndex < len(lines[lineIndex]) - 1 and lineIndex < numLines - 1:
        if lines[lineIndex + 1][charIndex + 1].isdigit():
            entireNumberData = getEntireNumber(lines[lineIndex + 1], charIndex + 1, lineIndex + 1)
            if entireNumberData[1]:
                adjacentNumbers['bottomRight'] = entireNumberData[0]
                sum += entireNumberData[0]
                adjacentNumbersFound += 1
    
    return (adjacentNumbersFound, adjacentNumbers)

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global numLines
    numLines = len(lines)

    for index, line in enumerate(lines):
        line = line.replace('\n', '')
        for charIndex, char in enumerate(line):
            if char != '.' and not char.isalnum():
                checkSurroundingCharacters(lines, index, charIndex)
    
    print('PART 1: Sum of all the part numbers: ' + str(sum))
    # PART 1 Answer: 560670

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global gearRatiosSum
    global mapOfFoundNumbers
    mapOfFoundNumbers = {}

    for index, line in enumerate(lines):
        line = line.replace('\n', '')
        for charIndex, char in enumerate(line):
            if char == '*':
                numsFound = checkSurroundingCharacters(lines, index, charIndex)
                if numsFound[0] == 2:
                    firstSurroundingNumber = 0
                    secondSurroundingNumber = 0
                    for surroundingNumbers in numsFound[1].values():
                        if surroundingNumbers != 0:
                            if firstSurroundingNumber == 0:
                                firstSurroundingNumber = surroundingNumbers
                            else:
                                secondSurroundingNumber = surroundingNumbers
                    gearRatiosSum += (firstSurroundingNumber * secondSurroundingNumber)
    print('PART 2: Sum of all the gear ratios: ' + str(gearRatiosSum))
    # PART 2 Answer: 91622824

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 3')
    parser.add_argument('input_file', metavar='filename', type=str, default='inputFile.txt', help='Path to input.')
    args = parser.parse_args()

    start_time = time.time()
    part1(args.input_file)
    print('Part 1 execution time: {:.3f} seconds'.format(time.time() - start_time))

    start_time = time.time()
    part2(args.input_file)
    print('Part 2 execution time: {:.3f} seconds'.format(time.time() - start_time))

if __name__ == '__main__':
    main()

#Source: [AdventOfCode](https://adventofcode.com/2023/day/3)