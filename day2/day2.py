# A - Rock A > C - A > Z
# B - Paper B > A - B > X
# C - Scissors C > B - C > Y

# X - Rock - 1
# Y - Paper - 2
# Z - Scissors - 3
myPick = {}
myPick['X'] = 1
myPick['Y'] = 2
myPick['Z'] = 3

points = 0

# loss - 0
# tie - 3
# win - 6

# NOW X - need to lose
# Y - needs to draw
# Z - needs to win
results = {}
results['X'] = 0
results['Y'] = 3
results['Z'] = 6

def determinePoints(elf, myPick):
    if elf == 'A':
        if myPick == 'X':
            return 3
        elif myPick == 'Y':
            return 6
        elif myPick == 'Z':
            return 0
    elif elf == 'B':
        if myPick == 'X':
            return 0
        elif myPick == 'Y':
            return 3
        elif myPick == 'Z':
            return 6
    elif elf == 'C':
        if myPick == 'X':
            return 6
        elif myPick == 'Y':
            return 0
        elif myPick == 'Z':
            return 3


# A - Rock A > C - A > Z
# B - Paper B > A - B > X
# C - Scissors C > B - C > Y

# X - Rock - 1
# Y - Paper - 2
# Z - Scissors - 3

# NOW X - need to lose
# Y - needs to draw
# Z - needs to win
def determinePick(elf, outcome):
    if elf == 'A':
        if outcome == 'X':
            return 'Z'
        elif outcome == 'Y':
            return 'X'
        elif outcome == 'Z':
            return 'Y'
    elif elf == 'B':
        if outcome == 'X':
            return 'X'
        elif outcome == 'Y':
            return 'Y'
        elif outcome == 'Z':
            return 'Z'
    elif elf == 'C':
        if outcome == 'X':
            return 'Y'
        elif outcome == 'Y':
            return 'Z'
        elif outcome == 'Z':
            return 'X'

input = open('inputDay2.txt', 'r')
lines = input.readlines()

#part 1
#for line in lines:
    # line[0] is elf
    # line[2] is me
#    points = points + myPick[line[2]]
#    points = points + determinePoints(line[0], line[2])

#part 2
for line in lines:
    # line[0] is elf
    # line[2] is outcome
    points = points + myPick[determinePick(line[0], line[2])]
    points = points + results[line[2]]
    
print("Total Number of Points: " + str(points)) # correct is 14827

#Source: [AdventOfCode](https://adventofcode.com/2022/day/2)