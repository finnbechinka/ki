import timeit
import random

csp = {}
csp["variables"] = [
    "gelb",
    "blau",
    "rot",
    "gruen",
    "weiss",
    "norweger",
    "ukrainer",
    "englaender",
    "japaner",
    "spanier",
    "wasser",
    "tee",
    "milch",
    "kaffee",
    "osaft",
    "kools",
    "chesterfields",
    "oldgold",
    "parliament",
    "luckystrikes",
    "fuchs",
    "pferd",
    "schnecken",
    "zebra",
    "hund",
]
csp["values"] = []
for i in range(len(csp["variables"])):
    csp["values"].append([0, 1, 2, 3, 4])


def complete(assignment):
    if len(assignment) == len(csp["variables"]):
        return True
    return False


def consistent(value, var, assignment, csp):
    if var == "englaender" and "rot" in assignment:
        if value != assignment["rot"]:
            return False
    if var == "rot" and "englaender" in assignment:
        if value != assignment["englaender"]:
            return False
    if var == "spanier" and "hund" in assignment:
        if value != assignment["hund"]:
            return False
    if var == "hund" and "spanier" in assignment:
        if value != assignment["spanier"]:
            return False
    if var == "kaffee" and "gruen" in assignment:
        if value != assignment["gruen"]:
            return False
    if var == "gruen" and "kaffee" in assignment:
        if value != assignment["kaffee"]:
            return False
    if var == "ukrainer" and "tee" in assignment:
        if value != assignment["tee"]:
            return False
    if var == "tee" and "ukrainer" in assignment:
        if value != assignment["ukrainer"]:
            return False
    if var == "gruen" and "weiss" in assignment:
        if value != assignment["weiss"] - 1:
            return False
    if var == "weiss" and "gruen" in assignment:
        if value - 1 != assignment["gruen"]:
            return False
    if var == "oldgold" and "schnecken" in assignment:
        if value != assignment["schnecken"]:
            return False
    if var == "schnecken" and "oldgold" in assignment:
        if value != assignment["oldgold"]:
            return False
    if var == "kools" and "gelb" in assignment:
        if value != assignment["gelb"]:
            return False
    if var == "gelb" and "kools" in assignment:
        if value != assignment["kools"]:
            return False
    if var == "milch":
        if value != 2:
            return False
    if var == "norweger":
        if value != 0:
            return False
    if var == "chesterfields" and "fuchs" in assignment:
        if value != assignment["fuchs"] + 1 and value != assignment["fuchs"] - 1:
            return False
    if var == "fuchs" and "chesterfields" in assignment:
        if value + 1 != assignment["chesterfields"] and value - 1 != assignment["chesterfields"]:
            return False
    if var == "kools" and "pferd" in assignment:
        if value != assignment["pferd"] + 1 and value != assignment["pferd"] - 1:
            return False
    if var == "pferd" and "kools" in assignment:
        if value + 1 != assignment["kools"] and value - 1 != assignment["kools"]:
            return False
    if var == "luckystrikes" and "osaft" in assignment:
        if value != assignment["osaft"]:
            return False
    if var == "osaft" and "luckystrikes" in assignment:
        if value != assignment["luckystrikes"]:
            return False
    if var == "japaner" and "parliament" in assignment:
        if value != assignment["parliament"]:
            return False
    if var == "parliament" and "japaner" in assignment:
        if value != assignment["japaner"]:
            return False
    if var == "norweger" and "blau" in assignment:
        if value != assignment["blau"] + 1 and value != assignment["blau"] - 1:
            return False
    if var == "blau" and "norweger" in assignment:
        if value != assignment["norweger"] + 1 and value != assignment["norweger"] - 1:
            return False
    if var == "chesterfields" and "wasser" in assignment:
        if value != assignment["wasser"] + 1 and value != assignment["wasser"] - 1:
            return False
    if var == "wasser" and "chesterfields" in assignment:
        if value != assignment["chesterfields"] + 1 and value != assignment["chesterfields"] - 1:
            return False

    if var == "gelb" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "gelb" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "gelb" and "gruen" in assignment:
        if value == assignment["gruen"]:
            return False
    if var == "gelb" and "weiss" in assignment:
        if value == assignment["weiss"]:
            return False
    if var == "blau" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "blau" and "gruen" in assignment:
        if value == assignment["gruen"]:
            return False
    if var == "blau" and "weiss" in assignment:
        if value == assignment["weiss"]:
            return False
    if var == "rot" and "gruen" in assignment:
        if value == assignment["gruen"]:
            return False
    if var == "rot" and "weiss" in assignment:
        if value == assignment["weiss"]:
            return False
    if var == "gruen" and "weiss" in assignment:
        if value == assignment["weiss"]:
            return False

    if var == "blau" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "rot" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "gruen" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "weiss" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "rot" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "gruen" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "weiss" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "gruen" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "weiss" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "weiss" and "gruen" in assignment:
        if value == assignment["gruen"]:
            return False

    if var == "norweger" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "norweger" and "englaender" in assignment:
        if value == assignment["englaender"]:
            return False
    if var == "norweger" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "norweger" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "ukrainer" and "englaender" in assignment:
        if value == assignment["englaender"]:
            return False
    if var == "ukrainer" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "ukrainer" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "englaender" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "englaender" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "japaner" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False

    if var == "ukrainer" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "englaender" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "japaner" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "spanier" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "englaender" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "japaner" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "spanier" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "japaner" and "englaender" in assignment:
        if value == assignment["englaender"]:
            return False
    if var == "spanier" and "englaender" in assignment:
        if value == assignment["englaender"]:
            return False
    if var == "spanier" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False

    if var == "wasser" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "wasser" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "wasser" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False
    if var == "wasser" and "osaft" in assignment:
        if value == assignment["osaft"]:
            return False
    if var == "tee" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "tee" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False
    if var == "tee" and "osaft" in assignment:
        if value == assignment["osaft"]:
            return False
    if var == "milch" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False
    if var == "milch" and "osaft" in assignment:
        if value == assignment["osaft"]:
            return False
    if var == "kaffee" and "osaft" in assignment:
        if value == assignment["osaft"]:
            return False

    if var == "tee" and "wasser" in assignment:
        if value == assignment["wasser"]:
            return False
    if var == "milch" and "wasser" in assignment:
        if value == assignment["wasser"]:
            return False
    if var == "kaffee" and "wasser" in assignment:
        if value == assignment["wasser"]:
            return False
    if var == "osaft" and "wasser" in assignment:
        if value == assignment["wasser"]:
            return False
    if var == "milch" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "kaffee" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "osaft" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "kaffee" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "osaft" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "osaft" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False

    if var == "kools" and "chesterfields" in assignment:
        if value == assignment["chesterfields"]:
            return False
    if var == "kools" and "oldgold" in assignment:
        if value == assignment["oldgold"]:
            return False
    if var == "kools" and "parliament" in assignment:
        if value == assignment["parliament"]:
            return False
    if var == "kools" and "luckystrikes" in assignment:
        if value == assignment["luckystrikes"]:
            return False
    if var == "chesterfields" and "oldgold" in assignment:
        if value == assignment["oldgold"]:
            return False
    if var == "chesterfields" and "parliament" in assignment:
        if value == assignment["parliament"]:
            return False
    if var == "chesterfields" and "luckystrikes" in assignment:
        if value == assignment["luckystrikes"]:
            return False
    if var == "oldgold" and "parliament" in assignment:
        if value == assignment["parliament"]:
            return False
    if var == "oldgold" and "luckystrikes" in assignment:
        if value == assignment["luckystrikes"]:
            return False
    if var == "parliament" and "luckystrikes" in assignment:
        if value == assignment["luckystrikes"]:
            return False

    if var == "chesterfields" and "kools" in assignment:
        if value == assignment["kools"]:
            return False
    if var == "oldgold" and "kools" in assignment:
        if value == assignment["kools"]:
            return False
    if var == "parliament" and "kools" in assignment:
        if value == assignment["kools"]:
            return False
    if var == "luckystrikes" and "kools" in assignment:
        if value == assignment["kools"]:
            return False
    if var == "oldgold" and "chesterfields" in assignment:
        if value == assignment["chesterfields"]:
            return False
    if var == "parliament" and "chesterfields" in assignment:
        if value == assignment["chesterfields"]:
            return False
    if var == "luckystrikes" and "chesterfields" in assignment:
        if value == assignment["chesterfields"]:
            return False
    if var == "parliament" and "oldgold" in assignment:
        if value == assignment["oldgold"]:
            return False
    if var == "luckystrikes" and "oldgold" in assignment:
        if value == assignment["oldgold"]:
            return False
    if var == "luckystrikes" and "parliament" in assignment:
        if value == assignment["parliament"]:
            return False

    if var == "fuchs" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "fuchs" and "schnecken" in assignment:
        if value == assignment["schnecken"]:
            return False
    if var == "fuchs" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "fuchs" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "pferd" and "schnecken" in assignment:
        if value == assignment["schnecken"]:
            return False
    if var == "pferd" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "pferd" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "schnecken" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "schnecken" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "zebra" and "hund" in assignment:
        if value == assignment["hund"]:
            return False

    if var == "pferd" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "schnecken" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "zebra" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "hund" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "schnecken" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "zebra" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "hund" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "zebra" and "schnecken" in assignment:
        if value == assignment["schnecken"]:
            return False
    if var == "hund" and "schnecken" in assignment:
        if value == assignment["schnecken"]:
            return False
    if var == "hund" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False

    return True


