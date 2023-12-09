#!/usr/bin/env python3

import argparse
import time

# fields
sumOfExtrapolatedValiues = 0
sumOfFirstInList = 0
listOfDifferences = []

# helper functions
def backUpTheLadder(differences):
    global sumOfExtrapolatedValiues, listOfDifferences, sumOfFirstInList

    while len(listOfDifferences) > 0:
        newDifferences = listOfDifferences.pop()
        length = len(newDifferences)
        oldLength = len(differences)
        newDifferences.append(int(newDifferences[length-1]) + int(differences[oldLength-1]))
        newDifferences.insert(0, int(newDifferences[0]) - int(differences[0]))
        differences = newDifferences
        
    sumOfExtrapolatedValiues += differences[-1]
    sumOfFirstInList += differences[0]

def recursivelySolve(sequence):
    global listOfDifferences
    differences = []
    for i in range(1, len(sequence)):
        differences.append(int(sequence[i]) - int(sequence[i-1]))

    if differences.count(differences[0]) == len(differences):
        differences.append(differences[0])
        backUpTheLadder(differences)
        return
    else:
        listOfDifferences.append(differences)
        return recursivelySolve(differences)

def part1(filename):
    global sumOfExtrapolatedValiues, listOfDifferences
    input = open(filename, 'r')
    lines = input.readlines()

    for line in lines:
        line = line.replace('\n', '')
        sequence = line.split(' ')
        listOfDifferences.append(sequence)
        recursivelySolve(sequence)
    
    print('PART 1: Sum of extrapolated values: ' + str(sumOfExtrapolatedValiues))
    # PART 1 Answer: 2005352194

def part2(filename):
    global sumOfFirstInList

    print('PART 2: Sum of first values: ' + str(sumOfFirstInList))
    # PART 2 Answer: 1077

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 9')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/9)