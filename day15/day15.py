import re

from z3 import If, Int, Solver

# helped via [this repo](https://github.com/fuglede/adventofcode/blob/master/2022/day15/solutions.py) on this file to make the code much much neater and to learn the algo

with open('inputDay15.txt') as f:
    ls = f.read().strip().split("\n")

inputs = [list(map(int, re.findall("-?\d+", x))) for x in ls]

# gets manhattan distance https://en.wikipedia.org/wiki/Taxicab_geometry
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

beacons = set()
cannotContainBeacon = set()
targetY = 2000000

for info in inputs:
    sensor = (info[0], info[1])
    beacon = (info[2], info[3])
    beacons.add(beacon)
    distance = manhattan(sensor, beacon)
    length = distance - abs(sensor[1] - targetY)
    # |= is a union on sets
    cannotContainBeacon |= set((x, targetY) for x in range(sensor[0] - length, sensor[0] + length + 1))

print("Part One Answer:", len(cannotContainBeacon - beacons)) #5403290

#part 2
def z3AbsoluteVal(x):
    return If(x >= 0, x, -x)

s = Solver()
x = Int("x")
y = Int("y")
s.add(x >= 0)
s.add(x <= (2*targetY))
s.add(y >= 0)
s.add(y <= (2*targetY))

for info in inputs:
    sensor = (info[0], info[1])
    beacon = (info[2], info[3])
    distance = manhattan(sensor, beacon)
    s.add((z3AbsoluteVal(x - sensor[0]) + z3AbsoluteVal(y - sensor[1])) > distance)

s.check()
model = s.model()
print("Part Two Answer:", model[x].as_long() * 4000000 + model[y].as_long()) #10291582906626