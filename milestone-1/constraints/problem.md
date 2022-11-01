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
