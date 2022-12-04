input = open('inputDay4.txt', 'r')
lines = input.readlines()

fullyContainCounter = 0
overlapCounter = 0

for line in lines:
    line = line.replace("\n", "")
    assignments = line.split(",")
    first = assignments[0].split("-")
    first[0] = int(first[0])
    first[1] = int(first[1])
    second = assignments[1].split("-")
    second[0] = int(second[0])
    second[1] = int(second[1])

    #Part 1
    if (first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1]):
        fullyContainCounter += 1
        overlapCounter += 1
    #Part 2
    elif (first[0] >= second[0] and first[0] <= second[1]) or (first[1] >= second[0] and first[1] <= second[1]):
        overlapCounter += 1
    elif (second[0] >= first[0] and second[0] <= first[1]) or (second[1] >= first[0] and second[1] <= first[1]):
        overlapCounter += 1

print("Part One Counter: " + str(fullyContainCounter)) #431
print("Part Two Counter: " + str(overlapCounter)) #823