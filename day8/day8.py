input = open('inputDay8.txt', 'r')
lines = input.readlines()

tempArray = []
twoDArray = []
horizDict = {}
vertDict = {}
countVisible = 0
highestScenicScore = 0
part1 = False

def visible(num, list):
    smallest = True
    for number in list:
        if num <= number:
            smallest = False
            break
    return smallest

def scenicScore(num, list):
    count = 0
    for number in list:
        count += 1
        if num <= number:
            break
    return count

index = 0
for line in lines:
    for i in range(0, len(line)):
        if line[i] != '\n':
            numberToAdd = int(line[i])
            if i in vertDict:
                vertDict[i].append(numberToAdd)
            else:
                vertDict[i] = [numberToAdd]
            if index in horizDict:
                horizDict[index].append(numberToAdd)
            else:
                horizDict[index] = [numberToAdd]
            tempArray.append(numberToAdd)
        else:
            twoDArray.append(tempArray)
            tempArray = []
    index += 1

for x in range(0, len(twoDArray)): # left to right
    for y in range(0, len(twoDArray[x])): # top to bottom
        if x == 0 or y == 0 or x == len(twoDArray) - 1 or y == len(twoDArray[x]) - 1:
            countVisible += 1
        else:
            tree = twoDArray[x][y]

            leftOfTree = horizDict[x][:y]
            rightOfTree = horizDict[x][(y+1):]
            topOfTree = vertDict[y][:x]
            bottomOfTree = vertDict[y][(x+1):]

            if part1:
                left = visible(tree, leftOfTree)
                right = visible(tree, rightOfTree)
                top = visible(tree, topOfTree)
                bottom = visible(tree, bottomOfTree)

                if left or right or top or bottom:
                    countVisible += 1
            else:
                # Need to reverse left of tree and top of tree so that the order they are evaluated is tree out
                leftOfTreeReversed = leftOfTree[::-1]
                topOfTreeReversed = topOfTree[::-1]
                left = scenicScore(tree, leftOfTreeReversed)
                right = scenicScore(tree, rightOfTree)
                top = scenicScore(tree, topOfTreeReversed)
                bottom = scenicScore(tree, bottomOfTree)

                score = left * right * top * bottom
                if score > highestScenicScore:
                    highestScenicScore = score

if part1:
    print("Part One Answer: " + str(countVisible)) #1807
else:
    print("Part Two Answer: " + str(highestScenicScore)) #480000

#Source: [AdventOfCode](https://adventofcode.com/2022/day/8)