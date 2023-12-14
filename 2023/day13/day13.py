#!/usr/bin/env python3

import argparse
import time
from enum import Enum

# fields
reflections = []
puzzleSolutions = {}  #key is the puzzle number and value is a tuple of the reflection direction and line number

class Direction(Enum):
    vertical=1
    horizontal=100

# helper functions
def findMissingCharacter(str1, str2):
    if len(str1) != len(str2):
        return False, -1

    differences = [(i, a, b) for i, (a, b) in enumerate(zip(str1, str2)) if a != b]
    # better and cleaner than this:
    #   for i, (a, b) in enumerate(zip(str1, str2)):
    #       if a != b:
    #           differences.append((i, a, b))

    if len(differences) == 1:
        return True, differences[0][0]
    else:
        return False, -1

def checkContainsAConsecutiveValue(array):
    return any(array[i] + 1 == array[i + 1] for i in range(len(array) - 1))

def lookForAndFixSmudges(direction, maskSmudges=0):
    global reflections
    newReflections = []
    if direction == Direction.vertical:
        lines = list(zip(*reflections))
    else:
        lines = reflections
    smudgesFound = 0

    for indexMain, line in enumerate(lines):
        for indexOthers, otherLine in enumerate(lines):
            if indexMain == indexOthers:
                continue
            isMissing, missingIndex = findMissingCharacter(line, otherLine)
            if isMissing:
                # print('Found missing character at index', missingIndex, 'in line', indexMain, line, 'and line', indexOthers)
                if line[missingIndex] == '.':
                    line = list(line)
                    newline = line[:missingIndex] + ['#'] + line[missingIndex + 1:]
                else:
                    line = list(line)
                    newline = line[:missingIndex] + ['.'] + line[missingIndex + 1:]
                lines[indexMain] = newline
                if direction == Direction.vertical:
                    newReflections = list(zip(*lines))
                else:
                    newReflections = lines
                return True, newReflections
    return False, reflections
    
def evaluateDirection(direction, reflections, puzzleNumber):
    global puzzleSolutions
    if direction == Direction.vertical:
        lines = list(zip(*reflections))
    else:
        lines = reflections

    for index, line in enumerate(lines):
        lines[index] = list(line)

    linePairs = []
    for line in lines:
        copies = [i for i, e in enumerate(lines) if e == line]
        linePairs.append(copies)
        
    res = []
    for x in linePairs:
        if x not in res:
            res.append(x)
    linePairs = res
    
    linePairs = list(filter(lambda x: len(x) > 1, linePairs))
    if len(linePairs) == 0:
        return 0
    linePairs = list(filter(lambda x: checkContainsAConsecutiveValue(x), linePairs))
    if len(linePairs) == 0:
        return 0
    
    # need to check if the given puzzle number already has the reflection point at that location
    for pair in linePairs:
        for index, value in enumerate(pair):
            if index == len(pair) - 1:
                # it will never be the very last value
                continue
            first = value
            second = value + 1
            while first >= 0 and second <= len(lines):
                if first == 0 or second == len(lines):
                    if second < len(lines) and lines[first] == lines[second]:
                        if puzzleNumber not in puzzleSolutions.keys():
                            puzzleSolutions[puzzleNumber] = (direction, (value + 1)) # plus one because we are counting from 0
                            return (value + 1) * direction.value # plus one because we are counting from 0
                        else:
                            if puzzleSolutions[puzzleNumber][0] != direction or puzzleSolutions[puzzleNumber][1] != (value + 1):
                                return (value + 1) * direction.value
                            break
                    elif second < len(lines) and lines[first] != lines[second]:
                        break
                    else:
                        if puzzleNumber not in puzzleSolutions.keys():
                            puzzleSolutions[puzzleNumber] = (direction, (value + 1)) # plus one because we are counting from 0
                            return (value + 1) * direction.value # plus one because we are counting from 0
                        else:
                            if puzzleSolutions[puzzleNumber][0] != direction or puzzleSolutions[puzzleNumber][1] != (value + 1):
                                return (value + 1) * direction.value
                            break
                if lines[first] != lines[second]:
                    break
                first -= 1
                second += 1

    return 0

