from platform import node


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


def index_to_name(list):
    names = []
    for i in list:
        names.append(nodes[i])
    return names


def dfs(start=8, end=9):
    visited = []
    stack = [start]
    while len(stack) > 0:
        print(f"--\n{index_to_name(stack)}, {index_to_name(visited)}\n--\n")
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
        print(f"--\n{index_to_name(queue)}, {index_to_name(visited)}\n--\n")
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


print(dfs())
print(bfs())
