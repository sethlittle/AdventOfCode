#!/usr/bin/env python3

import argparse
import time

# fields
grid = []
galaxies = {} # key: galaxy number, value: location of galaxy in (x, y) terms
xBlankLinesIndexs = []
yBlankLinesIndexs = []

# helper functions
def moveGalaxiesByOffset(offset):
    global galaxies, xBlankLinesIndexs, yBlankLinesIndexs
    newGalaxies = {}

    for galaxy, location in galaxies.items():
        xGaps = 0
        for xIndex in xBlankLinesIndexs:
            if location[0] > xIndex:
                xGaps += 1
            else:
                break

        yGaps = 0
        for yIndex in yBlankLinesIndexs:
            if location[1] > yIndex:
                yGaps += 1
            else:
                break

        xOffset, yOffset = 0, 0
        if xGaps != 0:
            xOffset = (xGaps * (offset - 1))
        if yGaps != 0:
            yOffset = (yGaps * (offset - 1))
        
        newGalaxies[galaxy] = (galaxies[galaxy][0] + xOffset, galaxies[galaxy][1] + yOffset)
    return newGalaxies

def getDistance(mapOfGalaxies):
    sumOfPaths = 0
    for galaxy, location in mapOfGalaxies.items():
        for otherGalaxies, otherLocation in mapOfGalaxies.items():
            if galaxy != otherGalaxies:
                if galaxy < otherGalaxies:
                    # USE THE MANHATTAN DISTANCE- https://xlinux.nist.gov/dads/HTML/manhattanDistance.html
                    sumOfPaths += abs(location[0] - otherLocation[0]) + abs(location[1] - otherLocation[1])
    return sumOfPaths

def part1(filename):
    global grid, galaxies, xBlankLinesIndexs, yBlankLinesIndexs
    input = open(filename, 'r')
    lines = input.readlines()

    for line in lines:
        line = line.replace('\n', '')
        grid.append(line)

    yValues = {} # key: y value, value: array of x values

    for index, line in enumerate(grid):
        if line.count('#') == 0:
            yBlankLinesIndexs.append(index)
        for index, char in enumerate(line):
            if index not in yValues.keys():
                yValues[index] = [char]
            else:
                yValues[index].append(char)

    for key, line in yValues.items():
        if line.count('#') == 0:
            xBlankLinesIndexs.append(key)

    numberOfGalaxies = 0
    for lineIndex, line in enumerate(grid):
        for charIndex, char in enumerate(line):
            if char == '#':
                numberOfGalaxies += 1
                galaxies[numberOfGalaxies] = (charIndex, lineIndex)

    updatedGalaxies = moveGalaxiesByOffset(10)

    print('PART 1: Sum of all the shortest paths between all the galaxies is: ' + str(getDistance(updatedGalaxies)))
    # PART 1 Answer: 10276166

def part2():
    updatedGalaxies = moveGalaxiesByOffset(1000000)

    print('PART 2: Sum of all the shortest paths between all the galaxies is: ' + str(getDistance(updatedGalaxies)))
    # PART 2 Answer: 598693078798

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 11')
    parser.add_argument('input_file', metavar='filename', type=str, default='inputFile.txt', help='Path to input.')
    args = parser.parse_args()

    start_time = time.time()
    part1(args.input_file)
    print('Part 1 execution time: {:.3f} seconds'.format(time.time() - start_time))

    start_time = time.time()
    part2()
    print('Part 2 execution time: {:.3f} seconds'.format(time.time() - start_time))

if __name__ == '__main__':
    main()

#Source: [AdventOfCode](https://adventofcode.com/2023/day/11)