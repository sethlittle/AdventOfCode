#!/usr/bin/env python3

import argparse
import time

# fields

# helper functions
def holidayHashFunction(input: str):
    value = 0
    for char in input:
        value += ord(char)
        value = value * 17
        value = value % 256
    return value    

def caclulateFocusingPower(box: int, lenses: {}) -> int:
    focusingPower = 0
    for label, lenseInfo in lenses.items():
        power = (box + 1) * lenseInfo[0] * lenseInfo[1]
        focusingPower += power
    return focusingPower

def part1(filename: str):
    input = open(filename, 'r')
    lines = input.readlines()
    directions = lines[0].replace('\n', '').split(',')

    sumOfResults = 0
    for input in directions:
        value = holidayHashFunction(input)
        sumOfResults += value
    
    print('PART 1: Sum of results: {}'.format(sumOfResults))
    # PART 1 Answer: 517015

def part2(filename):
    boxes = {} # key: box, value: dictionary where the key is the lense label and the value is a list of the focal length and the position
    for i in range(256):
        boxes[i] = {}
    # Box 0: {'rn': [1, 1], 'cm': [2, 2]}
    totalFocusingPower = 0
    directions = open(filename, 'r').readlines()[0].replace('\n', '').split(',')

    for input in directions:
        if '=' in input:
            parts = input.split('=')
            label = parts[0]
            focalLength = int(parts[1])
            boxNumber = holidayHashFunction(label)
            
            if label in boxes[boxNumber].keys():
                boxes[boxNumber][label][0] = focalLength
            else:
                boxes[boxNumber][label] = [focalLength, len(boxes[boxNumber]) + 1]
        else: # must be a '-'
            label = input.replace('-', '')
            boxNumber = holidayHashFunction(label)
            if label in boxes[boxNumber].keys():
                position = boxes[boxNumber][label][1]
                boxes[boxNumber].pop(label, None)
                for key in boxes[boxNumber].keys():
                    if boxes[boxNumber][key][1] > position:
                        boxes[boxNumber][key][1] -= 1

    for box, lenses in boxes.items():
        totalFocusingPower += caclulateFocusingPower(box, lenses)

    print('PART 2: Total Focusing Power: {}'.format(totalFocusingPower))
    # PART 2 Answer: 286104

def test():
    assert(0 == holidayHashFunction('rn'))
    assert(3 == holidayHashFunction('pc'))
    assert(52 == holidayHashFunction('HASH'))

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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/15)