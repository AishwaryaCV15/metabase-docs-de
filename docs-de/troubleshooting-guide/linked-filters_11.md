---
Titel: Meine verlinkten Filter funktionieren nicht
---


# Meine verknüpften Filter funktionieren nicht


Sie haben einen [verknüpften Filter][linked-filter-gloss] erstellt, so dass (zum Beispiel), wenn ein Dashboard sowohl einen "Bundesland"- als auch einen "Stadt"-Filter enthält, der "Stadt"-Filter nur Städte in dem durch den "Bundesland"-Filter ausgewählten Bundesland anzeigt. Allerdings:


- Ihre Karten zeigen "Kein Ergebnis" an, wenn Sie den verlinkten Filter anwenden,
- Ihr verknüpfter Filter scheint keine Wirkung zu haben, oder
- Ihr verknüpftes Filter-Widget zeigt keine Dropdown-Liste mit gefilterten Werten an.


Wenn Sie Probleme mit einem regulären [Filter-Widget][filter-widget-gloss] haben, lesen Sie bitte [diese Anleitung](./filters.md). Um Probleme mit verknüpften Filtern zu beheben, müssen Sie genau wissen, wie sie funktionieren:


## Verwendet eine verknüpfte Dashboardkarte eine SQL-Variable?


**Hauptursache**: Native/SQL-Fragen müssen eine [Feldfilter](../questions/native-editor/sql-parameters.md#the-field-filter-variable-type) Variable haben, um verknüpft werden zu können. Normale SQL-Variablen werden nicht funktionieren.


**Zu unternehmende Schritte**:


1. Aktualisieren Sie die Abfrage der Karte, um die reguläre Variable in eine [Feldfilter](../questions/native-editor/sql-parameters.md#the-field-filter-variable-type) Variable zu ändern.


Siehe [Beschränkungen der Verknüpfung von Filtern](../dashboards/linked-filters.md#limitations-of-linked-filters).


## Verstehen Sie die Direktionalität von verknüpften Filtern?


**Ursache:** Verknüpfte Filter sind eine der komplexeren Funktionen der Metabase, und viele Probleme entstehen, weil ihre Funktionsweise nicht verstanden wird.


**Zu ergreifende Maßnahmen:** Vergewissern Sie sich, dass Sie die folgenden Punkte verstanden haben und dass Ihr verknüpfter Filter unter Berücksichtigung dieser Punkte eingerichtet wurde.


1. Ein Filter ist nicht Teil einer bestimmten Frage. Stattdessen wird ein Filter zu einem Dashboard hinzugefügt und sein Wert wird zum Ausfüllen von Variablen in Fragen verwendet.


2. Damit die Metabase eine Dropdown-Liste mit möglichen Filterwerten anzeigen kann, muss sie wissen, dass die Spalte einer Kategorie entspricht. Dies geschieht automatisch, wenn die Frage aus Tabellen über den Notebook-Editor erstellt wird, da die Metabase die Tabelle und die Spalten aus der Synchronisation kennt.


3. Wenn die Frage, die die Variable enthält, in SQL geschrieben ist, muss der Autor der Frage hingegen "Feldfilter" ausgewählt haben. Außerdem muss das Feld, auf das verwiesen wird, in den Metadaten der Tabelle als Kategorie festgelegt sein, damit die Metabase eine Dropdown-Liste mit Werten anzeigt.


## Sind die Filter in der richtigen Richtung verknüpft?


**Ursache:** Die häufigste Ursache ist, dass die Filter in der falschen Richtung verknüpft wurden. Wenn Sie möchten, dass die von Filter B angezeigten Werte durch die Einstellung von Filter A eingeschränkt werden, müssen Sie die Einstellungen für Filter B und nicht für Filter A ändern, d. h., der nachgeschaltete Filter hat die Einstellung, nicht der vorgeschaltete Filter.


**Folgende Schritte sind zu unternehmen:**


1. Entfernen Sie die bestehende Verknüpfung und erstellen Sie eine neue in umgekehrter Richtung.


## Erfüllen einige Zeilen tatsächlich die vollständige Filterbedingung?


**Ursache:** Es gibt keine Zeilen, die alle Bedingungen in einem verknüpften Filter erfüllen. Wenn Sie den Namen einer Stadt manuell eingeben, die sich nicht in dem ausgewählten Bundesland befindet, erfüllt kein Datensatz beide Bedingungen.


**Folgende Schritte sind zu unternehmen:**


1. Erstellen Sie eine Frage, die nur den ersten Filter verwendet, und prüfen Sie, ob sie einige Zeilen ergibt. (Wenn dies nicht der Fall ist, wird das Hinzufügen eines zweiten Filters nicht dazu führen, dass Zeilen erscheinen).
2. Erstellen Sie eine Frage, von der Sie glauben, dass sie dasselbe Ergebnis liefert wie die Kombination der verknüpften Filtereinstellungen, die keine Daten liefert. Wenn sie das erwartete Ergebnis liefert, prüfen Sie, ob Sie Tippfehler gemacht haben und ob Sie [den richtigen Typ der Verknüpfung][join-types] verwenden.


## Bestehen alle Zeilen, die den ersten Test bestehen, auch den zweiten?


**Ursache:** In einigen Fällen erfüllen alle Zeilen, die die Bedingung des ersten Filters erfüllen, auch die Bedingung des zweiten Filters, so dass der zweite Filter keine Wirkung hat.


**Zu unternehmende Schritte:**


1. Erstellen Sie eine Frage, die die erste Filterbedingung direkt enthält (d. h. in der Frage und nicht über eine Variable), und fügen Sie dann die Bedingung des zweiten Filters hinzu. Wenn sich die Ergebnismenge nicht ändert, liegt das Problem in der Logik und nicht in den Filtern.
