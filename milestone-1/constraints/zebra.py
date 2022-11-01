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
    "mild",
    "kaffee",
    "o-saft",
    "kools",
    "chesterfield",
    "oldgold",
    "parliament",
    "luckystrike",
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
    # TODO: add constraint checks
    return True


print(csp["values"])
