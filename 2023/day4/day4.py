#!/usr/bin/env python3

import argparse
import time

# fields
sum = 0 # part 1
sumOfScratchcards = 0 # part 2
numberOfCardsMap = {} # key: card, value: number of that card
mapOfWinningNumbers = {} # key: card, value: list of winning numbers
mapOfCardNumbers = {} # key: card, value: list of card numbers
mapOfCardsAndNumberOfMatches = {} # key: card, value: number of matches

# helper functions

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global sum, mapOfWinningNumbers, mapOfCardNumbers, mapOfCardsAndNumberOfMatches, mapOfCardNumbers
    currentCardMatches = 0

    for line in lines:
        line = line.replace('\n', '')
        cardAndNumbers = line.split(':')
        card = int(cardAndNumbers[0][5:])
        numbers = cardAndNumbers[1].strip().split('|')
        winningNumbers = list(filter(lambda a: a != '', numbers[0].strip().split(' ')))
        cardNumbers = list(filter(lambda a: a != '', numbers[1].strip().split(' ')))
        numberOfCardsMap[card] = 1
        mapOfWinningNumbers[card] = winningNumbers
        mapOfCardNumbers[card] = cardNumbers

        for number in cardNumbers:
            if number in winningNumbers:
                currentCardMatches += 1
        
        mapOfCardsAndNumberOfMatches[card] = currentCardMatches
        if currentCardMatches != 0:
            sum += 2**(currentCardMatches - 1)
        currentCardMatches = 0
    
    print('PART 1: Pile of scratchoffs is worth: ' + str(sum))
    # PART 1 Answer: 27059

def part2():
    global sumOfScratchcards, mapOfCardsAndNumberOfMatches, mapOfCardNumbers, numberOfCardsMap

    for key, value in mapOfCardsAndNumberOfMatches.items():
        copies = numberOfCardsMap[key]
        for i in range(1, value + 1):
            numberOfCardsMap[key + i] += (1*copies)

    for numberOfCards in numberOfCardsMap.values():
        sumOfScratchcards += numberOfCards
    print('PART 2: Total number of winning cards: ' + str(sumOfScratchcards))
    # PART 2 Answer: 5744979

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 4')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/4)