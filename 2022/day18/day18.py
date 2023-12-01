from collections import defaultdict
from itertools import product

import networkx as nx
import numpy as np

with open("inputDay18.txt") as f:
    ls = f.read().strip().split("\n")

ns = np.array([list(map(int, l.split(","))) for l in ls])
print("Part One Answer:", sum(6 - (np.abs(cube - ns).sum(1) == 1).sum() for cube in ns))

# part 2
xmin, ymin, zmin = ns.min(0) - 1
xmax, ymax, zmax = ns.max(0) + 2
grid = set(product(range(xmin, xmax), range(ymin, ymax), range(zmin, zmax)))
cubes = set(map(tuple, ns))

dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
G = nx.Graph()
area = defaultdict(int)

for node1 in grid - cubes:
    x, y, z = node1
    for (dx, dy, dz) in dirs:
        node2 = (x + dx, y + dy, z + dz)
        if node2 in cubes:
            area[node1] += 1
        else:
            G.add_edge(node1, node2)

# At this point, the exterior area is simply the area of the
# connected component containing one of the points in the
# exterior.
print("Part Two Answer:", sum(area[n] for n in nx.descendants(G, (xmin, ymin, zmin))))