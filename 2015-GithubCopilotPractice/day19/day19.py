# --- Day 19: Medicine for Rudolph ---
# Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

# Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

# However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

# For example, imagine a simpler machine that supports only the following replacements:

# H => HO
# H => OH
# O => HH
# Given the replacements above and starting with HOH, the following molecules could be generated:

# HOOH (via H => HO on the first H).
# HOHO (via H => HO on the second H).
# OHOH (via H => OH on the first H).
# HOOH (via H => OH on the second H).
# HHHH (via O => HH).
# So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

# The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

# Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

# --- Part Two ---
# Now that the machine is calibrated, you're ready to begin molecule fabrication.
    
# Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.
    
# For example, suppose you have the following replacements:
    
# e => H
# e => O
# H => HO
# H => OH
# O => HH
# If you'd like to make HOH, you start with e, and then make the following replacements:
    
# e => O to get O
# O => HH to get HH
# H => OH (on the second H) to get HOH
# So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.
    
# How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

def parse_input():
    with open("input.txt") as f:
        lines = f.readlines()
    replacements = []
    for line in lines[:-2]:
        line = line.strip()
        if line:
            replacements.append(line.split(" => "))
    return replacements, lines[-1].strip()

def get_replacements(replacements, molecule):
    new_molecules = set()
    for r in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(r[0])] == r[0]:
                new_molecules.add(molecule[:i] + r[1] + molecule[i+len(r[0]):])
    return new_molecules

def part1():
    replacements, molecule = parse_input()
    return len(get_replacements(replacements, molecule))

def part2():
    replacements, molecule = parse_input()
    steps = 0
    while molecule != "e":
        if steps % 3 == 0:
            print(steps)
        for r in replacements:
            if r[1] in molecule:
                molecule = molecule.replace(r[1], r[0], 1)
                steps += 1
    return steps
# THIS BREAKS FOR SOME REASON

print("Part 1:", part1())
print("Part 2:", part2())

# SOLUTION:
# Part 1: 576
# Part 2: 207

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/19