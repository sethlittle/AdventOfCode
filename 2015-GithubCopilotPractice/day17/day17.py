# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

# --- Part Two ---
# While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

# In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

def getMinContainers(containers, target):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')
    if len(containers) == 0:
        return float('inf')
    minContainers = float('inf')
    for i in range(len(containers)):
        container = containers[i]
        newtarget = target - container
        newcontainers = containers[i+1:]
        newminContainers = getMinContainers(newcontainers, newtarget)
        if newminContainers < minContainers:
            minContainers = newminContainers
    return minContainers + 1

def getuniquecombos(containers, target):
    if target == 0:
        return [[]]
    if target < 0:
        return []
    if len(containers) == 0:
        return []
    combos = []
    for i in range(len(containers)):
        container = containers[i]
        newtarget = target - container
        newcontainers = containers[i+1:]
        newcombos = getuniquecombos(newcontainers, newtarget)
        for combo in newcombos:
            combo.append(container)
        combos.extend(newcombos)
    return combos

def part2(containers, target):
    minContainers = getMinContainers(containers, target)
    combos = getuniquecombos(containers, target)
    combos = [combo for combo in combos if len(combo) == minContainers]
    return len(combos)

def main():
    containers = []
    with open('input.txt', 'r') as f:
        for line in f:
            containers.append(int(line))
    # containers = [20, 15, 10, 5, 5]
    target = 150
    combos = getuniquecombos(containers, target)
    print(len(combos))
    print(part2(containers, target))

if __name__ == '__main__':
    main()

# SOLUTION:
# Part 1: 1638
# Part 2: 17

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/17