#!/usr/bin/env python3

import argparse
import time
from enum import Enum

# fields
possibleContraptionsWithOneUse = [
    '|', # pointy end of a splitter -> passes through as normal, flat-side the beam is split into two beams (up and down)
    '-', # pointy end of a splitter -> passes through as normal, flat-side the beam is split into two beams (left and right)
]

possibleContraptionsWithMultiUse = [
    '/', # beam is reflected 90 degrees
    '\\', # beam is reflected 90 degrees
]

grid = {} # key: tuple (x, y), value: [character, numberOfTimesChecked]
gridWidth = 0
gridHeight = 0

# Part 2
energizedAmounts = set()

class BeamDirection(Enum):
    towardsTheRight = 0
    towardsTheBottom = 1
    towardsTheLeft = 2
    towardsTheTop = 3

# helper functions
def clearGrid():
    global grid
    for location, value in grid.items():
        value[1] = 0

def getNextLocation(currentBeamDirection: BeamDirection, currentLocation: tuple) -> tuple:
    if currentBeamDirection == BeamDirection.towardsTheRight:
        return (currentLocation[0] + 1, currentLocation[1])
    elif currentBeamDirection == BeamDirection.towardsTheBottom:
        return (currentLocation[0], currentLocation[1] + 1)
    elif currentBeamDirection == BeamDirection.towardsTheLeft:
        return (currentLocation[0] - 1, currentLocation[1])
    elif currentBeamDirection == BeamDirection.towardsTheTop:
        return (currentLocation[0], currentLocation[1] - 1)
    
def evaluateEnergy(beamsInMovement: {}):
    # where beamsInMovement is a dictionary with the following: key: beamId, value: array of tuple (x, y) location and BeamDirection
    global grid, possibleContraptionsWithOneUse, possibleContraptionsWithMultiUse
    tilesEnergized = 0
    beamID = 1
    while len(beamsInMovement) > 0:
        for id, beamItems in beamsInMovement.copy().items():
            beamLocation = beamItems[0]
            beamDirection = beamItems[1]
            nextLocation = getNextLocation(beamDirection, beamLocation)
            if nextLocation in grid.keys():
                if grid[nextLocation][0] in possibleContraptionsWithOneUse and grid[nextLocation][1] > 1:
                    # Found a splitter that has already been checked
                    del beamsInMovement[id]
                elif grid[nextLocation][0] in possibleContraptionsWithMultiUse and grid[nextLocation][1] > 4:
                    # mirrors are not done when they have been checked once, we need to check to make
                    # sure both sides have been checked, this needs to be updated but for now its fine for now
                    del beamsInMovement[id]
                else:
                    if grid[nextLocation][0] == '|':
                        # Found a vertical splitter
                        if beamDirection == BeamDirection.towardsTheLeft or beamDirection == BeamDirection.towardsTheRight:
                            beamsInMovement[beamID] = [nextLocation, BeamDirection.towardsTheTop]
                            beamsInMovement[id] = [nextLocation, BeamDirection.towardsTheBottom]
                            beamID += 1  
                        else:
                            beamsInMovement[id][0] = nextLocation                      
                    elif grid[nextLocation][0] == '-':
                        # Found a horizontal splitter
                        if beamDirection == BeamDirection.towardsTheTop or beamDirection == BeamDirection.towardsTheBottom:
                            beamsInMovement[beamID] = [nextLocation, BeamDirection.towardsTheLeft]
                            beamsInMovement[id] = [nextLocation, BeamDirection.towardsTheRight]
                            beamID += 1
                        else:
                            beamsInMovement[id][0] = nextLocation
                    elif grid[nextLocation][0] == '/':
                        # Found a forward slash mirror
                        newDirection = beamDirection
                        if beamDirection == BeamDirection.towardsTheTop:
                            newDirection = BeamDirection.towardsTheRight
                        elif beamDirection == BeamDirection.towardsTheRight:
                            newDirection = BeamDirection.towardsTheTop
                        elif beamDirection == BeamDirection.towardsTheBottom:
                            newDirection = BeamDirection.towardsTheLeft
                        elif beamDirection == BeamDirection.towardsTheLeft:
                            newDirection = BeamDirection.towardsTheBottom
                        beamsInMovement[id] = [nextLocation, newDirection]
                    elif grid[nextLocation][0] == '\\':
                        # Found a back slash mirror
                        newDirection = beamDirection
                        if beamDirection == BeamDirection.towardsTheTop:
                            newDirection = BeamDirection.towardsTheLeft
                        elif beamDirection == BeamDirection.towardsTheLeft:
                            newDirection = BeamDirection.towardsTheTop
                        elif beamDirection == BeamDirection.towardsTheRight:
                            newDirection = BeamDirection.towardsTheBottom
                        elif beamDirection == BeamDirection.towardsTheBottom:
                            newDirection = BeamDirection.towardsTheRight
                        beamsInMovement[id] = [nextLocation, newDirection]
                    else:
                        # Found a normal tile (.)
                        beamsInMovement[id][0] = nextLocation
                grid[nextLocation][1] += 1
            else:
                # Beam has left the grid, remove it
                del beamsInMovement[id]

    for loc, info in grid.items():
        if info[1] > 0:
            tilesEnergized += 1
    clearGrid()
    return tilesEnergized

def part1(filename: str):
    global grid, gridWidth, gridHeight
    # beam enters in the top-left corner from the left and heading to the right.

    input = open(filename, 'r')
    lines = input.readlines()
    gridHeight = len(lines)

    for lineIndex, line in enumerate(lines):
        line = line.replace('\n', '')
        gridWidth = len(line)
        for charIndex, char in enumerate(line):
            grid[(charIndex, lineIndex)] = [char, 0]

    beamsInMovement = {'0':[(-1,0), BeamDirection.towardsTheRight]} #
        
    print('PART 1: Total Number of tiles energized {}'.format(evaluateEnergy(beamsInMovement)))
    # PART 1 Answer: 7608

def part2(filename):
    global gridWidth, gridHeight, energizedAmounts

    # test the energy at every entrypoint on all sides of the grid
    
    for i in range(gridHeight):
        energizedAmounts.add(evaluateEnergy({'0':[(-1,i), BeamDirection.towardsTheRight]}))
        energizedAmounts.add(evaluateEnergy({'0':[(gridWidth,i), BeamDirection.towardsTheLeft]}))

    for i in range(gridWidth):
        energizedAmounts.add(evaluateEnergy({'0':[(i,-1), BeamDirection.towardsTheBottom]}))
        energizedAmounts.add(evaluateEnergy({'0':[(i,gridHeight), BeamDirection.towardsTheTop]}))

    print('PART 2: Tiles energized in most optimal configuration {}'.format(max(energizedAmounts)))
    # PART 2 Answer: 8221

def test():
    assert(getNextLocation(BeamDirection.towardsTheRight, (-1,0)) == (0,0))

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 16')
    parser.add_argument('input_file', metavar='filename', type=str, default='inputFile.txt', help='Path to input.')
    args = parser.parse_args()

    start_time = time.time()
    part1(args.input_file)
    print('Part 1 execution time: {:.3f} seconds'.format(time.time() - start_time))

    start_time = time.time()
    part2(args.input_file)
    print('Part 2 execution time: {:.3f} seconds'.format(time.time() - start_time))

if __name__ == '__main__':
    test()
    main()

#Source: [AdventOfCode](https://adventofcode.com/2023/day/16)