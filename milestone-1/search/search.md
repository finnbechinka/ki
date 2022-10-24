# Search
## Aufgabe 1
### Tiefensuche
```
--
stack: ['Würzburg'],
visited: []
--
--
stack: ['Nürnberg', 'Erfurt', 'Frankfurt'],
visited: ['Würzburg']
--
--
stack: ['Stuttgart', 'München', 'Erfurt', 'Frankfurt'],
visited: ['Würzburg', 'Nürnberg']
--
--
stack: ['München', 'Erfurt', 'Frankfurt'],
visited: ['Würzburg', 'Nürnberg', 'Stuttgart']
--
depth-first-search: {'status': 'found', 'max_entries': 4, 'loops': 4}
```
### Breitensuche
```
--
queue: ['Würzburg'],
visited: []
--
--
queue: ['Frankfurt', 'Erfurt', 'Nürnberg'],
visited: ['Würzburg']
--
--
queue: ['Erfurt', 'Nürnberg', 'Kassel', 'Mannheim'],
visited: ['Würzburg', 'Frankfurt']
--
--
queue: ['Nürnberg', 'Kassel', 'Mannheim'],
visited: ['Würzburg', 'Frankfurt', 'Erfurt']
--
--
queue: ['Kassel', 'Mannheim', 'München', 'Stuttgart'],
visited: ['Würzburg', 'Frankfurt', 'Erfurt', 'Nürnberg']
--
--
queue: ['Mannheim', 'München', 'Stuttgart', 'München'],
visited: ['Würzburg', 'Frankfurt', 'Erfurt', 'Nürnberg', 'Kassel']
--
--
queue: ['München', 'Stuttgart', 'München', 'Karlsruhe'],
visited: ['Würzburg', 'Frankfurt', 'Erfurt', 'Nürnberg', 'Kassel', 'Mannheim']
--
breadth-first-search: {'status': 'found', 'max_entries': 4, 'loops': 7}
```
### A*
```
--
[
['Würzburg'],
]
--
--
[
['Würzburg', 'Frankfurt'],
['Würzburg', 'Erfurt'],
['Würzburg', 'Nürnberg'],
]
--
--
[
['Würzburg', 'Erfurt'],
['Würzburg', 'Frankfurt', 'Mannheim'],
['Würzburg', 'Nürnberg'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
--
[
['Würzburg', 'Frankfurt', 'Mannheim'],
['Würzburg', 'Nürnberg'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
--
[
['Würzburg', 'Frankfurt', 'Mannheim', 'Karlsruhe'],
['Würzburg', 'Nürnberg'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
--
[
['Würzburg', 'Nürnberg'],
['Würzburg', 'Frankfurt', 'Mannheim', 'Karlsruhe', 'Augsburg'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
--
[
['Würzburg', 'Frankfurt', 'Mannheim', 'Karlsruhe', 'Augsburg'],
['Würzburg', 'Nürnberg', 'München'],
['Würzburg', 'Frankfurt', 'Kassel'],
['Würzburg', 'Nürnberg', 'Stuttgart'],
]
--
--
[
['Würzburg', 'Nürnberg', 'München'],
['Würzburg', 'Frankfurt', 'Mannheim', 'Karlsruhe', 'Augsburg', 'München'],
['Würzburg', 'Frankfurt', 'Kassel'],
['Würzburg', 'Nürnberg', 'Stuttgart'],
]
--
A* erroneous heuristics: {'status': 'found', 'max_entries': 4, 'loops': 8}
```

## Aufgabe 2

Die gegebenen Restkostenabschätzungen dürfen nicht verwendet werden da die Restkosten für Nürnberg zu hoch geschätzt wurden. 
$$h(n)\leq h^*(n)\space nicht \space erfüllt$$
$$537_{km}\nleq 167_{km}$$
Um dies zu beheben muss die Restkostenabschätzung für Nürnberg auf $\leq167_{km}$ gesetzt werden.
```
--
[
['Würzburg'],
]
--
--
[
['Würzburg', 'Frankfurt'],
['Würzburg', 'Nürnberg'],
['Würzburg', 'Erfurt'],
]
--
--
[
['Würzburg', 'Nürnberg'],
['Würzburg', 'Erfurt'],
['Würzburg', 'Frankfurt', 'Mannheim'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
--
[
['Würzburg', 'Nürnberg', 'München'],
['Würzburg', 'Erfurt'],
['Würzburg', 'Frankfurt', 'Mannheim'],
['Würzburg', 'Nürnberg', 'Stuttgart'],
['Würzburg', 'Frankfurt', 'Kassel'],
]
--
A* corrected heuristics: {'status': 'found', 'max_entries': 5, 'loops': 4}
```