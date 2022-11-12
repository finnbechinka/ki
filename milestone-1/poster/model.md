Semester: 1, 3, 5  
  
Vorlesungen (je 2h): 
1. 2 x Mathe 1, Einf.i.d.Programm.m.Skriptsprachen, techn. Informatik, Einführung i. d. Informatik, OOP
2. Software Engineering, Embedded Systems, Datenbanken, Systemprogrammierung, Software Projektmanagement 
3. Sicherheit u. Zuverlässigkeit, Webengineering, Compilerbau, Künstl. Intelligent, Technical English, Computer Vision  
  
Räume: B 50-H, B 70-H, H 10-H, H 107, D 317, D 318, D 319, D 320, D 327, D 328, A 250-H, J 101  

## CSP
### Variablen
$Semester = \{1, 3, 5\}$

$Dozenten = \{\}$ 

$Vorlesungen = \{\}$

$Räume = \{\text{B 50-H}, \text{B 70-H}, \text{H 10-H}, \text{H 107}, \text{D 317}, \text{D 318}, \text{D 319}, \text{D 320}, \text{D 327}, \text{D 328}, \text{A 250-H}, \text{J 101} \}$ 
### Domänen
Combination aus Tag und Zeit?  

$Tage = \{0, 1, 2, 3, 4\}$ 

$Zeiten = \{8, 10, 12, 14, 16, 18\}$ 

$D_i = Tage \times Zeiten = \{(0, 8), ..., (4, 18)\}$
### Constraints
Pro Tag um die Gleiche Uhrzeit nur eine Vorlesung pro Raum.   
Pro Dozent nur eine Vorlesung zur gleichen Zeit.  