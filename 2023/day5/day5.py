#!/usr/bin/env python3

import argparse
import time
from enum import Enum
import threading
import concurrent.futures

# helper classes
class Map(Enum):
    seedToSoil=0
    soilToFertilizer=1
    fertilizerToWater=2
    waterToLight=3
    lightToTemperature=4
    temperatureToHumidity=5
    humidityToLocation=6

# fields
seeds = []
seedsToLocationsMap = {}
ranges = []
mapOfRanges = {} # key is the number of the range and value is the range

activeMap = Map.seedToSoil
seedsToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

def appendItemToList(line):
    global activeMap, seedsToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation
    lineInfo = line.split(' ')
    destinationRangeStart = int(lineInfo[0])
    sourceRangeStart = int(lineInfo[1])
    rangeLength = int(lineInfo[2])
    itemToAppend = (destinationRangeStart, sourceRangeStart, rangeLength)
    if activeMap == Map.seedToSoil:
        seedsToSoil.append(itemToAppend)
    elif activeMap == Map.soilToFertilizer:
        soilToFertilizer.append(itemToAppend)
    elif activeMap == Map.fertilizerToWater:
        fertilizerToWater.append(itemToAppend)
    elif activeMap == Map.waterToLight:
        waterToLight.append(itemToAppend)
    elif activeMap == Map.lightToTemperature:
        lightToTemperature.append(itemToAppend)
    elif activeMap == Map.temperatureToHumidity:
        temperatureToHumidity.append(itemToAppend)
    elif activeMap == Map.humidityToLocation:
        humidityToLocation.append(itemToAppend)

def switchActiveMap(line):
    global activeMap
    map = line[:-5].split('-to-')
    source = map[0]
    if source == 'seed' and map[1] == 'soil':
        activeMap = Map.seedToSoil
    elif source == 'soil':
        activeMap = Map.soilToFertilizer
    elif source == 'fertilizer':
        activeMap = Map.fertilizerToWater
    elif source == 'water':
        activeMap = Map.waterToLight
    elif source == 'light':
        activeMap = Map.lightToTemperature
    elif source == 'temperature':
        activeMap = Map.temperatureToHumidity
    elif source == 'humidity':
        activeMap = Map.humidityToLocation

def switchActiveMapReverse(line):
    global activeMap
    map = line[:-5].split('-to-')

def getSeedForLocation(location):
    humidity = -1
    temperature = -1
    light = -1
    water = -1
    fertilizer = -1
    soil = -1
    seed = -1

    for item in humidityToLocation:
        if item[0] <= location < item[0] + item[2]:
            humidity = location + (item[1] - item[0])
            continue
    if humidity < 0:
        humidity = location
    for item in temperatureToHumidity:
        if item[0] <= humidity < item[0] + item[2]:
            temperature = humidity + (item[1] - item[0])
            continue
    if temperature < 0:
        temperature = humidity
    for item in lightToTemperature:
        if item[0] <= temperature < item[0] + item[2]:
            light = temperature + (item[1] - item[0])
            continue
    if light < 0:
        light = temperature
    for item in waterToLight:
        if item[0] <= light < item[0] + item[2]:
            water = light + (item[1] - item[0])
            continue
    if water < 0:
        water = light
    for item in fertilizerToWater:
        if item[0] <= water < item[0] + item[2]:
            fertilizer = water + (item[1] - item[0])
            continue
    if fertilizer < 0:
        fertilizer = water
    for item in soilToFertilizer:
        if item[0] <= fertilizer < item[0] + item[2]:
            soil = fertilizer + (item[1] - item[0])
            continue
    if soil < 0:
        soil = fertilizer
    for item in seedsToSoil:
        if item[0] <= soil < item[0] + item[2]:
            seed = soil + (item[1] - item[0])
            continue
    if seed < 0:
        seed = soil
    return seed

def getLocationForSeed(seed):
    global seedsToLocationsMap
    soil = -1 
    fertilizer = -1
    water = -1
    light = -1 
    temperature = -1 
    humidity = -1
    location = -1
    for item in seedsToSoil:
        difference = item[0] - item[1]
        if item[1] <= seed < item[1] + item[2]:
            soil = seed + difference
            continue
    if soil < 0:
        soil = seed
    for item in soilToFertilizer:
        difference = item[0] - item[1]
        if item[1] <= soil < item[1] + item[2]:
            fertilizer = soil + difference
            continue
    if fertilizer < 0:
        fertilizer = soil
    for item in fertilizerToWater:
        difference = item[0] - item[1]
        if item[1] <= fertilizer < item[1] + item[2]:
            water = fertilizer + difference
            continue
    if water < 0:
        water = fertilizer
    for item in waterToLight:
        difference = item[0] - item[1]
        if item[1] <= water < item[1] + item[2]:
            light = water + difference
            continue
    if light < 0:
        light = water
    for item in lightToTemperature:
        difference = item[0] - item[1]
        if item[1] <= light < item[1] + item[2]:
            temperature = light + difference
            continue
    if temperature < 0:
        temperature = light
    for item in temperatureToHumidity:
        difference = item[0] - item[1]
        if item[1] <= temperature < item[1] + item[2]:
            humidity = temperature + difference
            continue
    if humidity < 0:
        humidity = temperature
    for item in humidityToLocation:
        difference = item[0] - item[1]
        if item[1] <= humidity < item[1] + item[2]:
            location = humidity + difference
            continue
    if location < 0:
        location = humidity
    return location

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global seeds
    
    for index, line in enumerate(lines):
        if index == 0:
            seeds = line[6:].strip().split(' ')
        elif line[0].isdigit():
            appendItemToList(line)
        elif line[0].isalpha():
            switchActiveMap(line)

    for seed in seeds:
        seedsToLocationsMap[seed] = getLocationForSeed(int(seed))
        sortedValues = sorted(seedsToLocationsMap.values())
    
    seedsToLocationsMap.clear()
    print('PART 1: Lowest Location Number Planted: ' + str(sortedValues[0]))
    # PART 1 Answer: 240320250

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    global seeds, ranges
    seedFound = False
    
    for index, line in enumerate(lines):
        if index == 0:
            seedRanges = line[6:].strip().split(' ')
            for index, value in enumerate(seedRanges):
                # this takes entirely too long
                if index % 2 == 0:
                    ranges.append((int(value), int(value) + int(seedRanges[index + 1])))
        elif line[0].isdigit():
            appendItemToList(line)
        elif line[0].isalpha():
            switchActiveMap(line)

    print('Done parsing')

    # threading did not work, after getting some help online I am going to try to start 
    # backwards and start checking locations until it gets to a seed within a range
    location = 0
    while not seedFound:
        if location % 1000000 == 0:
            print('Checking location: ' + str(location))
        seed = getSeedForLocation(location)
        if not seedFound:
            for range in ranges:
                if range[0] <= seed < range[1]:
                    seedFound = True
        location+=1

    print('Done finding seed: ' + str(seed))

    print('PART 2: Lowest Location Number Planted: ' + str(location - 1))
    # PART 2 Answer: 28580589

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 4')
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

#Source: [AdventOfCode](https://adventofcode.com/2023/day/5)
