input = open('inputDay3.txt', 'r')
lines = input.readlines()

dupChar = ''
value = 0
totalSum = 0
badgeSum = 0
lineCount = 0

def getValueFor(character):
    asciiVal = ord(character)
    if asciiVal >= 97: #a-z
        return asciiVal - 96
    else: #A-Z
        return asciiVal - 38

for line in lines:
    # line length is len(line) - 1 because each line ends with the \n character
    # line length / 2 is each compartment size
    # first part - line[:((len(line) - 1)//2)]
    # second part - line[((len(line) - 1)//2):]

    for char in line[:((len(line) - 1)//2)]:
        if char in line[((len(line) - 1)//2):]:
            dupChar = char
            break

    totalSum += getValueFor(dupChar) 
    lineCount += 1

print("Final sum part 1: " + str(totalSum)) #7878

tempLines = []

for line in lines:
    stringToAppend = line.replace("\n", "")
    tempLines.append(stringToAppend)
    if len(tempLines) == 3:
        for char in tempLines[0]:
            if char in tempLines[1] and char in tempLines[2]:
                badgeSum += getValueFor(char)
                break
        tempLines.clear()

print("Final sum part 2: " + str(badgeSum)) #2760