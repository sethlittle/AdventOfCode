#!/usr/bin/env python3

import argparse
import time
import sys

# fields
directionalMap = {
    # [(x: 0, y: 0), (x: 0, y: 0)]
    '|': [(0, -1), (0, 1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
    '.': [(0, 0), (0, 0)]
    # S (starting point) type is determined by the exactly 2 non-zero directional values
}
path = []
startingPostion = (0, 0)
grid = [0, 0] # gridWidthAndHeight

mapOfLocations = {} # key: location (x, y), value: directionalMap values for that letter

# helper functions
def getOpenings(x, y):
    global mapOfLocations
    foundOpening = []
    
    # check if any point towards the current position ( and ensure it isnt already in the paths )
    # check left
    if x > 0 and (mapOfLocations[(x-1, y)][0] == (1, 0) or mapOfLocations[(x-1, y)][1] == (1, 0)):
        foundOpening.append((x-1, y))

    # check right
    if x < len(mapOfLocations) and (mapOfLocations[(x+1, y)][0] == (-1, 0) or mapOfLocations[(x+1, y)][1] == (-1, 0)):
        foundOpening.append((x+1, y))

    # check up
    if y > 0 and (mapOfLocations[(x, y-1)][0] == (0, 1) or mapOfLocations[(x, y-1)][1] == (0, 1)):
        foundOpening.append((x, y-1))

    # check down
    if y < len(mapOfLocations) and (mapOfLocations[(x, y+1)][0] == (0, -1) or mapOfLocations[(x, y+1)][1] == (0, -1)):
        foundOpening.append((x, y+1))

    return foundOpening

def searchLoop(x, y, previousLocation=None):
    global mapOfLocations, startingPostion, path
    if (x, y) == startingPostion and previousLocation is None:
        path.append((x, y))
        openings = getOpenings(x, y) # There should be 2 here, we just wan the first one to travel down that path
        return searchLoop(openings[0][0], openings[0][1], (x, y))
    elif (x, y) == startingPostion:
        return

    path.append((x, y))
    connections = mapOfLocations[(x, y)]
    firstDirection = connections[0]
    secondDirection = connections[1]
    if (x + firstDirection[0], y + firstDirection[1]) != previousLocation:
        return searchLoop(x + firstDirection[0], y + firstDirection[1], (x, y))
    else:
        return searchLoop(x + secondDirection[0], y + secondDirection[1], (x, y))

def part1(filename):
    global startingPostion, mapOfLocations, directionalMap, grid
    input = open(filename, 'r')
    lines = input.readlines()
    grid[1] = len(lines)

    for lineIndex, line in enumerate(lines):
        grid[0] = len(line)
        line = line.replace('\n', '')
        for charIndex, char in enumerate(line):
            if char == 'S':
                startingPostion = (charIndex, lineIndex)
                mapOfLocations[(charIndex, lineIndex)] = directionalMap['.']
            else:
                mapOfLocations[(charIndex, lineIndex)] = directionalMap[char]
    
    sys.setrecursionlimit(100000)
    searchLoop(startingPostion[0], startingPostion[1])
    
    print('PART 1: Steps to the furthest point: ' + str(len(path) / 2))
    # PART 1 Answer: 6947

# if you shoot a ray from a point to the edge of the grid, the ray crosses the edge an odd number of times if and only if the point is inside the polygon
def evenOdd(x, y, path):
    n = len(path) - 1
    c = False
    for i in range(n + 1):
        if (path[i][0] == x and path[i][1] == y):
            return False # point is on the edge
        elif (path[i][1] > y) != (path[n][1] > y):
            slope = (x - path[i][0]) * (path[n][1] - path[i][1]) - (path[n][0] - path[i][0]) * (y - path[i][1])
            if slope == 0:
                return False
            if (slope < 0) != (path[n][1] < path[i][1]):
                c = not c
        n = i
    return c

def part2():
    global path, grid

    area = 0

    for xValue in range(grid[0] - 1):
        for yValue in range(grid[1]):
            area += evenOdd(xValue, yValue, path)
            
    print('PART 2: Number of locations inside:', str(area))
    # PART 2 Answer: 273

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 9')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/10)