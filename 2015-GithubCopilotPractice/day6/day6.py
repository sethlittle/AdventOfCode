# --- Day 6: Probably a Fire Hazard ---
# --- Part One ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
# # Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

import argparse
import re
import concurrent.futures
import threading

# Global Variables
# 1000x1000 grid
grid = [[0 for x in range(1000)] for y in range(1000)]

def turnOn(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] = 1

def turnOff(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] = 0

def toggle(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0

def allMaps():
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[x][y] == 1:
                print('X', end='')
            else:
                print('.', end='')
        print('')

def function(threadNumber):
    print('Thread ' + str(threadNumber) + ' started')
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[x][y] == 1:
                print('X', end='')
            else:
                print('.', end='')
        print('')
    print('Thread ' + str(threadNumber) + ' done')

def switchActiveMap(line):
    if line.startswith('turn on'):
        x1 = int(line[8:].split(' through ')[0].split(',')[0])
        y1 = int(line[8:].split(' through ')[0].split(',')[1])
        x2 = int(line[8:].split(' through ')[1].split(',')[0])
        y2 = int(line[8:].split(' through ')[1].split(',')[1])
        turnOn(x1, y1, x2, y2)
    elif line.startswith('turn off'):
        x1 = int(line[9:].split(' through ')[0].split(',')[0])
        y1 = int(line[9:].split(' through ')[0].split(',')[1])
        x2 = int(line[9:].split(' through ')[1].split(',')[0])
        y2 = int(line[9:].split(' through ')[1].split(',')[1])
        turnOff(x1, y1, x2, y2)
    elif line.startswith('toggle'):
        x1 = int(line[7:].split(' through ')[0].split(',')[0])
        y1 = int(line[7:].split(' through ')[0].split(',')[1])
        x2 = int(line[7:].split(' through ')[1].split(',')[0])
        y2 = int(line[7:].split(' through ')[1].split(',')[1])
        toggle(x1, y1, x2, y2)
    else:
        print('Error: ' + line)

def getActiveLights():
    global grid
    activeLights = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[x][y] == 1:
                activeLights += 1
    return activeLights

def raiseBrightness(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] += 1

def lowerBrightness(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[x][y] > 0:
                grid[x][y] -= 1

def toggleBrightness(x1, y1, x2, y2):
    global grid
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] += 2

def switchBrightnessMap(line):
    if line.startswith('turn on'):
        x1 = int(line[8:].split(' through ')[0].split(',')[0])
        y1 = int(line[8:].split(' through ')[0].split(',')[1])
        x2 = int(line[8:].split(' through ')[1].split(',')[0])
        y2 = int(line[8:].split(' through ')[1].split(',')[1])
        raiseBrightness(x1, y1, x2, y2)
    elif line.startswith('turn off'):
        x1 = int(line[9:].split(' through ')[0].split(',')[0])
        y1 = int(line[9:].split(' through ')[0].split(',')[1])
        x2 = int(line[9:].split(' through ')[1].split(',')[0])
        y2 = int(line[9:].split(' through ')[1].split(',')[1])
        lowerBrightness(x1, y1, x2, y2)
    elif line.startswith('toggle'):
        x1 = int(line[7:].split(' through ')[0].split(',')[0])
        y1 = int(line[7:].split(' through ')[0].split(',')[1])
        x2 = int(line[7:].split(' through ')[1].split(',')[0])
        y2 = int(line[7:].split(' through ')[1].split(',')[1])
        toggleBrightness(x1, y1, x2, y2)
    else:
        print('Error: ' + line)

def getBrightness():
    global grid
    brightness = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            brightness += grid[x][y]
    return brightness

def main():
    global grid
    parser = argparse.ArgumentParser(description='Advent of Code 2015 Day 6')
    parser.add_argument('input_file', metavar='input_file', type=str, nargs='?', default='input.txt', help='The name of the input file.')
    parser.add_argument('-t', '--threads', metavar='threads', type=int, nargs='?', default=1, help='The number of threads to use.')
    args = parser.parse_args()

    # Read the input file
    with open(args.input_file) as file:
        input = file.readlines()

    for line in input:
        switchActiveMap(line)

    print(int(getActiveLights()))

    grid = [[0 for x in range(1000)] for y in range(1000)]

    for line in input:
        switchBrightnessMap(line)

    print(int(getBrightness()))

    # with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    #     executor.map(function, range(0, args.threads))
    
if __name__ == '__main__':
    main()

#SOLUTION:
# PART 1: 400410
# PART 2: 15343601

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/6
