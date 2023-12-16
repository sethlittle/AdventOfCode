#!/usr/bin/env python3

import argparse
import time
from enum import Enum
from functools import cache

# fields
values = {}
mapOfLayout = []

class direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4

# helper functions
def cycle():
    global mapOfLayout

    mapOfLayout = list(zip(*mapOfLayout))
    evaluateRoundRocks(direction.NORTH)
    # printedLayout = list(zip(*mapOfLayout))
    # print('N:', *printedLayout, sep='\n')

    mapOfLayout = list(zip(*mapOfLayout))
    evaluateRoundRocks(direction.EAST)
    # print('LR 1:', *mapOfLayout, sep='\n')

    mapOfLayout = list(zip(*mapOfLayout))
    evaluateRoundRocks(direction.SOUTH)
    # printedLayout = list(zip(*mapOfLayout))
    # print('S:', *printedLayout, sep='\n')

    mapOfLayout = list(zip(*mapOfLayout))
    evaluateRoundRocks(direction.WEST)
    # print('LR 2:', *mapOfLayout, sep='\n')

def moveRocksLeftOrNorth(lineIndex, rocksToMoveLeft):
    global mapOfLayout
    while rocksToMoveLeft != []:
        charIndex = rocksToMoveLeft.pop(0)
        blocked = False
        while charIndex != 0 and not blocked:
            if mapOfLayout[lineIndex][charIndex - 1] == '#' or mapOfLayout[lineIndex][charIndex - 1] == 'O':
                blocked = True
            else:
                mapOfLayout[lineIndex] = list(mapOfLayout[lineIndex])
                mapOfLayout[lineIndex][charIndex] = '.'
                mapOfLayout[lineIndex][charIndex - 1] = 'O'     
                charIndex -= 1       

def moveRocksRightOrSouth(lineIndex, rocksToMoveRight):
    global mapOfLayout
    while rocksToMoveRight != []:
        charIndex = rocksToMoveRight.pop()
        if charIndex == len(mapOfLayout[lineIndex]) - 1:
            continue
        blocked = False
        while charIndex != len(mapOfLayout[lineIndex]) - 1 and not blocked:
            if mapOfLayout[lineIndex][charIndex + 1] == '#' or mapOfLayout[lineIndex][charIndex + 1] == 'O':
                blocked = True
            else:
                mapOfLayout[lineIndex] = list(mapOfLayout[lineIndex])
                mapOfLayout[lineIndex][charIndex] = '.'
                mapOfLayout[lineIndex][charIndex + 1] = 'O'     
                charIndex += 1

def evaluateRoundRocks(direction):
    global mapOfLayout
    allRocksToMove = []
    for lineIndex, line in enumerate(mapOfLayout):
        for charIndex, char in enumerate(line):
            if char == 'O':
                allRocksToMove.append(charIndex)
        if direction == direction.NORTH or direction == direction.EAST:
            moveRocksLeftOrNorth(lineIndex, allRocksToMove)
        else:
            moveRocksRightOrSouth(lineIndex, allRocksToMove)
        allRocksToMove = []

def part1(filename):
    global mapOfLayout
    input = open(filename, 'r')
    lines = input.readlines()
    totalLoad = 0

    for index, line in enumerate(lines):
        line = line.replace('\n', '')
        mapOfLayout.append(line)

    mapOfLayout = list(zip(*mapOfLayout))
    evaluateRoundRocks(direction.NORTH)

    mapOfLayout = list(zip(*mapOfLayout))
    
    for index, line in enumerate(mapOfLayout):
        values[len(mapOfLayout) - index] = line

    for key, line in values.items():
        for char in line:
            if char == 'O':
                totalLoad += key

    print('PART 1: Total Load on the Support Beams:', totalLoad)
    # PART 1 Answer: 110128

# PART 2 major help from internet
@cache 
def move_north(rockMap: tuple[str]) -> tuple[str]:
    rockMap = list(rockMap)
    for y, row in enumerate(rockMap):
        for x, char in enumerate(row):
            if char != 'O':
                continue
            obstacles_y = [y for y in range(y) if rockMap[y][x] in '#O']
            new_y = max(obstacles_y, default=-1) + 1
            if new_y != y:
                rockMap[y] = rockMap[y][:x] + '.' + rockMap[y][x + 1:]
                rockMap[new_y] = rockMap[new_y][:x] + 'O' + rockMap[new_y][x + 1:]
    return tuple(rockMap)

@cache
def turn_clockwise(rockMap: tuple[str]) -> tuple[str]:
    return tuple(''.join(row) for row in zip(*rockMap[::-1]))

@cache
def thousand_cycles(rockMap: tuple[str]) -> tuple[str]:
    for _ in range(4 * 1000):
        rockMap = move_north(rockMap)
        rockMap = turn_clockwise(rockMap)
    return rockMap

def caclulate_load(rockMap: tuple[str]) -> int:
    height = len(rockMap)
    return sum(row.count('O') * (height - y) for y, row in enumerate(rockMap))

def part2(filename):
    # global mapOfLayout, values
    # mapOfLayout = []
    # values = {}
    # cycles = 1000000000
    # input = open(filename, 'r')
    # lines = input.readlines()
    # totalLoad = 0

    # for index, line in enumerate(lines):
    #     line = line.replace('\n', '')
    #     mapOfLayout.append(line)

    # layoutsSet = set()
    # copy = map(tuple, mapOfLayout.copy())
    # layoutsSet.add(copy)
    # while cycles != 0:
    #     # print('Cycle:', cycles)
    #     if cycles % 1000 == 0:
    #         print('Cycle:', cycles)
    #     cycle()
    #     copy = map(tuple, mapOfLayout.copy())
    #     if copy in layoutsSet:
    #         print('CYCLIC ALERT', cycles)
    #         print('COPY:', copy)
    #         print('map:', mapOfLayout)
    #         break
    #     else:
    #         layoutsSet.add(copy)
    #     cycles -= 1

    # for index, line in enumerate(mapOfLayout):
    #     values[len(mapOfLayout) - index] = line

    # for key, line in values.items():
    #     for char in line:
    #         if char == 'O':
    #             totalLoad += key

    # print('PART 2: Total Load on the Support Beams:', totalLoad)

    rockMap = tuple(open(filename).read().splitlines())
    for i in range (1_000_000_000 // 1000):
        rockMap = thousand_cycles(rockMap)

    print('PART 2: Total Load on the Support Beams:', caclulate_load(rockMap))
    # PART 2 Answer: 103861

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 14')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/14)

# ******** WIP ********
# try adding cache to all the functions we used in 1
