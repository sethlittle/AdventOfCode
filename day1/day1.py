elfCals = []
largestCals = 0

input = open('inputFile.txt', 'r')
lines = input.readlines()

counter = 0
for line in lines:
    if line != '\n':
        counter += int(line)
    else:
        elfCals.append(counter)
        if largestCals < counter:
            largestCals = counter
        counter = 0

topCal = 0
secondCal = 0
thirdCal = 0
for cal in elfCals:
    if cal >= topCal:
        temp = topCal
        temp2 = secondCal
        topCal = cal
        secondCal = temp
        thirdCal = temp2
    elif cal >= secondCal:
        temp3 = secondCal
        secondCal = cal
        thirdCal = temp3
    elif cal >= thirdCal:
        thirdCal = cal

print("Highest Calories: " + str(topCal))
print("Second Most Calories: " + str(secondCal))
print("Third Most Calories: " + str(thirdCal))

topThreeCals = topCal + secondCal + thirdCal
print("Top Three Calories Combined: " + str(topThreeCals))
