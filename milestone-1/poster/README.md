# Projekt 1: Poster
(Abgabe: 16.11.22)

## Stundenplanung

Betrachten Sie das Stundenplanproblem:

![timetable](timetable.bmp)

Es gibt verschiedene Jahrgänge/Semester, verschiedene Vorlesungen (die von bestimmten Dozenten
gehalten werden) und unterschiedliche Räume. Nehmen Sie den Stundenplan Ihres Studiengangs
für das Wintersemester (betrachten Sie also alle Semester und nicht nur Ihren Jahrgang) und
betrachten Sie zur Vereinfachung nur die Vorlesungen. Gehen Sie zur Vereinfachung ebenfalls
davon aus, dass alle Räume gleich groß (und ausreichend groß) sind und dass die Vorlesungen
immer in festen 2h-Zeitfenstern geplant werden können.


1.  Listen Sie alle Eigenschaften des Problems übersichtlich auf: Welche Vorlesungen werden in
    welchem Jahrgang von welchem Dozenten angeboten, welche Räume werden dabei berücksichtigt?

2.  Lösen Sie das Problem, indem Sie entweder

    *   Gradientensuche und Simulated Annealing, oder
    *   Genetische/Evolutionäre Algorithmen mit verschiedenen Parametereinstellungen, oder
    *   Constraintsolving mit `BT_Search` und AC-3

    implementieren und anwenden. Sie können gern auch die passenden Java-Klassen in [`aimacode/aima-java`]
    bzw. die passenden Python-Klassen in [`aimacode/aima-python`] als Ausgangspunkt nutzen.[^aima]

    Wenn das Problem sofort beim ersten oder zweiten Schritt gelöst ist, machen Sie es etwas
    komplexer: Reduzieren Sie die Zahl der verfügbaren Räume und/oder lassen Sie einen Dozenten
    mehrere Module machen. Wenn es zu lange braucht, vereinfachen Sie das Problem ein wenig:
    Geben Sie zusätzliche Räume hinzu, verteilen Sie die Arbeit auf mehrere Dozenten, entfernen
    Sie einige Kurse pro Jahrgang.

3.  Erstellen Sie ein DIN-A2-Poster, auf dem Sie Ihr Vorgehen, die Modellierung und wichtige
    Code-Fragmente und die Ergebnisse übersichtlich präsentieren. Beschränken Sie sich dabei
    auf die wesentlichen Aussagen.

    Sie finden eine gute Anleitung sowie passende Vorlagen im Blog
    ["How to create beautiful and effective academic posters in PowerPoint"]. Sie _können_ diese
    Vorlagen nutzen (müssen es aber nicht).


Abzugeben ist der Sourcecode sowie das Poster (als **PDF**). Sie stellen das Poster in der Übung
bzw. im Praktikum vor und geben sich dann anschließend gegenseitig Feedback. Sie haben
**pro Person 8 Minuten Zeit für die Vorstellung Ihres Posters**. Für das abgegebene Poster (PDF)
und die Vorstellung Ihrer Arbeit erhalten Sie zusätzlich noch bis zu 10 Punkten vom Dozenten-Team.

**Bewertungs-/Feedback-Kriterien**:

1.  Modellierung: Werden die wesentlichen Aspekte des Problems bei der Modellierung berücksichtigt?
2.  Gestaltung:
    -   Ist das Poster optisch ansprechend gestaltet?
    -   Werden die Gestaltungselemente sinnvoll und sparsam eingesetzt?
3.  Lesbarkeit:
    -   Ist das Poster gut lesbar?
    -   Sind die wichtigsten Thesen zusammengefasst und vorgestellt?
4.  Nachvollziehbarkeit:
    -   Lässt sich die geleistete Arbeit nachvollziehen?
    -   Gibt es einen (inhaltlichen) "roten Faden" vom Problem über die Modellierung und die
        Implementierung zu den Experimenten und den Ergebnissen sowie einem Fazit?
5.  Zeit: Wurde die Zeitvorgabe bei der Präsentation des Posters eingehalten (8 Minuten)?
6.  Persönliches Fazit:
    -   Was hat Ihnen besonders gut an dem beurteilten Poster gefallen?
    -   Welche Aspekte könnte der/die Autor/in verbessern (und wie)?


[`aimacode/aima-java`]: https://github.com/aimacode/aima-java/tree/AIMA3e/aima-core
[`aimacode/aima-python`]: https://github.com/aimacode/aima-python
["How to create beautiful and effective academic posters in PowerPoint"]: https://www.brightcarbon.com/blog/effective-academic-posters-powerpoint/