def next_var(assignment, csp):
    best_var = 0
    min_len = 999
    for var in csp["variables"]:
        if var not in assignment:
            if len(csp["values"][csp["variables"].index(var)]) < min_len:
                best_var = var
    return best_var


def bt_search(assignment, csp):
    if complete(assignment):
        return assignment
    var = next_var(assignment, csp)
    removed = []
    while len(csp["values"][csp["variables"].index(var)]) > 0:
        value = csp["values"][csp["variables"].index(var)][0]
        if consistent(value, var, assignment, csp):
            assignment[var] = value
            result = bt_search(assignment, csp)
            if result:
                return result
            del assignment[var]

        removed.append(csp["values"][csp["variables"].index(var)][csp["values"][csp["variables"].index(var)].index(value)])
        csp["values"][csp["variables"].index(var)].remove(value)
    for v in removed:
        csp["values"][csp["variables"].index(var)].append(v)

    return False


print("start")
random.shuffle(csp["variables"])
n = 1
times = timeit.timeit("bt_search({}, csp)", globals=globals(), number=n)

result = bt_search({}, csp)

if result:
    print("result:")
    haeuser = [[], [], [], [], []]
    for key, value in result.items():
        haeuser[value].append(key)
    for i in range(len(haeuser)):
        print(f"Haus {i+1}: {haeuser[i]}")
else:
    print("failure")
print(f"avg runtime: {(times/n):.4f}s")
print("end")