def evaluateDiagram(puzzleNumber):
    global reflections
    sumToReturn = 0
    sumToReturn += evaluateDirection(Direction.horizontal, reflections, puzzleNumber)
    if sumToReturn == 0:
        sumToReturn += evaluateDirection(Direction.vertical, reflections, puzzleNumber)

    return sumToReturn

def evaluateDiagram2(puzzleNumber):
    sumToReturn = 0
    results = lookForAndFixSmudges(Direction.horizontal)
    if results[0]:
        eval = evaluateDirection(Direction.horizontal, results[1], puzzleNumber)
        print('Horizontal:', eval)
        if eval != 0:
            sumToReturn += eval
        else:
            results = lookForAndFixSmudges(Direction.vertical)
            sumToReturn += evaluateDirection(Direction.vertical, results[1], puzzleNumber)
            print('Vertical:', sumToReturn)
    else:
        results = lookForAndFixSmudges(Direction.vertical)
        sumToReturn += evaluateDirection(Direction.vertical, results[1], puzzleNumber)
        print('Vertical:', sumToReturn)

    if sumToReturn == 0:
        results = lookForAndFixSmudges(Direction.horizontal, maskSmudges=1)
        if results[0]:
            eval = evaluateDirection(Direction.horizontal, results[1], puzzleNumber)
            print('Horizontal:', eval)
            if eval != 0:
                sumToReturn += eval
            else:
                results = lookForAndFixSmudges(Direction.vertical, maskSmudges=1)
                sumToReturn += evaluateDirection(Direction.vertical, results[1], puzzleNumber)
                print('Vertical:', sumToReturn)
        else:
            results = lookForAndFixSmudges(Direction.vertical, maskSmudges=1)
            sumToReturn += evaluateDirection(Direction.vertical, results[1], puzzleNumber)
            print('Vertical:', sumToReturn)

    return sumToReturn

def part1(filename):
    global reflections
    reflections = []
    input = open(filename, 'r')
    lines = input.readlines()
    summaryValue = 0
    lineIndex = 0
    puzzleNumber = 1

    for index, line in enumerate(lines):
        if line == '\n':
            summaryValue += evaluateDiagram(puzzleNumber)
            reflections = []
            puzzleNumber += 1
            lineIndex = 0
            continue
        line = line.replace('\n', '')
        reflections.append(line)
        lineIndex += 1
        if index == len(lines) - 1:
            summaryValue += evaluateDiagram(puzzleNumber)
            reflections = []
            puzzleNumber += 1
            lineIndex = 0
            continue
    
    print('PART 1: Summary value:', summaryValue)
    # PART 1 Answer: 29213

def part2(filename):
    global reflections
    input = open(filename, 'r')
    lines = input.readlines()
    summaryValue = 0
    lineIndex = 0
    puzzleNumber = 1

    for index, line in enumerate(lines):
        if line == '\n':
            print('evaluating diagram 1 of puzzle', puzzleNumber)
            summaryValue += evaluateDiagram2(puzzleNumber)
            reflections = []
            puzzleNumber += 1
            lineIndex = 0
            continue
        line = line.replace('\n', '')
        reflections.append(line)
        lineIndex += 1
        if index == len(lines) - 1:
            print('evaluating diagram 2 of puzzle', puzzleNumber)
            summaryValue += evaluateDiagram2(puzzleNumber)
            reflections = []
            puzzleNumber += 1
            lineIndex = 0
            continue
    print('PART 2: Summary value:', summaryValue)
    # PART 2 Answer: 29141 is too low -> 37453 is the answer (get that somehow)

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 13')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/13)


###### WIP ######