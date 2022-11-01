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


def next_var(assignment, csp):
    for var in csp["variables"]:
        if var not in assignment:
            return var


def bt_search(assignment, csp):
    if complete(assignment):
        return assignment

    var = next_var(assignment, csp)

    for value in csp["values"][csp["variables"].index(var)]:
        print(value)
        if consistent(value, var, assignment, csp):
            assignment[var] = value
            result = bt_search(assignment, csp)
            if result:
                return result
            del assignment[var]
    return False


bt_search({}, csp)
