import timeit
import random

rooms = ["B 50-H", "B 70-H", "H 10-H", "H 107", "D 317", "D 318", "D 319", "D 320", "D 327", "D 328", "A 250-H", "J 101"]
days = [0, 1, 2, 3, 4]
times = [8, 10, 12]

dt = [(x, y) for x in days for y in times]
slots = [(x, y) for x in rooms for y in dt]

lectures = [
    ("Mathe 1/V1", 1, "George, BC"),
    ("Mathe 1/V2", 1, "George, BC"),
    ("Mathe 1/Ü", 1, "Kreienkamp, Angela"),
    ("Einf.i.d.Programm.m.Skriptsprachen/V", 1, "George, BC"),
    ("Einf.i.d.Programm.m.Skriptsprachen/P", 1, "George, BC"),
    ("techn. Informatik/V", 1, "Kreienkamp, Angela"),
    ("techn. Informatik/P", 1, "Kreienkamp, Angela"),
    ("Einführung i. d. Informatik/V", 1, "Behrens, Grit"),
    ("Einführung i. d. Informatik/Ü", 1, "Behrens, Grit"),
    ("OOP/V", 1, "Rexilius, Jan"),
    ("OOP/P", 1, "Rexilius, Jan"),
    ("Software Engineering/V", 3, "Brunsmann, Jörg"),
    ("Software Engineering/P", 3, "Brunsmann, Jörg"),
    ("Embedded Systems/V", 3, "König, Matthias"),
    ("Embedded Systems/P", 3, "König, Matthias"),
    ("Datenbanken/V", 3, "Becking, Dominic"),
    ("Datenbanken/P", 3, "Becking, Dominic"),
    ("Systemprogrammierung/V", 3, "Gips, Carsten"),
    ("Systemprogrammierung/P", 3, "Gips, Carsten"),
    ("Software Projektmanagement", 3, "Teich, Irene"),
    ("Sicherheit u. Zuverlässigkeit/V", 5, "Thiel, Christoph"),
    ("Sicherheit u. Zuverlässigkeit/P", 5, "Thiel, Christoph"),
    ("Webengineering/V", 5, "Behrens, Grit"),
    ("Webengineering/P", 5, "Behrens, Grit"),
    ("Compilerbau/V", 5, "Gips, Carsten"),
    ("Compilerbau/P", 5, "Gips, Carsten"),
    ("Künstl. Intelligent/V", 5, "Gips, Carsten"),
    ("Künstl. Intelligent/P", 5, "Gips, Carsten"),
    ("Technical English", 5, "Demir, Hüseyin"),
    ("Computer Vision/V", 5, "Rexilius, Jan"),
    ("Computer Vision/P", 5, "Rexilius, Jan"),
]

edges = [(x, y) for x in range(len(lectures)) for y in range(len(lectures))]
remove = []
for i in range(len(edges) - 1):
    if edges[i][0] == edges[i][1]:
        remove.append(edges[i])
for e in remove:
    edges.remove(e)
neighbors = []
for i in range(len(lectures)):
    neighbors.append([])
    for j in range(len(lectures)):
        if i == j:
            continue
        neighbors[i].append(j)

csp = {}
csp["variables"] = lectures
csp["values"] = []
for i in range(len(csp["variables"])):
    tmp = slots.copy()
    random.shuffle(tmp)
    csp["values"].append(slots.copy())


def complete(assignment):
    if len(assignment) == len(csp["variables"]):
        return True
    return False


def consistent(value, var, assignment, csp):
    free_days = {1: 0, 3: 4, 5: 2}
    sem = var[1]
    p = var[2]
    dt = value[1]
    day = dt[0]
    time = dt[1]
    # check if day is free day for given semester
    if free_days[sem] == day:
        return False
    # check for time overlap
    for k, v in assignment.items():
        curr_sem = k[1]
        curr_p = k[2]
        curr_dt = v[1]
        same_sem = curr_sem == sem
        same_dt = curr_dt == dt
        same_p = curr_p == p
        # check if sem already has event at given time
        if same_sem and same_dt:
            return False
        # check if prof already has event at given time
        if same_dt and same_p:
            return False
    # check if slot is already is use
    if value in assignment.values():
        return False
    return True


def next_var(assignment, csp):
    for var in csp["variables"]:
        if var not in assignment:
            return var


def bt_search(assignment, csp):
    if complete(assignment):
        return assignment
    var = next_var(assignment, csp)
    for value in csp["values"][csp["variables"].index(var)]:
        if consistent(value, var, assignment, csp):
            assignment[var] = value
            result = bt_search(assignment, csp)
            if result:
                return result
            del assignment[var]
    return False


def ac3(csp):
    queue = edges.copy()
    while len(queue) >= 1:
        x, y = queue.pop(0)
        if arc_reduce(csp, x, y):
            if len(csp["values"][x]) == 0:
                return False
            for z in neighbors[x]:
                queue.append(z, x)


def arc_reduce(csp, x, y):
    removed = False
    for v in csp["values"][x]:
        tmp_ass = {}
        tmp_ass[csp["variables"][x]] = v
        found = False
        for v2 in csp["values"][y]:
            if consistent(v2, csp["variables"][y], tmp_ass, csp):
                found = True
        if not found:
            csp["values"][x].remove(v)
            removed = True
    return removed


print("start")
# print(csp)
ac3(csp)
# print(csp)
n = 1
runtime_total = 0
for i in range(n):
    csp["variables"]
    result = bt_search({}, csp)
    if result:
        print("result:")
        [print(f"{result[x]}: {x}") for x in result]
    else:
        print("failure")
print("end")
