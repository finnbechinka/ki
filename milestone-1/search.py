nodes = [
    "Augsburg",
    "Erfurt",
    "Frankfurt",
    "Karlsruhe",
    "Kassel",
    "Mannheim",
    "Nürnberg",
    "Stuttgart",
    "Würzburg",
    "München",
]
edges = [
    [2, 4],
    [2, 5],
    [2, 8],
    [5, 3],
    [3, 0],
    [0, 9],
    [8, 1],
    [8, 6],
    [6, 7],
    [6, 9],
    [4, 9],
]

for i in range(len(nodes)):
    print(f"{i}: {nodes[i]}")

for i in range(len(edges)):
    print(f"{nodes[edges[i][0]]} -> {nodes[edges[i][1]]}")
