from enum import Enum

# helper functions
def getFileName(part):
    if activePart == Part.test1:
        return 'testInput.txt'
    elif activePart == Part.test2:
        return 'testInput2.txt'
    else:
        return 'inputFile.txt'

class Part(Enum):
    test1=0
    test2=1
    part1=2
    part2=3
    bothParts=4

# CHANGE THIS IF NEEDED
activePart = Part.bothParts

# SOLUTION
input = open(getFileName(activePart), 'r')
lines = input.readlines()

# SOLUTION HELPER FUNCTIONS
def getLimit(color):
    if color == Color.red:
        return 12
    elif color == Color.blue:
        return 14
    elif color == Color.green:
        return 13

redsBluesGreens = {'red': 0, 'blue': 0, 'green': 0}

def checkIfColorsFail(dict):
    for color in Color:
        if dict[color.value] > getLimit(color):
            return True
    return False

def checkColorsPassed(gameResult, redsBluesGreens):
    for color in gameResult:
        numberAndColor = color.strip().split(' ')
        redsBluesGreens[numberAndColor[1]] = int(numberAndColor[0])
    if not checkIfColorsFail(redsBluesGreens):
        return True
    return False

def getMaxColors(gameResult, maxColors):
    for color in gameResult:
        numberAndColor = color.strip().split(' ')
        if int(numberAndColor[0]) > maxColors[numberAndColor[1]]:
            maxColors[numberAndColor[1]] = int(numberAndColor[0])

def getMaxColorPower(maxColors):
    maxColorPower = 1
    for key, value in maxColors.items():
        if value > 0:
            maxColorPower *= value
    return maxColorPower

class Color(Enum):
    red = 'red'
    blue = 'blue'
    green = 'green'

sumOfGameIds = 0
gameWasPossible = False

# PART 1
if activePart != Part.part2:
    for line in lines:
        line = line.strip().replace('\n', '')
        gameIDAndGameResults = line.split(':')
        gameID = int(gameIDAndGameResults[0][4:]) # Crops off 'Game' and the space
        
        gameResults = gameIDAndGameResults[1].strip().split(';')

        for result in gameResults:
            result = result.strip()
            if ',' in result:
                colors = result.split(', ')
            else:
                colors = [result]
            gameWasPossible = checkColorsPassed(colors, redsBluesGreens)
            redsBluesGreens = {'red': 0, 'blue': 0, 'green': 0}
            if not gameWasPossible:
                break
 
        if gameWasPossible:
            sumOfGameIds += gameID
            gameWasPossible = False
    
    print("PART 1: Sum of all of the gameIds: " + str(sumOfGameIds))
    # PART 1 Answer: 2727

# PART 2
maxColors = {'red': 0, 'blue': 0, 'green': 0}
sumOfPowers = 0

if activePart != Part.part1:
    for line in lines:
        line = line.strip().replace('\n', '')
        gameIDAndGameResults = line.split(':')
        
        gameResults = gameIDAndGameResults[1].strip().split(';')

        for result in gameResults:
            result = result.strip()
            if ',' in result:
                colors = result.split(', ')
            else:
                colors = [result]
            gameWasPossible = getMaxColors(colors, maxColors)
        sumOfPowers += getMaxColorPower(maxColors)
        maxColors = {'red': 0, 'blue': 0, 'green': 0}

    print("PART 2: Sum of all of the gameIds: " + str(sumOfPowers))
    # PART 2 Answer: 56580 

#Source: [AdventOfCode](https://adventofcode.com/2023/day/2)