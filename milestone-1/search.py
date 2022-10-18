from asyncio.windows_events import INFINITE


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
    [2, 4, 173],
    [2, 5, 85],
    [2, 8, 217],
    [5, 3, 80],
    [3, 0, 250],
    [0, 9, 84],
    [8, 1, 186],
    [8, 6, 103],
    [6, 9, 167],
    [6, 7, 183],
    [4, 9, 502],
]
heuristics = [0, 400, 100, 10, 460, 200, 537, 300, 170, 0]


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
    visited = []
    stack = [start]
    while len(stack) > 0:
        print(f"--\n{index_to_name(stack)}, {index_to_name(visited)}\n--")
        if stack[0] == end:
            return "found"
        visited.append(stack[0])
        for e in edges:
            if e[0] == stack[0]:
                if e[1] not in visited:
                    stack.insert(1, e[1])
            elif e[1] == stack[0]:
                if e[0] not in visited:
                    stack.insert(1, e[0])
        stack.pop(0)
    return "unable to find"


def bfs(start=8, end=9):
    visited = []
    queue = [start]
    while len(queue) > 0:
        print(f"--\n{index_to_name(queue)}, {index_to_name(visited)}\n--")
        if queue[0] == end:
            return "found"
        visited.append(queue[0])
        for e in edges:
            if e[0] == queue[0]:
                if e[1] not in visited:
                    queue.append(e[1])
            elif e[1] == queue[0]:
                if e[0] not in visited:
                    queue.append(e[0])
        queue.pop(0)
    return "unable to find"


def astar(start=8, end=9, h=heuristics):
    # node, cost to get to node
    visited = []
    queue = [[start, 9999]]
    while len(queue) > 0:
        print(f"--\n{index_to_name([i[0] for i in queue])}, {visited}\n--")
        curr = queue[0]
        if curr[0] == end:
            return "found"
        for e in edges:
            if e[0] == curr[0]:
                if e[0] not in [i[0] for i in visited]:
                    for i in range(len(queue)):
                        if e[2] + h[e[1]] < queue[i][1]:
                            queue.insert(i, [e[1], e[2] + h[e[1]]])
            elif e[1] == curr[0]:
                if e[0] not in [i[0] for i in visited]:
                    for i in range(len(queue)):
                        if e[2] + h[e[1]] < queue[i][1]:
                            queue.insert(i, [e[0], e[2] + h[e[1]]])
        visited.append(curr)
        queue.pop(0)
    return "unable to find"


print(f"dfs: {dfs()}")
print(f"bfs: {bfs()}")
print(f"A*: {astar()}")
