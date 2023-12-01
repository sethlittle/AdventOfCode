from collections import defaultdict
from heapq import heappop, heappush
import re

with open("inputDay16.txt") as f:
    ls = f.read().strip().split("\n")

flows = {}
neighbors = defaultdict(list)
for l in ls:
    this = l.split()[1]
    flow = int(re.findall("\d+", l)[0])
    flows[this] = flow
    for neighbor in l.split()[9:]:
        neighbors[this].append(neighbor.replace(",", ""))

penalty = 110

# Part 1
def actions(state):
    score, valveName, time, opened = state
    for neighbor in neighbors[valveName]:
        yield (score + penalty, neighbor, time + 1, opened)
    if valveName not in opened and flows[valveName] != 0:
        new_opened = opened | {valveName}
        yield (
            score - (30 - time - 1) * flows[valveName] + penalty,
            valveName,
            time + 1,
            new_opened,
        )


q = [(0, "AA", 0, frozenset())]
seen = {q[0]}
while q:
    state = heappop(q)
    score, _, time, _ = state
    if time == 30:
        print("Part One Answer:", 30 * penalty - score) #2119
        break
    for new_state in actions(state):
        if new_state in seen:
            continue
        seen.add(new_state)
        heappush(q, new_state)

# Part 2
def actions2(state):
    score, valveName1, valveName2, time, opened = state
    # Both move
    for neighbor in neighbors[valveName1]:
        for neighbor2 in neighbors[valveName2]:
            yield (score + penalty, neighbor, neighbor2, time + 1, opened)
    # Both open
    if (
        valveName1 != valveName2
        and valveName1 not in opened
        and valveName2 not in opened
        and flows[valveName1] != 0
        and flows[valveName2] != 0
    ):
        new_opened = opened | {valveName1, valveName2}
        yield (
            score
            - (26 - time - 1) * flows[valveName1]
            - (26 - time - 1) * flows[valveName2]
            + penalty,
            valveName1,
            valveName2,
            time + 1,
            new_opened,
        )
    # We open, elephant moves
    if valveName1 not in opened and flows[valveName1] != 0:
        new_opened = opened | {valveName1}
        for neighbor2 in neighbors[valveName2]:
            yield (
                score - (26 - time - 1) * flows[valveName1] + penalty,
                valveName1,
                neighbor2,
                time + 1,
                new_opened,
            )
    # We move, elephant opens
    if valveName2 not in opened and flows[valveName2] != 0:
        new_opened = opened | {valveName2}
        for neighbor in neighbors[valveName1]:
            yield (
                score - (26 - time - 1) * flows[valveName2] + penalty,
                neighbor,
                valveName2,
                time + 1,
                new_opened,
            )


q = [(0, "AA", "AA", 0, frozenset())]
seen = {q[0]}
while q:
    state = heappop(q)
    score, _, _, time, _ = state
    if time == 26:
        print("Part Two Answer:", 26 * penalty - score) #2615
        break
    for new_state in actions2(state):
        if new_state in seen:
            continue
        seen.add(new_state)
        heappush(q, new_state)
