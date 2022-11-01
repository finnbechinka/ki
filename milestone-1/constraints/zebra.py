csp = {}
csp["variables"] = [
    "gelb",
    "blau",
    "rot",
    "grün",
    "weiß",
    "norweger",
    "ukrainer",
    "engländer",
    "japaner",
    "spanier",
    "wasser",
    "tee",
    "milch",
    "kaffee",
    "o-saft",
    "kools",
    "chesterfield",
    "oldgold",
    "parliament",
    "luckystrikes",
    "fuchs",
    "pferd",
    "schnecke",
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
    if var == "engländer" and "rot" in assignment:
        if value != assignment["rot"]:
            return False
    if var == "rot" and "engländer" in assignment:
        if value != assignment["engländer"]:
            return False
    if var == "spanier" and "hund" in assignment:
        if value != assignment["hund"]:
            return False
    if var == "hund" and "spanier" in assignment:
        if value != assignment["spanier"]:
            return False
    if var == "kaffee" and "grün" in assignment:
        if value != assignment["grün"]:
            return False
    if var == "grün" and "kaffee" in assignment:
        if value != assignment["kaffee"]:
            return False
    if var == "ukrainer" and "tee" in assignment:
        if value != assignment["tee"]:
            return False
    if var == "tee" and "ukrainer" in assignment:
        if value != assignment["ukrainer"]:
            return False
    if var == "grün" and "weiß" in assignment:
        if value != assignment["weiß"] + 1:
            return False
    if var == "weiß" and "grün" in assignment:
        if value + 1 != assignment["grün"]:
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
    if var == "chesterfield" and "fuchs" in assignment:
        if value != assignment["fuchs"] + 1 and value != assignment["fuchs"] - 1:
            return False
    if var == "fuchs" and "chesterfield" in assignment:
        if value != assignment["chesterfield"] + 1 and value != assignment["chesterfield"] - 1:
            return False
    if var == "kools" and "pferd" in assignment:
        if value != assignment["pferd"] + 1 and value != assignment["pferd"] - 1:
            return False
    if var == "pferd" and "kools" in assignment:
        if value != assignment["kools"] + 1 and value != assignment["kools"] - 1:
            return False
    if var == "luckystrike" and "o-saft" in assignment:
        if value != assignment["o-saft"]:
            return False
    if var == "o-saft" and "luckystrike" in assignment:
        if value != assignment["luckystrike"]:
            return False
    if var == "japaner" and "parliaments" in assignment:
        if value != assignment["parliaments"]:
            return False
    if var == "parliaments" and "japaner" in assignment:
        if value != assignment["japaner"]:
            return False
    if var == "norweger" and "blau" in assignment:
        if value != assignment["blau"]:
            return False
    if var == "blau" and "norweger" in assignment:
        if value != assignment["norweger"]:
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
    if var == "gelb" and "grün" in assignment:
        if value == assignment["grün"]:
            return False
    if var == "gelb" and "weiß" in assignment:
        if value == assignment["weiß"]:
            return False
    if var == "blau" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "blau" and "grün" in assignment:
        if value == assignment["grün"]:
            return False
    if var == "blau" and "weiß" in assignment:
        if value == assignment["weiß"]:
            return False
    if var == "rot" and "grün" in assignment:
        if value == assignment["grün"]:
            return False
    if var == "rot" and "weiß" in assignment:
        if value == assignment["weiß"]:
            return False
    if var == "grün" and "weiß" in assignment:
        if value == assignment["weiß"]:
            return False

    if var == "blau" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "rot" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "grün" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "weiß" and "gelb" in assignment:
        if value == assignment["gelb"]:
            return False
    if var == "rot" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "grün" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "weiß" and "blau" in assignment:
        if value == assignment["blau"]:
            return False
    if var == "grün" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "weiß" and "rot" in assignment:
        if value == assignment["rot"]:
            return False
    if var == "weiß" and "grün" in assignment:
        if value == assignment["grün"]:
            return False

    if var == "norweger" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "norweger" and "engländer" in assignment:
        if value == assignment["engländer"]:
            return False
    if var == "norweger" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "norweger" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "ukrainer" and "engländer" in assignment:
        if value == assignment["engländer"]:
            return False
    if var == "ukrainer" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "ukrainer" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "engländer" and "japaner" in assignment:
        if value == assignment["japaner"]:
            return False
    if var == "engländer" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False
    if var == "japaner" and "spanier" in assignment:
        if value == assignment["spanier"]:
            return False

    if var == "ukrainer" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "engländer" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "japaner" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "spanier" and "norweger" in assignment:
        if value == assignment["norweger"]:
            return False
    if var == "engländer" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "japaner" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "spanier" and "ukrainer" in assignment:
        if value == assignment["ukrainer"]:
            return False
    if var == "japaner" and "engländer" in assignment:
        if value == assignment["engländer"]:
            return False
    if var == "spanier" and "engländer" in assignment:
        if value == assignment["engländer"]:
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
    if var == "wasser" and "o-saft" in assignment:
        if value == assignment["o-saft"]:
            return False
    if var == "tee" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "tee" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False
    if var == "tee" and "o-saft" in assignment:
        if value == assignment["o-saft"]:
            return False
    if var == "milch" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False
    if var == "milch" and "o-saft" in assignment:
        if value == assignment["o-saft"]:
            return False
    if var == "kaffee" and "o-saft" in assignment:
        if value == assignment["o-saft"]:
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
    if var == "o-saft" and "wasser" in assignment:
        if value == assignment["wasser"]:
            return False
    if var == "milch" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "kaffee" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "o-saft" and "tee" in assignment:
        if value == assignment["tee"]:
            return False
    if var == "kaffee" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "o-saft" and "milch" in assignment:
        if value == assignment["milch"]:
            return False
    if var == "o-saft" and "kaffee" in assignment:
        if value == assignment["kaffee"]:
            return False

    if var == "kools" and "chesterfield" in assignment:
        if value == assignment["chesterfield"]:
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
    if var == "chesterfield" and "oldgold" in assignment:
        if value == assignment["oldgold"]:
            return False
    if var == "chesterfield" and "parliament" in assignment:
        if value == assignment["parliament"]:
            return False
    if var == "chesterfield" and "luckystrikes" in assignment:
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

    if var == "chesterfield" and "kools" in assignment:
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
    if var == "oldgold" and "chesterfield" in assignment:
        if value == assignment["chesterfield"]:
            return False
    if var == "parliament" and "chesterfield" in assignment:
        if value == assignment["chesterfield"]:
            return False
    if var == "luckystrikes" and "chesterfield" in assignment:
        if value == assignment["chesterfield"]:
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
    if var == "fuchs" and "schnecke" in assignment:
        if value == assignment["schnecke"]:
            return False
    if var == "fuchs" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "fuchs" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "pferd" and "schnecke" in assignment:
        if value == assignment["schnecke"]:
            return False
    if var == "pferd" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "pferd" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "schnecke" and "zebra" in assignment:
        if value == assignment["zebra"]:
            return False
    if var == "schnecke" and "hund" in assignment:
        if value == assignment["hund"]:
            return False
    if var == "zebra" and "hund" in assignment:
        if value == assignment["hund"]:
            return False

    if var == "pferd" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "schnecke" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "zebra" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "hund" and "fuchs" in assignment:
        if value == assignment["fuchs"]:
            return False
    if var == "schnecke" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "zebra" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "hund" and "pferd" in assignment:
        if value == assignment["pferd"]:
            return False
    if var == "zebra" and "schnecke" in assignment:
        if value == assignment["schnecke"]:
            return False
    if var == "hund" and "schnecke" in assignment:
        if value == assignment["schnecke"]:
            return False
    if var == "hund" and "zebra" in assignment:
        if value == assignment["zebra"]:
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


result = bt_search({}, csp)

print("result:")
i = 0
for key, value in result.items():
    i += 1
    if i % 5 == 0:
        print(f"{key}: {value}")
    else:
        print(f"{key}: {value}, ", end="")
