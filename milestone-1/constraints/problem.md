## Rätsel
```
01. Der Engländer lebt im roten Haus.
02. Der Spanier hat einen Hund.
03. Der Ukrainer trinkt gern Tee.
04. Das grüne Haus steht (direkt) links vom weißen Haus.
05. Im grünen Haus wird Kaffee getrunken.
06. Die Person, die Gurken isst, hat einen Leguan
07. Der Bewohner des mittleren Hauses trinkt Milch.
08. Der Bewohner des gelben Hauses mag Pizza.
09. Der Norweger wohnt im ersten Haus.
10. Der Tofu-Esser wohnt neben der Person mit dem Papagei.
11. Dr Mann mit dem Pferd lebt neben der Person, die Pizza mag.
12. Der Erdbeeren-Esser trinkt Orangensaft.
13. Der Norweger wohnt neben dem blauen Haus.
14. Der Japaner isst gerne Kebab.
15. Der Tofu-Esser hat einen Nachbarn, der Wasser trinkt.
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

$$D_i = \{1,2,3,4,5\}$$  

### Constraints
$$C = \text{\{}$$
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
zebra\neq hund,\\
$$
$$\text{\}}$$
