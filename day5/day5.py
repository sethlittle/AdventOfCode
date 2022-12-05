input = open('inputDay5.txt', 'r')
lines = input.readlines()

# count, from, to
instructions = [0, 0, 0]
result = ''
part1 = False
elementsToBeMoved = []

def parseLine(stringLine):
    line = stringLine.replace("\n", "")
    line = line.replace(" ", "")
    line = line.replace("move", "")
    lines = line.split("from", 1)
    instructions[0] = int(lines[0])
    fromToLines = lines[1].split("to", 1)
    instructions[1] = fromToLines[0]
    instructions[2] = fromToLines[1]

entriesEntered = False
stackDict = {}

#initiate stackDict to be an empty list at each element "1" - "9"
for i in range(1, 10):
    stackDict[str(i)] = []

for line in lines:
    if entriesEntered != True:
        if line == '\n':
            entriesEntered = True
        else:
            if line[1] != " " and line[1] != "1":
                stackDict["1"].insert(0, line[1])
            if line[5] != " " and line[5] != "2":
                stackDict["2"].insert(0, line[5])
            if line[9] != " " and line[9] != "3":
                stackDict["3"].insert(0, line[9])
            if line[13] != " " and line[13] != "4":
                stackDict["4"].insert(0, line[13])
            if line[17] != " " and line[17] != "5":
                stackDict["5"].insert(0, line[17])
            if line[21] != " " and line[21] != "6":
                stackDict["6"].insert(0, line[21])
            if line[25] != " " and line[25] != "7":
                stackDict["7"].insert(0, line[25])
            if line[29] != " " and line[29] != "8":
                stackDict["8"].insert(0, line[29])
            if line[33] != " " and line[33] != "9":
                stackDict["9"].insert(0, line[33])
    else:
        parseLine(line)
        if part1: 
            for i in range(0, instructions[0]):
                element = stackDict[instructions[1]].pop()
                stackDict[instructions[2]].append(element)
        else:
            for i in range(0, instructions[0]):
                elementsToBeMoved.insert(0, stackDict[instructions[1]].pop())
            for element in elementsToBeMoved:
                stackDict[instructions[2]].append(element)
            elementsToBeMoved = []

for i in range(1, 10):
    result = result + stackDict[str(i)].pop()

if part1:   
    print("Part one answer: " + result) #ZSQVCCJLL
else:
    print("Part two answer: " + result) #QZFJRWHGS


