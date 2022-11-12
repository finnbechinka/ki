import timeit
import random

rooms = ["B 50-H", "B 70-H", "H 10-H", "H 107", "D 317", "D 318", "D 319", "D 320", "D 327", "D 328", "A 250-H", "J 101"]
days = [0, 1, 2, 3, 4]
times = [8, 10, 12, 14, 16, 18]

dt = [(x, y) for x in days for y in times]
slots = [(x, y) for x in rooms for y in dt]

lectures = [
    ("Mathe 1", 1),
    ("Einf.i.d.Programm.m.Skriptsprachen", 1),
    ("techn. Informatik", 1),
    ("Einführung i. d. Informatik", 1),
    ("OOP", 1),
    ("Software Engineering", 2),
    ("Embedded Systems", 2),
    ("Datenbanken", 2),
    ("Systemprogrammierung", 2),
    ("Software Projektmanagement", 2),
    ("Sicherheit u. Zuverlässigkeit", 3),
    ("Webengineering", 3),
    ("Compilerbau", 3),
    ("Künstl. Intelligent", 3),
    ("Technical English", 3),
    ("Computer Vision", 3),
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
    random.shuffle(csp["variables"])
    result = bt_search({}, csp)
    if result:
        print("result:")
        [print(f"{result[x]}: {x}") for x in result]
    else:
        print("failure")
print("end")
