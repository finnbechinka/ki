## Rätsel
```
1. Es gibt fünf Häuser.
2. Der Engländer wohnt im roten Haus.
3. Der Spanier hat einen Hund.
4. Kaffee wird im grünen Haus getrunken.
5. Der Ukrainer trinkt Tee.
6. Das grüne Haus ist direkt links vom weißen Haus.
7. Der Raucher von Old-Gold-Zigaretten hält Schnecken als Haustiere.
8. Die Zigaretten der Marke Kools werden im gelben Haus geraucht.
9. Milch wird im mittleren Haus getrunken.
10. Der Norweger wohnt im ersten Haus.
11. Der Mann, der Chesterfields raucht, wohnt neben dem Mann mit dem Fuchs.
12. Die Marke Kools wird geraucht im Haus neben dem Haus mit dem Pferd.
13. Der Lucky-Strike-Raucher trinkt am liebsten Orangensaft.
14. Der Japaner raucht Zigaretten der Marke Parliaments.
15. Der Norweger wohnt neben dem blauen Haus.
16. Der Chesterfields-Raucher hat einen Nachbarn, der Wasser trinkt.
Wer trinkt Wasser? Wem gehört das Zebra? 
```
### Lösung
| Haus | 0 | 1 | 2 | 3 | 4 |
|------|---|---|---|---|---|
| Farbe | gelb | blau | rot | grün | weiß |
| Nationalität | Norweger | Ukrainer | Engländer | Japaner | Spanier |
| Getränk | __Wasser__ | Tee | Milch | Kaffee | O-Saft |
| Zigaretten | Kools | Chesterfield | Old Gold | Parliament | Lucky Strikes |
| Haustier | Fuchs | Pferd | Schnecken | __Zebra__ | Hund |

## CSP
### Variablen
$$FARBEN = \{gelb, blau, rot, grün, weiß\}$$  

$$NATIONALITÄTEN = \{norweger, ukrainer, engländer, japaner, spanier\}$$  

$$GETRÄNKE = \{wasser, tee, milch, kaffee, \text{o-saft}\}$$  

$$ZIGARETTEN = \{kools, chesterfield, old gold, parliament, lucky strike\}$$  

$$HAUSTIERE = \{fuchs, pferd, schnecke, zebra, hund\}$$  

$$V = \{FARBEN, NATIONALITÄTEN, GETRÄNKE, ZIGARETTEN, HAUSTIERE\}$$
### Domänen
Gleich für alle i; representiert die 5 Häuser:  

$$D_i = \{0,1,2,3,4\}$$  

### Constraints
$$
C = \{
$$

$$
engländer = rot,\\
spanier = hund,\\
kaffee = grün,\\
ukrainer = tee,\\
grün = weiß + 1 ,\\
old gold = schnecken,\\
kools = gelb,\\
milch = 2,\\
norweger = 0,\\
chesterfield = (fuchs + 1 || fuchs - 1),\\
kools = (pferd + 1 || pferd - 1),\\
lucky strike = \text{o-saft},\\
japaner = parliaments,\\
norweger = blau,\\
chesterfields = (wasser + 1 || wasser - 1),\\
$$

$$
gelb\neq blau,\\
gelb\neq rot,\\
gelb\neq grün,\\
gelb\neq weiß,\\
blau\neq rot,\\
blau\neq grün,\\
blau\neq weiß,\\
rot\neq grün,\\
rot\neq weiß,\\
grün\neq weiß,\\
$$

$$
norweger\neq ukrainer,\\
norweger\neq engländer,\\
norweger\neq japaner,\\
norweger\neq spanier,\\
ukrainer\neq engländer,\\
ukrainer\neq japaner,\\
ukrainer\neq spanier,\\
engländer\neq japaner,\\
engländer\neq spanier,\\
japaner\neq spanier,\\
$$

$$
wasser\neq tee,\\
wasser\neq milch,\\
wasser\neq kaffee,\\
wasser\neq \text{o-saft},\\
tee\neq milch,\\
tee\neq kaffee,\\
tee\neq \text{o-saft},\\
milch\neq kaffee,\\
milch\neq \text{o-saft},\\
kaffee\neq \text{o-saft},\\
$$

$$
kools\neq chesterfield,\\
kools\neq old gold,\\
kools\neq parliament,\\
kools\neq lucky strike,\\
chesterfield\neq old gold,\\
chesterfield\neq parliament,\\
chesterfield\neq lucky strike,\\
old gold\neq parliament,\\
old gold\neq lucky strike,\\
parliament\neq lucky strike,\\
$$

$$
fuchs\neq pferd,\\
fuchs\neq schnecke,\\
fuchs\neq zebra,\\
fuchs\neq hund,\\
pferd\neq schnecke,\\
pferd\neq zebra,\\
pferd\neq hund,\\
schnecke\neq zebra,\\
schnecke\neq hund,\\
zebra\neq hund
$$

$$
\}
$$

