#!/usr/bin/env python3

import argparse
import time
from enum import Enum
from functools import cmp_to_key

# fields
totalWinnings = 0
totalWinningsWithJoker = 0
isJokerEnabled = False

class Type(Enum):
    highCard=0
    onePair=1
    twoPairs=2
    threeOfAKind=3
    fullHouse=4
    fourOfAKind=5
    fiveOfAKind=6

# each of these is a tuple
# 0: hand
# 1: bid
# 2: type
hands = []

# helper functions
def noRepeatChars(string):
    if len(string) != 5:
        print('ERROR: noRepeatChars() called with string of length != 5')
        return False

    for char in string:
        if string.count(char) > 1:
            return False
    return True

def checkOnePair(string):
    charSet = set()
    if len(string) != 5:
        print('ERROR: checkOnePair() called with string of length != 5')
        return False

    for char in string:
        if string.count(char) == 2:
            charSet.add(char)

    if len(charSet) == 1:
        return True

def checkTwoPair(string):
    charSet = set()
    if len(string) != 5:
        print('ERROR: checkTwoPair() called with string of length != 5')
        return False

    for char in string:
        if string.count(char) == 2:
            charSet.add(char)

    if len(charSet) == 2:
        return True

def checkFullHouse(string):
    if len(string) != 5:
        print('ERROR: checkFullHouse() called with string of length != 5')
        return False

    charWith3 = ''
    for char in string:
        if string.count(char) == 3:
            charWith3 = char
            continue

    for char in string:
        if charWith3 != '' and char != charWith3 and string.count(char) == 2:
            return True

    return False


def checkXOfAKind(string, x):
    if len(string) != 5:
        print('ERROR: checkXOfAKind() called with string of length != 5')
        return False

    for char in string:
        if string.count(char) == x:
            return True
    return False

def getHandType(hand):
    # ORDER MATTERS HERE (i.e. check for 5 of a kind before 4 of a kind)
    if checkXOfAKind(hand, 5):
        return Type.fiveOfAKind
    elif checkXOfAKind(hand, 4):
        return Type.fourOfAKind
    elif checkFullHouse(hand):
        return Type.fullHouse
    elif checkXOfAKind(hand, 3):
        return Type.threeOfAKind
    elif checkTwoPair(hand):
        return Type.twoPairs
    elif checkOnePair(hand):
        return Type.onePair
    elif noRepeatChars(hand):
        return Type.highCard

class HandWithoutJokers(Enum):
    threeMatching=0
    twoMatching=1
    twoMatchingTheOtherTwo=2
    noMatches=3

def checkHandWithoutJokers(hand):
    charsOfTwo = set()
    for char in hand:
        if hand.count(char) == 3:
            return HandWithoutJokers.threeMatching

    for char in hand:
        if hand.count(char) == 2:
            charsOfTwo.add(char)
    
    if len(charsOfTwo) == 1:
        return HandWithoutJokers.twoMatching
    if len(charsOfTwo) == 2:
        return HandWithoutJokers.twoMatchingTheOtherTwo
    else:
        return HandWithoutJokers.noMatches

