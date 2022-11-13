import timeit
import random

rooms = ["B 50-H", "B 70-H", "H 10-H", "H 107", "D 317", "D 318", "D 319", "D 320", "D 327", "D 328", "A 250-H", "J 101"]
days = [0, 1, 2, 3, 4]
times = [8, 10, 12, 14, 16]

dt = [(x, y) for x in days for y in times]
slots = [(x, y) for x in rooms for y in dt]

lectures = [
    ("Mathe 1", 1),
    ("Einf.i.d.Programm.m.Skriptsprachen", 1),
    ("techn. Informatik", 1),
    ("Einführung i. d. Informatik", 1),
    ("OOP", 1),
    ("asdasd1", 1),
    ("Einfasdasdhen", 1),
    ("dteasdasdik", 1),
    ("Eiasdasdasik", 1),
    ("sdasdasd", 1),
    ("Software Engineering", 3),
    ("Embedded Systems", 3),
    ("Datenbanken", 3),
    ("Systemprogrammierung", 3),
    ("Software Projektmanagement", 3),
    ("Sicherheit u. Zuverlässigkeit", 5),
    ("Webengineering", 5),
    ("Compilerbau", 5),
    ("Künstl. Intelligent", 5),
    ("Technical English", 5),
    ("Computer Vision", 5),
]


csp = {}
csp["variables"] = lectures
csp["values"] = []
for i in range(len(csp["variables"])):
    tmp = slots.copy()
    random.shuffle(tmp)
    csp["values"].append(tmp)


def complete(assignment):
    if len(assignment) == len(csp["variables"]):
        return True
    return False


def consistent(value, var, assignment, csp):
    free_days = {1: 0, 3: 4, 5: 2}
    sem = var[1]
    dt = value[1]
    day = dt[0]
    time = dt[1]
    # check if day is free day for given semester
    if free_days[sem] == day:
        return False
    # check if there is already a lecture at the proposed day/time for given semester
    for k, v in assignment.items():
        curr_sem = v[1]
        curr_dt = k[1]
        same_sem = curr_sem == sem
        same_dt = curr_dt == dt
        if same_sem and same_dt:
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


print("start")
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
