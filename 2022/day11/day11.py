class Monkey:
    def __init__(self, number, items, operation, operationAmount, testAmount, trueThrowTo, falseThrowTo):
        self.number = number
        self.items = items
        self.operation = operation
        self.operationAmount = operationAmount
        self.testAmount = testAmount
        self.trueThrowTo = trueThrowTo
        self.falseThrowTo = falseThrowTo
        self.numberOfInspections = 0
    
    def __str__(self):
        return f"ID: {self.number}\nItems: {self.items}\noperation: {self.operation}\noperationAmount: {self.operationAmount}\ntestAmount: {self.testAmount}\nTrue Throw: {self.trueThrowTo}\nFalse Throw: {self.falseThrowTo}"

monkeys = {}
mostInspections = 0
secondMostInspections = 0
part1 = False

def inspectElement(worryLevel, operation, operationAmount, divisor):
    worryLevel = int(worryLevel)
    if operation == "*":
        if operationAmount == "old":
            worryLevel = worryLevel * worryLevel
        else:
            worryLevel = worryLevel * int(operationAmount) 
    elif operation == "+":
        if operationAmount == "old":
            worryLevel = worryLevel + worryLevel
        else:
            worryLevel = worryLevel + int(operationAmount) 
    if part1:
        worryLevel = worryLevel // divisor
    else:
        worryLevel = worryLevel % divisor
    return worryLevel

#Create map
with open('inputDay11.txt', 'r+') as input:
    for line in input:
        line = line.strip().replace("\n", "")
        lines = line.replace(":", "").split(" ")
        if line.startswith("Monkey "):
            number = int(lines[1])

            items = next(input).strip().replace("\n", "").replace("Starting items: ", "").replace(" ", "").split(",")

            operations = next(input).strip().replace("\n", "").replace("Operation: new = old ", "").split(" ")
            operation = operations[0]
            operationAmount = operations[1]

            testAmount = next(input).strip().replace("\n", "")
            testAmount = int(testAmount.replace("Test: divisible by ", ""))

            trueThrowTo = next(input).strip().replace("\n", "")
            trueThrowTo = int(trueThrowTo.replace("If true: throw to monkey ", ""))

            falseThrowTo = next(input).strip().replace("\n", "")
            falseThrowTo = int(falseThrowTo.replace("If false: throw to monkey ", ""))

            monkey = Monkey(number, items, operation, operationAmount, testAmount, trueThrowTo, falseThrowTo)
            monkeys[monkey.number] = monkey

# all monkeys here is a round
def performRounds(rounds, divisor):
    for i in range(0, rounds):
        for monkey in monkeys.values():
            for item in monkey.items:
                monkey.numberOfInspections += 1
                if divisor == 0:
                    divisor = 1
                    for monkeyDivisors in monkeys.values():
                        divisor *= monkeyDivisors.testAmount
                worryLevel = inspectElement(item, monkey.operation, monkey.operationAmount, divisor)
                if worryLevel % monkey.testAmount == 0:
                    monkeys[monkey.trueThrowTo].items.append(str(worryLevel))
                else:
                    monkeys[monkey.falseThrowTo].items.append(str(worryLevel))
            monkey.items = []

if part1:
    performRounds(20, 3)
else:
    performRounds(10000, 9699690)

for monkey in monkeys.values():
    # print(f"Monkey {monkey.number}:", monkey.items)
    if monkey.numberOfInspections > mostInspections:
        secondMostInspections = mostInspections
        mostInspections = monkey.numberOfInspections
    elif monkey.numberOfInspections > secondMostInspections:
        secondMostInspections = monkey.numberOfInspections
    # print(f"Monkey {monkey.number} inspected items {monkey.numberOfInspections} times.")

if part1:
    print("Part One Answer:", mostInspections * secondMostInspections) #90294
else:
    print("Part Two Answer:", mostInspections * secondMostInspections) #18170818354
