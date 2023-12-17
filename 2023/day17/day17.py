#!/usr/bin/env python3

import argparse
import time
import heapq
import sys
from collections import defaultdict
from typing import NamedTuple, Iterator
from typing_extensions import Self

# fields
class Direction(NamedTuple):
    dx: int
    dy: int

east = Direction(1, 0)
west = Direction(-1, 0)
north = Direction(0, 1)
south = Direction(0, -1)

allDirections = [east, west, north, south]

class Position(NamedTuple):
    x: int
    y: int
    direction: Direction # direction of the last move
    run: int # number of moves in the same direction

    def neighbors(self, width: int, height: int) -> Iterator[Self]:
        # Iterators are objects that allow you to traverse through all the elements of a collection and return one element at a time.
        excludedDirections = [Direction(-self.direction.dx, -self.direction.dy)] # cannot go back
        if self.run == 3: # cannot move more that 3 times in the same direction
            excludedDirections.append(self.direction)
        for direction in allDirections.copy():
            if direction not in excludedDirections:
                yield from self._new_position(direction, width, height) # get the next position

    # ON YIELD -> When you use a function with a return value, every time you call the function, 
    # it starts with a new set of variables. In contrast, if you use a generator function instead 
    # of a normal function, the execution will start right from where it left last.

    def _new_position(self, direction: Direction, width: int, height: int) -> Iterator[Self]:
        run = self.run + 1 if direction == self.direction else 1 # if the direction is the same, increment the run, else set it to 1
        x = self.x + direction.dx
        y = self.y + direction.dy
        if 0 <= x < width and 0 <= y < height: # only yield the next value if the new position is within the map
            yield self.__class__(x, y, direction, run) # has to be self.__class__ because we use it for UltraPosition as well

    @property
    def min_run(self) -> int:
        return 0 # used in dijkstra to check that we have at least gone 0 moves (more relevant for Part 2)

class UltraPosition(Position): # subclasses Position
    def neighbors(self, width: int, height: int) -> Iterator[Self]:
        directions = allDirections.copy()
        excludedDirections = [Direction(-self.direction.dx, -self.direction.dy)] # cannot go back
        if self.run == 10: # cannot move more that 10 times in the same direction
            excludedDirections.append(self.direction)
        if 1 <= self.run < 4:
            directions = [self.direction] # if we have gone 1-3 times in the same direction, we can only go in that direction
        for direction in directions:
            if direction not in excludedDirections:
                yield from self._new_position(direction, width, height)
    
    @property
    def min_run(self) -> int:
        return 4 # used in dijkstra to check that we have at least gone 4 moves

# helper functions
def dijkstra(inputMap: list[list[int]], start: Position) -> int:
    width = len(inputMap[0]) # used to determine if the position is within the map
    height = len(inputMap) # used to determine if the position is within the map
    goal = width - 1, height - 1 # gets the location of the desired destination
    priority_queue = [(0, start, [])] # priority queue is a list of tuples (heat_loss, position, path)
    total_heat_loss_map = defaultdict(lambda: float('infinity'))
    while priority_queue: # while the queue is not empty
        heat_loss, position, path = heapq.heappop(priority_queue)
        if (position.x, position.y) == goal and position.run >= position.min_run:
            # if we have reached the goal and we have gone at least the minimum number of moves, we return
            return heat_loss
        for newPosition in position.neighbors(width, height): # get all the neighbors of the position
            new_heat_loss = heat_loss + inputMap[newPosition.y][newPosition.x]
            # new heat loss is equal to the current heat loss plus the heat loss of the new position
            if new_heat_loss < total_heat_loss_map[newPosition]:
                # we only want to contine if the new heat loss is less than the total heat loss of the new position (which is infinity unless it has been set)
                total_heat_loss_map[newPosition] = new_heat_loss
                heapq.heappush(priority_queue, (new_heat_loss, newPosition, path + [position])) # push the new value onto the queue

def part1(filename: str):
    input = open(filename, 'r')
    lines = input.readlines()

    heatLossMap = list(list(map(int, line.rstrip('\n'))) for line in lines) # rstrip removes the listed characters from the right side of the string
    # makes a map that looks like the following
    # [
    #     [2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3], 
    #     [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3], 
    #     [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4], 
    #     [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2], 
    #     [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6], 
    #     [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4], 
    #     [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6], 
    #     [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3], 
    #     [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7], 
    #     [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3], 
    #     [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3], 
    #     [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5], 
    #     [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3]
    # ]

        
    print('PART 1: Least Heat Loss:', dijkstra(heatLossMap, Position(0, 0, east, 0)))
    # PART 1 Answer: 665

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()

    heatLossMap = list(list(map(int, line.rstrip('\n'))) for line in lines)

    print('PART 2: Ultra Least Heat Loss:', dijkstra(heatLossMap, UltraPosition(0, 0, east, 0)))
    # PART 2 Answer: 809

def test():
    test1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]
    ]
    assert(71 == dijkstra(test1, UltraPosition(0, 0, east, 0)))

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2023 Day 17')
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

# Source: [AdventOfCode](https://adventofcode.com/2023/day/17)

# ALMOST ENTIRELY COPIED FROM janek37 on GitHub in his solution [here](https://github.com/janek37/advent-of-code/blob/main/2023/day17.py), for learngin purposes only.