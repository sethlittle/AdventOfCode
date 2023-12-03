# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

# SOLUTION
def getHousesVisited(directions):
    housesVisited = set()
    x = 0
    y = 0
    housesVisited.add((x, y))
    for direction in directions:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        housesVisited.add((x, y))
    return housesVisited

# TESTS
def testPart1():
    assert len(getHousesVisited('>')) == 2
    assert len(getHousesVisited('^>v<')) == 4
    assert len(getHousesVisited('^v^v^v^v^v')) == 2

# MAIN
def mainPart1():
    testPart1()
    input = open('inputFile.txt', 'r')
    directions = input.read()
    print('Houses visited: ' + str(len(getHousesVisited(directions))))

# SOLUTION
# Houses visited: 2081

# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

# SOLUTION
def getHousesVisitedBySantaAndRoboSanta(directions):
    housesVisited = set()
    santaX = 0
    santaY = 0
    roboSantaX = 0
    roboSantaY = 0
    housesVisited.add((santaX, santaY))
    housesVisited.add((roboSantaX, roboSantaY))
    for i in range(len(directions)):
        if i % 2 == 0:
            if directions[i] == '^':
                santaY += 1
            elif directions[i] == 'v':
                santaY -= 1
            elif directions[i] == '>':
                santaX += 1
            elif directions[i] == '<':
                santaX -= 1
            housesVisited.add((santaX, santaY))
        else:
            if directions[i] == '^':
                roboSantaY += 1
            elif directions[i] == 'v':
                roboSantaY -= 1
            elif directions[i] == '>':
                roboSantaX += 1
            elif directions[i] == '<':
                roboSantaX -= 1
            housesVisited.add((roboSantaX, roboSantaY))
    return housesVisited

# TESTS
def test():
    assert len(getHousesVisitedBySantaAndRoboSanta('^v')) == 3
    assert len(getHousesVisitedBySantaAndRoboSanta('^>v<')) == 3
    assert len(getHousesVisitedBySantaAndRoboSanta('^v^v^v^v^v')) == 11

# MAIN
def main():
    test()
    input = open('inputFile.txt', 'r')
    directions = input.read()
    print('Houses visited by Santa and Robo-Santa: ' + str(len(getHousesVisitedBySantaAndRoboSanta(directions))))

if __name__ == '__main__':
    mainPart1()
    main()

# SOLUTION
# Houses visited by Santa and Robo-Santa: 2341

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/3
