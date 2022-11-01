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

$$HAUSTIERE = \{fuchs, pferd, schnecken, zebra, hund\}$$  

$$V = \{FARBEN, NATIONALITÄTEN, GETRÄNKE, ZIGARETTEN, HAUSTIERE\}$$
### Domänen
Gleich für alle i; representiert die 5 Häuser:  

$$D_i = \{1,2,3,4,5\}$$  

### Constraints
$$C = \{\\
gelb\neq blau,\\
gelb\neq rot,\\
gelb\neq grün,\\
gelb\neq weiß,\\
blau\neq rot,\\
blau\neq grün,\\
blau\neq grün,\\
blau\neq weiß,\\
rot\neq grün,\\
rot\neq weiß,\\
grün\neq weiß,\\
\}$$
