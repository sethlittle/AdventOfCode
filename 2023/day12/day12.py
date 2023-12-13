#!/usr/bin/env python3

import argparse
import time
from functools import cache

# TIP: -> ? can become both a '.' and a '#'
# try: r += (... P[p:p+N[n]] ...)
# except IndexError: pass

# fields

# helper functions
# got help online for this function (move slowly through the string)
@cache
def getPossibleArrangements(recordFragment, configurations, num_done_in_group=0):
    if not recordFragment:
        return not configurations and not num_done_in_group
    numberOfPossibleArrangements = 0
    possibleValues = ['.', '#'] if recordFragment[0] == '?' else recordFragment[0]
    for option in possibleValues:
        if option == '#': #extend current group
            numberOfPossibleArrangements += getPossibleArrangements(recordFragment[1:], configurations, num_done_in_group + 1)
        else: 
            if num_done_in_group:
                # close group
                if configurations and configurations[0] == num_done_in_group:
                    numberOfPossibleArrangements += getPossibleArrangements(recordFragment[1:], configurations[1:])
            else:
                # move forward
                numberOfPossibleArrangements += getPossibleArrangements(recordFragment[1:], configurations)
    return numberOfPossibleArrangements
    
# '.' is operational
# '#' is damaged
# '?' is unknown
def part1(filename):
    sumOfPossibleArrangements = 0
    with open(filename) as file:
        parts = [line.split(' ') for line in file.read().strip().split('\n')]

    records = [(record, tuple(map(int, stringConfigs.split(',')))) for record, stringConfigs in parts]

    for record, configs in records:
        sumOfPossibleArrangements += getPossibleArrangements(record + '.', configs)

    print('PART 1: Sum of possible counts:', sumOfPossibleArrangements)
    # PART 1 Answer: 7032

def part2(filename):
    sumOfPossibleArrangements = 0
    with open(filename) as file:
        parts = [line.split() for line in file.read().strip().split('\n')]

    records = [(record, tuple(map(int, stringConfigs.split(',')))) for record, stringConfigs in parts]

    for index, (record, configs) in enumerate(records):
        records[index] = (record + '?' + record + '?' + record + '?' + record + '?' + record, configs * 5)

    for record, configs in records:
        arrangements = getPossibleArrangements(record + '.', configs)
        sumOfPossibleArrangements += arrangements

    print('PART 2: Sum of possible counts:', sumOfPossibleArrangements)
    # PART 2 Answer: 

def test():
    assert(10 == getPossibleArrangements('?###????????' + '.', (3,2,1)))
    assert(4 == getPossibleArrangements('????.######..#####.' + '.', (1,6,5)))
    assert(1 == getPossibleArrangements('????.#...#...' + '.', (4,1,1)))
    assert(1 == getPossibleArrangements('?#?#?#?#?#?#?#?' + '.', (1,3,1,6)))
    assert(4 == getPossibleArrangements('.??..??...?##.' + '.', (1,1,3)))
    assert(1 == getPossibleArrangements('???.### 1,1,3' + '.', (1,1,3)))

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
    test()
    main()

#Source: [AdventOfCode](https://adventofcode.com/2023/day/12)