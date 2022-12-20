import numpy as np

input = open('inputDay14.txt', 'r')
lines = input.readlines()

GRIDOFFSET = 750
rockPaths = []
sandPourLocation = (500, 0) #(width, height)
maxHeight, minHeight, minWidth, maxWidth = 0, 0, 0, 0
gridHeight, gridWidth = 0,0
stillPouring = False
unitsOfSandFallen = 0
part1 = False

def findMaxAndMin():
    global maxHeight, minHeight, minWidth, maxWidth
    rockPaths.append([sandPourLocation])
    for paths in rockPaths:
        for location in paths:
            if location[0] > maxWidth:
                maxWidth = location[0]
            elif location[0] < minWidth or minWidth == 0:
                minWidth = location[0]
            
            if location[1] > maxHeight:
                maxHeight = location[1]
            elif location[1] < minHeight or minHeight == 0:
                minHeight = location[1]
    rockPaths.pop()

def drawRocks(pointA, pointB):
    minusMult = 1

    if pointA[0] == pointB[0]: # vert path
        if pointA[1] - pointB[1] > 0:
            minusMult = -1
        for i in range(0, abs(pointA[1] - pointB[1]) + 1): 
            grid[(pointA[1] + (i * minusMult) - minHeight)][(pointA[0] - minWidth) + GRIDOFFSET] = '#'
    elif pointA[1] == pointB[1]: # horizontal path
        if pointA[0] - pointB[0] > 0:
            minusMult = -1
        for i in range(0, abs(pointA[0] - pointB[0]) + 1):
            grid[(pointA[1] - minHeight)][(pointA[0] - minWidth + (i * minusMult)) + GRIDOFFSET] = '#'
            
for line in lines:
    rockPathsDirection = []
    line = line.replace("\n", "")
    rockPath = line.split(" -> ")
    for rockWall in rockPath:
        rockWallInfo = rockWall.split(",")
        rockPathsDirection.append((int(rockWallInfo[0]), int(rockWallInfo[1])))
    rockPaths.append(rockPathsDirection)

findMaxAndMin()
gridHeight = (maxHeight - minHeight) + 2
gridWidth = (maxWidth - minWidth) + 1500
grid = np.full((gridHeight + 1, gridWidth + 1), '.', dtype='U1')

def printGrid():
    for c in grid:
        for r in c:
            print(r, end=" ")
        print()
    print()

def pourSand():
    global stillPouring, unitsOfSandFallen
    try:
        if grid[((sandPourLocation[1] - minHeight))][((sandPourLocation[0] - minWidth)) + GRIDOFFSET] == "O":
            stillPouring = False
        blocked = False
        i = 0
        j = 0

        while not blocked:
            if grid[((sandPourLocation[1] - minHeight) + i + 1)][((sandPourLocation[0] - minWidth) + j) + GRIDOFFSET] == ".":
                i = i + 1
            else:
                if grid[((sandPourLocation[1] - minHeight) + i + 1)][((sandPourLocation[0] - minWidth) + j - 1) + GRIDOFFSET] == ".":
                    i = i + 1
                    j = j - 1
                else:
                    if grid[((sandPourLocation[1] - minHeight) + i + 1)][((sandPourLocation[0] - minWidth) + j + 1) + GRIDOFFSET] == ".":
                        i = i + 1
                        j = j + 1
                    else:
                        grid[((sandPourLocation[1] - minHeight) + i)][((sandPourLocation[0] - minWidth) + j) + GRIDOFFSET] = "O"
                        blocked = True
                        unitsOfSandFallen += 1
    except IndexError:
        # Index out of bounds means the last one has been set
        stillPouring = False

def drawBottomLine():
    bottomHeight = maxHeight + 2
    for i in range(0, abs(maxWidth - minWidth) + 1500 + 1):
        grid[bottomHeight][i] = "#"

for path in rockPaths:
    for (index, point) in enumerate(path):
        if index < len(path) - 1:
            drawRocks(path[index], path[index+1])

if not part1:
    drawBottomLine()

# start sand pour
stillPouring = True
while stillPouring:
    pourSand()
    # printGrid()

if part1:
    print("Part One Answer:", unitsOfSandFallen) # 862
else:
    print("Part Two Answer:", unitsOfSandFallen - 1) # 28744
