node_names = [
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
# format: node, node, cost
edges = [
    [8, 1, 186],
    [2, 8, 217],
    [8, 6, 103],
    [2, 4, 173],
    [2, 5, 85],
    [5, 3, 80],
    [3, 0, 250],
    [0, 9, 84],
    [6, 9, 167],
    [6, 7, 183],
    [4, 9, 502],
]

heuristics = [0, 400, 100, 10, 460, 200, 537, 300, 170, 0]
heuristics_fixed = [0, 400, 100, 10, 460, 200, 160, 300, 170, 0]


def index_to_name(list):
    names = []
    for i in list:
        names.append(node_names[i])
    return names


for i in range(len(node_names)):
    print(f"{i}: {node_names[i]}")

for i in range(len(edges)):
    print(f"{node_names[edges[i][0]]} -> {node_names[edges[i][1]]}")


def dfs(start=8, end=9):
    max_entries = 0
    loops = 0

    visited = []
    stack = [start]
    while len(stack) > 0:
        loops += 1
        if len(stack) > max_entries:
            max_entries = len(stack)

        print(f"--\nstack: {index_to_name(stack)}, \nvisited: {index_to_name(visited)}\n--")
        curr = stack.pop(0)
        if curr == end:
            return {"status": "found", "max_entries": max_entries, "loops": loops}
        visited.append(curr)
        for e in edges:
            if e[0] == curr:
                if e[1] not in visited:
                    stack.insert(0, e[1])
            elif e[1] == curr:
                if e[0] not in visited:
                    stack.insert(0, e[0])
    return {"status": "not found", "max_entries": max_entries, "loops": loops}


def bfs(start=8, end=9):
    max_entries = 0
    loops = 0

    visited = []
    queue = [start]
    while len(queue) > 0:
        loops += 1
        if len(queue) > max_entries:
            max_entries = len(queue)

        print(f"--\nqueue: {index_to_name(queue)}, \nvisited: {index_to_name(visited)}\n--")
        if queue[0] == end:
            return {"status": "found", "max_entries": max_entries, "loops": loops}
        visited.append(queue[0])
        for e in edges:
            if e[0] == queue[0]:
                if e[1] not in visited:
                    queue.append(e[1])
            elif e[1] == queue[0]:
                if e[0] not in visited:
                    queue.append(e[0])
        queue.pop(0)
    return {"status": "not found", "max_entries": max_entries, "loops": loops}


def astar(start=8, end=9, h=heuristics):
    max_entries = 0
    loops = 0

    # node, cost to get to node
    queue = [
        [
            [
                start,
            ],
            h[start],
        ]
    ]
    while len(queue) > 0:
        loops += 1
        if len(queue) > max_entries:
            max_entries = len(queue)
        # print(queue)
        print("--\n[")
        for i in range(len(queue)):
            print(f"{index_to_name(queue[i][0])},")
        print("]\n--")
        partial = queue.pop(0)
        curr = partial[0][len(partial[0]) - 1]
        cost = partial[1]
        # print(f"{partial} --- {curr}")
        if curr == end:
            return {"status": "found", "max_entries": max_entries, "loops": loops}

        for e in edges:
            if e[0] == curr and e[1] not in partial[0]:
                tmp = list(partial)
                tmp[0] = list(partial[0])
                tmp[0].append(e[1])
                tmp[1] += e[2] + h[e[1]]
                tmp[1] -= h[e[0]]
                # print(f"curr: {curr}, tmp: {tmp}, partial: {partial}\n")
                added = False
                for i in range(len(queue)):
                    if cost + e[2] + h[e[1]] < queue[i][1]:
                        queue.insert(i, tmp)
                        added = True
                        break
                if not added:
                    queue.append(tmp)
            elif e[1] == curr and e[0] not in partial[0]:
                tmp = list(partial)
                tmp[0] = list(partial[0])
                tmp[0].append(e[0])
                tmp[1] += e[2] + h[e[0]]
                tmp[1] -= h[e[1]]
                # print(f"curr: {curr}, tmp: {tmp}, partial: {partial}\n")
                added = False
                for i in range(len(queue)):
                    if cost + e[2] + h[e[1]] < queue[i][1]:
                        queue.insert(i, tmp)
                        added = True
                        break
                if not added:
                    queue.append(tmp)
    return {"status": "not found", "max_entries": max_entries, "loops": loops}


print(f"depth-first-search: {dfs()}")
print(f"breadth-first-search: {bfs()}")
print(f"A* erroneous heuristics: {astar()}")
print(f"A* corrected heuristics: {astar(h=heuristics_fixed)}")
