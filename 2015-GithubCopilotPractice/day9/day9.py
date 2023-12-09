# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

# --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

import argparse
import itertools

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2015 Day 9')
    parser.add_argument('input_file', metavar='filename', type=str, default='inputFile.txt', help='Path to input.')
    args = parser.parse_args()

    input = open(args.input_file, 'r')
    lines = input.readlines()

    distances = {}
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(' ')
        if line[0] not in distances:
            distances[line[0]] = {}
        if line[2] not in distances:
            distances[line[2]] = {}
        distances[line[0]][line[2]] = int(line[4])
        distances[line[2]][line[0]] = int(line[4])

    cities = list(distances.keys())
    permutations = list(itertools.permutations(cities))

    shortestDistance = 999999
    longestDistance = 0
    for permutation in permutations:
        distance = 0
        for i in range(1, len(permutation)):
            distance += distances[permutation[i-1]][permutation[i]]
        if distance < shortestDistance:
            shortestDistance = distance
        if distance > longestDistance:
            longestDistance = distance

    print('PART 1: Shortest distance: ' + str(shortestDistance))
    # PART 1 Answer: 207
    print('PART 2: Longest distance: ' + str(longestDistance))
    # PART 2 Answer: 804

if __name__ == '__main__':
    main()

# SOLUTION:
# Part 1: 207
# Part 2: 804

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/9
