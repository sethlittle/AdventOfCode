# --- Day 15: Science for Hungry People ---

# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

def part1(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    ingredients = {}
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(' ')
        ingredients[line[0].replace(':', '')] = {
            'capacity': int(line[2].replace(',', '')),
            'durability': int(line[4].replace(',', '')),
            'flavor': int(line[6].replace(',', '')),
            'texture': int(line[8].replace(',', '')),
            'calories': int(line[10].replace(',', ''))
        }
    # print(ingredients)
    maxScore = 0
    for i in range(0, 101):
        for j in range(0, 101 - i):
            for k in range(0, 101 - i - j):
                for l in range(0, 101 - i - j - k):
                    if i + j + k + l == 100:
                        # print(i, j, k, l)
                        capacity = ingredients['Sprinkles']['capacity'] * i + ingredients['Butterscotch']['capacity'] * j + ingredients['Chocolate']['capacity'] * k + ingredients['Candy']['capacity'] * l
                        durability = ingredients['Sprinkles']['durability'] * i + ingredients['Butterscotch']['durability'] * j + ingredients['Chocolate']['durability'] * k + ingredients['Candy']['durability'] * l
                        flavor = ingredients['Sprinkles']['flavor'] * i + ingredients['Butterscotch']['flavor'] * j + ingredients['Chocolate']['flavor'] * k + ingredients['Candy']['flavor'] * l
                        texture = ingredients['Sprinkles']['texture'] * i + ingredients['Butterscotch']['texture'] * j + ingredients['Chocolate']['texture'] * k + ingredients['Candy']['texture'] * l
                        if capacity < 0:
                            capacity = 0
                        if durability < 0:
                            durability = 0
                        if flavor < 0:
                            flavor = 0
                        if texture < 0:
                            texture = 0
                        score = capacity * durability * flavor * texture
                        if score > maxScore:
                            maxScore = score
    print(maxScore)

# --- Part Two ---
# Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

def part2(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    ingredients = {}
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(' ')
        ingredients[line[0].replace(':', '')] = {
            'capacity': int(line[2].replace(',', '')),
            'durability': int(line[4].replace(',', '')),
            'flavor': int(line[6].replace(',', '')),
            'texture': int(line[8].replace(',', '')),
            'calories': int(line[10].replace(',', ''))
        }
    maxScore = 0
    for i in range(0, 101):
        for j in range(0, 101 - i):
            for k in range(0, 101 - i - j):
                for l in range(0, 101 - i - j - k):
                    if i + j + k + l == 100:
                        # print(i, j, k, l)
                        capacity = ingredients['Sprinkles']['capacity'] * i + ingredients['Butterscotch']['capacity'] * j + ingredients['Chocolate']['capacity'] * k + ingredients['Candy']['capacity'] * l
                        durability = ingredients['Sprinkles']['durability'] * i + ingredients['Butterscotch']['durability'] * j + ingredients['Chocolate']['durability'] * k + ingredients['Candy']['durability'] * l
                        flavor = ingredients['Sprinkles']['flavor'] * i + ingredients['Butterscotch']['flavor'] * j + ingredients['Chocolate']['flavor'] * k + ingredients['Candy']['flavor'] * l
                        texture = ingredients['Sprinkles']['texture'] * i + ingredients['Butterscotch']['texture'] * j + ingredients['Chocolate']['texture'] * k + ingredients['Candy']['texture'] * l
                        calories = ingredients['Sprinkles']['calories'] * i + ingredients['Butterscotch']['calories'] * j + ingredients['Chocolate']['calories'] * k + ingredients['Candy']['calories'] * l
                        if calories == 500:
                            if capacity < 0:
                                capacity = 0
                            if durability < 0:
                                durability = 0
                            if flavor < 0:
                                flavor = 0
                            if texture < 0:
                                texture = 0
                            score = capacity * durability * flavor * texture
                            if score > maxScore:
                                maxScore = score
    print(maxScore)

def main():
    part1('input.txt')
    part2('input.txt')

if __name__ == "__main__":
    main()

# SOLUTION:
# Part 1: 21367368
# Part 2: 1766400

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/15