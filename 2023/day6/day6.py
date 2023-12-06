#!/usr/bin/env python3

import argparse
import time

# fields
possibilities = 1
mapOfRaces = {}

# helper functions
def calculatePossibilities(time, distance):
    possibilitiesThisGame = 0
    for i in range(time):
        speed = i # time spent holding it down
        distanceTravelled = speed * (time - i)
        if distanceTravelled > distance:
            possibilitiesThisGame += 1
    return possibilitiesThisGame

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global possibilities
    times = list(filter(lambda a: a != '', lines[0][5:].strip().split(' ')))
    distances = list(filter(lambda a: a != '', lines[1][9:].strip().split(' ')))
    races = list(zip(times, distances))

    for index, race in enumerate(races):
        mapOfRaces[index] = calculatePossibilities(int(race[0]), int(race[1]))
        
    for value in mapOfRaces.values():
        possibilities *= value
    
    print('PART 1: Total number of possibilites: ' + str(possibilities))
    # PART 1 Answer: 32076

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global possibilities
    possibilities = 0
    time = int(lines[0][5:].strip().replace(' ', ''))
    distance = int(lines[1][9:].strip().replace(' ', ''))

    possibilities = calculatePossibilities(time, distance)

    print('PART 2: Total number of ways to win: ' + str(possibilities))
    # PART 2 Answer: 34278221

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 6')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/6)