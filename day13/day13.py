input = open('inputDay13.txt', 'r')
lines = input.read()

part1=False

def is_ordered(left, right):
    #print(f"Compare {left} vs {right}")
    for i in range(0, max(len(left), len(right))):
        if i >= len(right):
            #print("Right side ran out of items, so inputs are not in the right order")
            #print()
            return False
        if i >= len(left):
            #print("Left side ran out of items, so inputs are in the right order")
            #print()
            return True

        if type(left[i]) is int and type(right[i]) is int:
            #print(f"Compare {left[i]} vs {right[i]}")
            if left[i] > right[i]:
                #print("Right side is smaller, so inputs are not in the right order")
                #print()
                return False
            elif left[i] < right[i]:
                #print("Left side is smaller, so inputs are in the right order")
                #print()
                return True
        elif type(left[i]) is list and type(right[i]) is list:
            ordered = is_ordered(left[i], right[i])
            if ordered is not None:
                return ordered
        elif type(left[i]) is list and type(right[i]) is int:
            #print(f"Compare {left[i]} vs {right[i]}")
            #print(f"Mixed types; convert right to [{right[i]}] and retry comparison")
            ordered = is_ordered(left[i], [right[i]])
            if ordered is not None:
                return ordered
        elif type(left[i]) is int and type(right[i]) is list:
            #print(f"Compare {left[i]} vs {right[i]}")
            #print(f"Mixed types; convert left to [{left[i]}] and retry comparison")
            ordered = is_ordered([left[i]], right[i])
            if ordered is not None:
                return ordered
    return None

total = 0
allSignals = [[[2]],[[6]]]
index = 1

lines = lines.split('\n\n')
for line in lines:
    lAndR = line.split('\n')
    leftArr = eval(lAndR[0])
    rightArr = eval(lAndR[1])
    if part1:
        #print(f"== Pair {index} ==")
        ordered = is_ordered(leftArr, rightArr)
        if ordered is not None and ordered is True:
            total += index

        index += 1
    else:
        allSignals.append(leftArr)
        allSignals.append(rightArr)

#Insertion Sort
orderedSignals = []
for step in range(1, len(allSignals)):
    key = allSignals[step]
    j = step - 1
    
    while j >= 0 and is_ordered(key, allSignals[j]):
        allSignals[j + 1] = allSignals[j]
        j = j - 1

    allSignals[j + 1] = key

twoIndex = 0
sixIndex = 0
for (index, sign) in enumerate(allSignals):
    if sign == [[2]]:
        twoIndex = index + 1
    elif sign == [[6]]:
        sixIndex = index + 1

if part1:
    print("Part One Answer:", total) #5682
else:
    print("Part Two Answer:", twoIndex * sixIndex)

