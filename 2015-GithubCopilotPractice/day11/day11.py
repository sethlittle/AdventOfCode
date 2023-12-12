# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle input is hxbxwxba.

# --- Part Two ---
# Santa's password expired again. What's the next one?

# Your puzzle input is still hxbxwxba.

import argparse
import time
import re

def incrementPassword(password):
    password = list(password)
    for index, char in enumerate(password[::-1]):
        if char == 'z':
            password[len(password) - 1 - index] = 'a'
        else:
            password[len(password) - 1 - index] = chr(ord(char) + 1)
            break
    return ''.join(password)

def isValidPassword(password):
    if re.search(r'[iol]', password):
        return False
    if not re.search(r'(.)\1.*(.)\2', password):
        return False
    for index, char in enumerate(password):
        if index < len(password) - 2:
            if ord(password[index + 1]) == ord(char) + 1 and ord(password[index + 2]) == ord(char) + 2:
                return True
    return False

def part1(password):
    while True:
        password = incrementPassword(password)
        if isValidPassword(password):
            break
    print('PART 1: Santa\'s next password is: ' + password)

def part2(password):
    while True:
        password = incrementPassword(password)
        if isValidPassword(password):
            break
    while True:
        password = incrementPassword(password)
        if isValidPassword(password):
            break
    print('PART 2: Santa\'s next password is: ' + password)

def main():
    input = 'hxbxwxba'

    start_time = time.time()
    part1(input)
    print('Part 1 execution time: {:.3f} seconds'.format(time.time() - start_time))

    start_time = time.time()
    part2(input)
    print('Part 2 execution time: {:.3f} seconds'.format(time.time() - start_time))

if __name__ == '__main__':
    main()

# SOLUTION:
# Part 1: hxbxxyzz
# Part 2: hxcaabcc

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/11