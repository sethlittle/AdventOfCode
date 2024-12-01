# --- Day 21: RPG Simulator 20XX ---
# Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

# In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

# Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

# Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

# Here is what the item shop is selling:

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
# You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

# For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

# The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
# In this scenario, the player wins! (Barely.)

# You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

hit_points = 100

def parse_input():
    with open("input.txt") as f:
        lines = f.readlines()
    boss = {}
    for line in lines:
        line = line.strip()
        if line:
            key, value = line.split(": ")
            boss[key] = int(value)
    return boss

def part1():
    boss = parse_input()
    weapons = [
        {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
        {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
        {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
        {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
        {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}
    ]
    armors = [
        {"name": "None", "cost": 0, "damage": 0, "armor": 0},
        {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
        {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
        {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
        {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
        {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5}
    ]
    rings = [
        {"name": "None", "cost": 0, "damage": 0, "armor": 0},
        {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
        {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
        {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
        {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
        {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
        {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3}
    ]
    min_cost = 100000
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 != ring2:
                        cost = weapon["cost"] + armor["cost"] + ring1["cost"] + ring2["cost"]
                        damage = weapon["damage"] + armor["damage"] + ring1["damage"] + ring2["damage"]
                        armorValue = weapon["armor"] + armor["armor"] + ring1["armor"] + ring2["armor"]
                        if simulate_battle(damage, armorValue, boss):
                            min_cost = min(min_cost, cost)
    return min_cost

def simulate_battle(damage, armor, boss):
    boss_hp = boss["Hit Points"]
    boss_damage = boss["Damage"]
    boss_armor = boss["Armor"]
    player_hp = hit_points
    while True:
        boss_hp -= max(damage - boss_armor, 1)
        if boss_hp <= 0:
            return True
        player_hp -= max(boss_damage - armor, 1)
        if player_hp <= 0:
            return False
        
def part2():
    boss = parse_input()
    weapons = [
        {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
        {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
        {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
        {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
        {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}
    ]
    armors = [
        {"name": "None", "cost": 0, "damage": 0, "armor": 0},
        {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
        {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
        {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
        {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
        {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5}
    ]
    rings = [
        {"name": "None", "cost": 0, "damage": 0, "armor": 0},
        {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
        {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
        {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
        {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
        {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
        {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3}
    ]
    max_cost = 0
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 != ring2:
                        cost = weapon["cost"] + armor["cost"] + ring1["cost"] + ring2["cost"]
                        damage = weapon["damage"] + armor["damage"] + ring1["damage"] + ring2["damage"]
                        armorValue = weapon["armor"] + armor["armor"] + ring1["armor"] + ring2["armor"]
                        if not simulate_battle(damage, armorValue, boss):
                            max_cost = max(max_cost, cost)
    return max_cost

print("Part 1:", part1())
print("Part 2:", part2())

# SOLUTION:
# Part 1: 121
# Part 2: 201

# Generated using GitHub Copilot as a practice exercise
# SOURCE: https://adventofcode.com/2015/day/21