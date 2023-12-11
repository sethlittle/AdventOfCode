# --- Day 10: Elves Look, Elves Say ---

# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

# For example:

# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# Your puzzle input is 1321131112

# --- Part Two ---
# Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

def lookAndSay(input):
    output = ''
    currentChar = input[0]
    currentCount = 1
    for char in input[1:]:
        if char == currentChar:
            currentCount += 1
        else:
            output += str(currentCount) + currentChar
            currentChar = char
            currentCount = 1
    output += str(currentCount) + currentChar
    return output

def part1(input):
    for i in range(40):
        input = lookAndSay(input)
    print('PART 1: Length of the result: ' + str(len(input)))
    # PART 1 Answer: 492982

def part2(input):
    for i in range(50):
        input = lookAndSay(input)
    print('PART 2: Length of the result: ' + str(len(input)))
    # PART 2 Answer: 6989950

def main():
    input = '1321131112'
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()

# SOLUTION:
# Part 1: 492982
# Part 2: 6989950

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/10