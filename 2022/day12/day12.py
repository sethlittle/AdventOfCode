from math import inf
import networkx as nx

with open("inputDay12.txt") as f:
    ls = f.read().strip().split("\n")

all_as = set()
elev = {}
for x, l in enumerate(ls):
    for y, char in enumerate(l):
        point = (x, y)
        elev[point] = ord(char)
        match char:
            case "S":
                s = point
                elev[point] = ord("a")
            case "E":
                e = point
                elev[point] = ord("z")
            case "a":
                all_as.add(point)
            

G = nx.DiGraph()
for point in elev:
    x = point[0]
    y = point[1]
    for (dx, dy) in [(0, 1), (0,-1), (1,0), (-1,0)]:
        if elev.get((x + dx, y + dy), inf) <= elev[point] + 1:
            G.add_edge(point, (x + dx, y + dy))

# Part 1
print("Part One Answer: ", nx.shortest_path_length(G, s, e)) #412

# Part 2
all_lengths = nx.shortest_path_length(G, target=e)
print("Part Two Answer: ", min(all_lengths.get(a, inf) for a in all_as)) #402
