# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Part 1
# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string needs all of the following:
# * It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# * It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# * It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# How many strings are nice?

# Part 2
# Now, a nice string is one with all of the following properties:
# * It contains a pair of any two letters that appears at least twice in the string without overlapping,
#   like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# * It contains at least one letter which repeats with exactly one letter between them,
#   like xyx, abcdefeghi (efe), or even aaa.

# How many strings are nice under these new rules?

import argparse
import time

niceStrings = []

def is_nice(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    double = False
    badStrings = ['ab', 'cd', 'pq', 'xy']
    vowelCount = 0
    for i in range(len(string)):
        if string[i] in vowels:
            vowelCount += 1
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                double = True
        if string[i:i + 2] in badStrings:
            return False
    if vowelCount >= 3 and double:
        return True
    else:
        return False

def is_nice2(string):
    double = False
    repeatedLetter = False
    for i in range(len(string)):
        if i < len(string) - 2:
            if string[i] == string[i + 2]:
                repeatedLetter = True
        if i < len(string) - 1:
            if string[i:i + 2] in string[i + 2:]:
                double = True
    if double and repeatedLetter:
        return True
    else:
        return False

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global niceStrings

    for line in lines:
        line = line.replace('\n', '')
        if is_nice(line):
            niceStrings.append(line)

    print('PART 1: Number of nice strings: ' + str(len(niceStrings)))
    # PART 1 Answer: 236

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global niceStrings
    niceStrings = []
    
    for line in lines:
        line = line.replace('\n', '')
        if is_nice2(line):
            niceStrings.append(line)

    print("PART 2: Number of nice strings: " + str(len(niceStrings)))
    # PART 2 Answer: 51

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2015 Day 5')
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

# SOLUTION:
# PART 1 Answer: 236
# PART 2 Answer: 51

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/5
