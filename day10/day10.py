import numpy as np

input = open('inputDay10.txt', 'r')
lines = input.readlines()

cycle = 1

X = 1 # middle sprite position

CRTarr = [
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]    
]

buffer = 0
totalSum = 0
charToDraw = '.'

def drawPixel():
    global X, cycle, CRTarr, charToDraw
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    if col == X-1 or col == X or col == X+1:
        charToDraw = '#'
    else:
        charToDraw = '.'
    CRTarr[row][col] = charToDraw

def noopCycle():
    global X, buffer, cycle
    drawPixel()
    X += buffer
    buffer = 0
    cycle += 1

def addxCycle(value):
    global X, buffer, cycle
    drawPixel()
    X += buffer
    buffer = value
    cycle += 1

stops = [20, 60, 100, 140, 180, 220]

for line in lines:
    line = line.replace("\n", "")
    if line != "noop":
        line = line.split(" ")
        addxCycle(int(line[1]))
        if cycle in stops:
            totalSum += (cycle * X)
        noopCycle()
    else:
        noopCycle()
    if cycle in stops:
        totalSum += (cycle * X)

print("Part One Answer:", totalSum) #15880

print("Part Two Answer - The following 8 letters")
for r in CRTarr:
   for c in r:
      print(c,end = " ")
   print()

#Source: [AdventOfCode](https://adventofcode.com/2022/day/10)