def getHandTypeForJokerEnabledHnads(hand):
    if 'J' not in hand:
        return getHandType(hand)
    
    handWithOutJokers = hand.replace('J', '')
    if len(handWithOutJokers) == 0: # JJJJJ
        return Type.fiveOfAKind
    if len(handWithOutJokers) == 1: # XJJJJ
        return Type.fiveOfAKind
    if len(handWithOutJokers) == 2: # XXJJJ
        if handWithOutJokers[0] == handWithOutJokers[1]:
            return Type.fiveOfAKind
        else:
            return Type.fourOfAKind
    if len(handWithOutJokers) == 3: # XXXJJ
        if handWithOutJokers[0] == handWithOutJokers[1] == handWithOutJokers[2]:
            return Type.fiveOfAKind
        elif handWithOutJokers[0] == handWithOutJokers[1] or handWithOutJokers[1] == handWithOutJokers[2] or handWithOutJokers[0] == handWithOutJokers[2]:
            return Type.fourOfAKind
        else: 
            return Type.threeOfAKind
    if len(handWithOutJokers) == 4: # XXXXJ
        if handWithOutJokers[0] == handWithOutJokers[1] == handWithOutJokers[2] == handWithOutJokers[3]:
            return Type.fiveOfAKind
        elif checkHandWithoutJokers(handWithOutJokers) == HandWithoutJokers.threeMatching: 
            return Type.fourOfAKind
        elif checkHandWithoutJokers(handWithOutJokers) == HandWithoutJokers.twoMatchingTheOtherTwo:
            return Type.fullHouse
        elif checkHandWithoutJokers(handWithOutJokers) == HandWithoutJokers.twoMatching:
            return Type.threeOfAKind
        elif checkHandWithoutJokers(handWithOutJokers) == HandWithoutJokers.noMatches:
            return Type.onePair
        else:
            return Type.highCard

def convertHandToNumbers(hand):
    global isJokerEnabled
    hand = list(hand)
    for index, card in enumerate(hand):
        if card == 'T':
            hand[index] = 10
        elif card == 'J' and not isJokerEnabled:
            hand[index] = 11
        elif card == 'J' and isJokerEnabled:
            hand[index] = 0
        elif card == 'Q':
            hand[index] = 12
        elif card == 'K':
            hand[index] = 13
        elif card == 'A':
            hand[index] = 14
        else:
            hand[index] = int(card)
    return hand

def compareHands(hand1, hand2):
    hand1 = convertHandToNumbers(hand1)
    hand2 = convertHandToNumbers(hand2)

    if len(hand1) != len(hand2):
        print('ERROR: compareHands() called with hands of different lengths')
        return 0

    for i in range(len(hand1)):
        if hand1[i] > hand2[i]:
            return 1
        elif hand1[i] < hand2[i]:
            return -1

def compare(tuple1, tuple2):
    hand1, bid1, type1 = tuple1
    hand2, bid2, type2 = tuple2
    if type1.value == type2.value:
        return compareHands(hand1, hand2)
    elif type1.value > type2.value:
        return 1
    else:
        return -1

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global totalWinnings, hands, isJokerEnabled
    isJokerEnabled = False

    for line in lines:
        line = line.replace('\n', '')
        lineInfo = line.split(' ')
        hand = lineInfo[0]
        bid = int(lineInfo[1])
        type = getHandType(hand)
        hands.append((hand, bid, type))

    compare_key = cmp_to_key(compare)
    sortedHands = sorted(hands, key=compare_key)
        
    for index, hand in enumerate(sortedHands):
        hand, bid, type = hand
        totalWinnings += bid * (index + 1)
    
    print('PART 1: Total Winnings: ' + str(totalWinnings))
    # PART 1 Answer: 248812215

def part2(filename):
    # J cards are jokers
    input = open(filename, 'r')
    lines = input.readlines()
    global totalWinningsWithJoker, hands, isJokerEnabled
    isJokerEnabled = True
    hands = []

    for line in lines:
        line = line.replace('\n', '')
        lineInfo = line.split(' ')
        hand = lineInfo[0]
        bid = int(lineInfo[1])
        type = getHandTypeForJokerEnabledHnads(hand)
        hands.append((hand, bid, type))

    compare_key = cmp_to_key(compare)
    sortedHands = sorted(hands, key=compare_key)

    for index, hand in enumerate(sortedHands):
        hand, bid, type = hand
        print("  Hand:", hand, bid, "Multiplier:", str(index + 1), type)
        totalWinningsWithJoker += bid * (index + 1)

    print('PART 2: Total Winnings: ' + str(totalWinningsWithJoker))
    # PART 2 Answer: 250057090

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 7')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/7)