## Runtime

#### Keine Heuristiken
```
start
1:
runtime: 0.5748s
result:
Haus 1: ['fuchs', 'kools', 'norweger', 'gelb', 'wasser']
Haus 2: ['chesterfields', 'ukrainer', 'tee', 'pferd', 'blau']
Haus 3: ['englaender', 'milch', 'rot', 'oldgold', 'schnecken']
Haus 4: ['kaffee', 'japaner', 'parliament', 'gruen', 'zebra']
Haus 5: ['osaft', 'luckystrikes', 'hund', 'spanier', 'weiss']
2:
runtime: 32.9351s
result:
Haus 1: ['kools', 'fuchs', 'norweger', 'gelb', 'wasser']
Haus 2: ['tee', 'chesterfields', 'pferd', 'ukrainer', 'blau']
Haus 3: ['milch', 'rot', 'englaender', 'oldgold', 'schnecken']
Haus 4: ['zebra', 'kaffee', 'parliament', 'japaner', 'gruen']
Haus 5: ['luckystrikes', 'weiss', 'spanier', 'osaft', 'hund']
3:
runtime: 0.5289s
result:
Haus 1: ['gelb', 'wasser', 'norweger', 'fuchs', 'kools']
Haus 2: ['blau', 'chesterfields', 'tee', 'ukrainer', 'pferd']
Haus 3: ['milch', 'oldgold', 'schnecken', 'englaender', 'rot']
Haus 4: ['kaffee', 'parliament', 'gruen', 'zebra', 'japaner']
Haus 5: ['luckystrikes', 'hund', 'weiss', 'osaft', 'spanier']
4:
runtime: 1.0142s
result:
Haus 1: ['fuchs', 'kools', 'wasser', 'norweger', 'gelb']
Haus 2: ['ukrainer', 'tee', 'pferd', 'blau', 'chesterfields']
Haus 3: ['rot', 'schnecken', 'oldgold', 'milch', 'englaender']
Haus 4: ['japaner', 'gruen', 'zebra', 'kaffee', 'parliament']
Haus 5: ['hund', 'spanier', 'weiss', 'osaft', 'luckystrikes']
5:
runtime: 2.6275s
result:
Haus 1: ['fuchs', 'norweger', 'gelb', 'kools', 'wasser']
Haus 2: ['ukrainer', 'blau', 'chesterfields', 'pferd', 'tee']
Haus 3: ['oldgold', 'milch', 'englaender', 'schnecken', 'rot']
Haus 4: ['gruen', 'kaffee', 'zebra', 'japaner', 'parliament']
Haus 5: ['osaft', 'weiss', 'luckystrikes', 'hund', 'spanier']
6:
runtime: 0.4357s
result:
Haus 1: ['wasser', 'kools', 'gelb', 'norweger', 'fuchs']
Haus 2: ['chesterfields', 'pferd', 'blau', 'tee', 'ukrainer']
Haus 3: ['englaender', 'rot', 'oldgold', 'milch', 'schnecken']
runtime: 2.5450s
result:
Haus 1: ['kools', 'norweger', 'fuchs', 'gelb', 'wasser']
Haus 2: ['ukrainer', 'tee', 'blau', 'pferd', 'chesterfields']
Haus 3: ['oldgold', 'rot', 'englaender', 'milch', 'schnecken']
Haus 4: ['parliament', 'kaffee', 'japaner', 'gruen', 'zebra']
Haus 5: ['hund', 'luckystrikes', 'osaft', 'weiss', 'spanier']
10:
runtime: 0.2928s
result:
Haus 1: ['wasser', 'gelb', 'fuchs', 'norweger', 'kools']
Haus 2: ['tee', 'chesterfields', 'ukrainer', 'blau', 'pferd']
Haus 3: ['schnecken', 'oldgold', 'rot', 'milch', 'englaender']
Haus 4: ['zebra', 'japaner', 'gruen', 'kaffee', 'parliament']
Haus 5: ['spanier', 'luckystrikes', 'weiss', 'hund', 'osaft']
avg runtime: 4.7125s
end
```
#### Mit MRV
```
start
1:
runtime: 2.9324s
result:
Haus 1: ['gelb', 'wasser', 'fuchs', 'kools', 'norweger']
Haus 2: ['pferd', 'chesterfields', 'blau', 'tee', 'ukrainer']
Haus 3: ['schnecken', 'milch', 'oldgold', 'rot', 'englaender']
Haus 4: ['zebra', 'gruen', 'kaffee', 'parliament', 'japaner']
Haus 5: ['hund', 'spanier', 'osaft', 'weiss', 'luckystrikes']
2:
runtime: 19.9132s
result:
Haus 1: ['kools', 'wasser', 'gelb', 'norweger', 'fuchs']
Haus 2: ['ukrainer', 'chesterfields', 'tee', 'pferd', 'blau']
Haus 3: ['milch', 'oldgold', 'rot', 'englaender', 'schnecken']
Haus 4: ['zebra', 'parliament', 'gruen', 'kaffee', 'japaner']
Haus 5: ['hund', 'weiss', 'osaft', 'spanier', 'luckystrikes']
3:
runtime: 50.9401s
result:
Haus 1: ['kools', 'wasser', 'gelb', 'norweger', 'fuchs']
Haus 2: ['chesterfields', 'ukrainer', 'pferd', 'blau', 'tee']
Haus 3: ['oldgold', 'rot', 'englaender', 'schnecken', 'milch']
Haus 4: ['kaffee', 'zebra', 'japaner', 'gruen', 'parliament']
Haus 5: ['weiss', 'osaft', 'hund', 'luckystrikes', 'spanier']
4:
runtime: 0.3347s
result:
Haus 1: ['fuchs', 'gelb', 'kools', 'wasser', 'norweger']
Haus 2: ['chesterfields', 'ukrainer', 'blau', 'tee', 'pferd']
Haus 3: ['milch', 'oldgold', 'schnecken', 'rot', 'englaender']
Haus 4: ['kaffee', 'parliament', 'japaner', 'zebra', 'gruen']
Haus 5: ['spanier', 'luckystrikes', 'osaft', 'hund', 'weiss']
5:
runtime: 0.1640s
result:
Haus 1: ['fuchs', 'gelb', 'kools', 'wasser', 'norweger']
Haus 2: ['tee', 'ukrainer', 'blau', 'chesterfields', 'pferd']
Haus 3: ['oldgold', 'rot', 'milch', 'schnecken', 'englaender']
Haus 4: ['gruen', 'kaffee', 'japaner', 'parliament', 'zebra']
Haus 5: ['weiss', 'osaft', 'hund', 'spanier', 'luckystrikes']
6:
runtime: 5.0548s
result:
Haus 1: ['norweger', 'wasser', 'kools', 'fuchs', 'gelb']
Haus 2: ['ukrainer', 'chesterfields', 'blau', 'tee', 'pferd']
Haus 3: ['schnecken', 'milch', 'rot', 'oldgold', 'englaender']
Haus 4: ['parliament', 'japaner', 'zebra', 'kaffee', 'gruen']
Haus 5: ['osaft', 'luckystrikes', 'hund', 'spanier', 'weiss']
7:
runtime: 10.0812s
result:
Haus 1: ['fuchs', 'norweger', 'wasser', 'kools', 'gelb']
Haus 2: ['tee', 'ukrainer', 'pferd', 'blau', 'chesterfields']
Haus 3: ['oldgold', 'milch', 'schnecken', 'englaender', 'rot']
Haus 4: ['kaffee', 'zebra', 'parliament', 'gruen', 'japaner']
Haus 5: ['hund', 'luckystrikes', 'weiss', 'spanier', 'osaft']
8:
runtime: 7.7478s
result:
Haus 1: ['norweger', 'gelb', 'wasser', 'fuchs', 'kools']
Haus 2: ['chesterfields', 'pferd', 'blau', 'tee', 'ukrainer']
Haus 3: ['schnecken', 'englaender', 'rot', 'milch', 'oldgold']
Haus 4: ['kaffee', 'japaner', 'parliament', 'zebra', 'gruen']
Haus 5: ['spanier', 'hund', 'weiss', 'luckystrikes', 'osaft']
9:
runtime: 50.8806s
result:
Haus 1: ['fuchs', 'gelb', 'wasser', 'norweger', 'kools']
Haus 2: ['pferd', 'ukrainer', 'tee', 'chesterfields', 'blau']
Haus 3: ['rot', 'oldgold', 'milch', 'schnecken', 'englaender']
Haus 4: ['japaner', 'zebra', 'gruen', 'parliament', 'kaffee']
Haus 5: ['weiss', 'osaft', 'hund', 'spanier', 'luckystrikes']
10:
runtime: 1.2412s
result:
Haus 1: ['fuchs', 'gelb', 'kools', 'wasser', 'norweger']
Haus 2: ['blau', 'ukrainer', 'chesterfields', 'tee', 'pferd']
Haus 3: ['schnecken', 'oldgold', 'milch', 'rot', 'englaender']
Haus 4: ['parliament', 'japaner', 'gruen', 'kaffee', 'zebra']
Haus 5: ['luckystrikes', 'osaft', 'hund', 'spanier', 'weiss']
avg runtime: 14.9290s
end
```