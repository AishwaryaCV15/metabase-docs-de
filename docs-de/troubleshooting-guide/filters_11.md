---
Titel: Fehlersuche bei Filtern
---


# Fehlerbehebung bei Filtern


Es ist immer eine gute Idee, mit einer kurzen Überprüfung der Richtigkeit zu beginnen:


1. Löschen Sie Ihren Browser-Cache.
2. Aktualisieren Sie die Seite.
3. Öffnen Sie Ihre Frage oder das Dashboard in einem Inkognito-Fenster.


## Dashboard-Filter


Wenn ein Dashboard-Filter keine oder die falschen Ergebnisse liefert:


1. Klicken Sie auf das Symbol **Bleistift**, um in den Bearbeitungsmodus zu wechseln.
2. Klicken Sie auf das Symbol **Zahnrad** neben Ihrem Filter-Widget.
3. Vergewissern Sie sich, dass Sie unter **Spalte zum Filtern nach** eine Spalte für Ihren Filter ausgewählt haben.
4. Wenn Sie die richtige **Spalte zum Filtern nicht finden können**, oder wenn Sie "Keine Ergebnisse" erhalten, wenn Sie den Filter anwenden:
- Verlassen Sie den Bearbeitungsmodus und klicken Sie auf eine Dashboard-Karte, um zur _ursprünglichen Frage_ zu gelangen.
- Befolgen Sie die Schritte zur Fehlerbehebung unter [Fragenfilter](#question-filters).


## Frage-Filter


Wenn ein Fragenfilter keine oder die falschen Ergebnisse liefert:


1. Vergewissern Sie sich, dass die Frage die Spalte enthält, nach der Sie filtern möchten.
2. Überprüfen Sie, ob die Spalte tatsächlich den/die Wert(e) enthält, nach denen Sie filtern wollen. Sie können dies tun durch:
- Zahlen- oder Datumsspalten sortieren,
- Erstellen eines "enthält"-Filters für Zeichenkettenspalten, oder
- fragen Sie Ihren Datenbankadministrator.
3. Bitten Sie Ihren Metabase-Administrator, Ihnen bei der Überprüfung zu helfen, ob:
- Metabase mit Ihrer Datenbank auf demneuesten Stand ist(../databases/sync-scan.md),
- die Spalte in der Metabase [sichtbar] ist(../data-modeling/metadata-editing.md#column-visibility),
- Sie haben die richtigen [Datenberechtigungen](../permissions/data.md), um auf die Spalte zuzugreifen.


### Sonderfälle


Wenn Sie Probleme mit dem Filtern nach einer:


- [Benutzerdefinierte Spalte](../questions/query-builder/editor.md#custom-columns): überprüfen Sie, ob der benutzerdefinierte Ausdruck wie erwartet funktioniert. Ihr benutzerdefinierter Ausdruck könnte zum Beispiel leere Werte zurückgeben, obwohl Sie Zahlen erwarten.
- [SQL-Feldfilter](../questions/native-editor/sql-parameters.md#the-field-filter-variable-type): Vergewissern Sie sich, dass Sie die richtige [Feldfilter-Syntax](../questions/native-editor/sql-parameters.md#field-filter-syntax) verwenden, und lesen Sie dann [Troubleshooting SQL variables](./sql.md#sql-variables-and-field-filters).


**Erläuterung**


Wenn wir zum ersten Mal einen Filter einrichten, müssen wir den Filter mit einer Spalte verknüpfen. Wenn wir die falschen Annahmen über die Werte oder den Datentyp einer Spalte treffen, wird der Filter überhaupt nicht funktionieren. Wenn sich eine Spalte auf der Datenbankseite ändert, kann der Filter plötzlich nicht mehr funktionieren.


Nehmen wir zum Beispiel an, wir möchten einen Filter mit dem Namen "Select Product ID" erstellen, der mit einer Spalte mit dem Namen **Product ID** verknüpft ist. Der Filter funktioniert nicht, wenn eines der folgenden Dinge passiert:


- Unsere Frage enthält nicht die Spalte**Produkt-ID**.
- Wir geben die Zahl 4 in den Filter "Produkt-ID auswählen" ein, obwohl die Spalte**Produkt-ID** nur die Werte 1, 2 und 3 enthält.
- Die**Produkt-ID** wird in der Datenbank oder auf der Seite "Tabellenmetadaten" in etwas anderes umbenannt.
-**Produkt-ID** wird aus der Datenbank gelöscht oder auf der Seite "Tabellenmetadaten" ausgeblendet.
-**Produkt-ID** ist eine benutzerdefinierte Spalte, die nicht wie erwartet funktioniert.
- Wir haben keine Datenberechtigung für den Zugriff auf die Spalte**Produkt-ID**.
- Wir haben "Produkt-ID auswählen" zu einem numerischen Filter gemacht, aber**Produkt-ID** ist eine Zeichenkettenspalte (siehe den folgenden Abschnitt).

## Zeit-, ID- und Zahlenfilter


So debuggen Sie Dashboard- und Fragenfilter, die Zeitstempel, UUIDs oder numerische Daten enthalten:


1. Suchen Sie den [Datentyp](https://www.metabase.com/learn/grow-your-data-skills/data-fundamentals/data-types-overview) der Spalte, nach der Sie filtern möchten. Sie finden diese Information in:
- der [Datenreferenz](../exploration-and-organization/data-model-reference.md),
- die [Tabellen-Metadaten-Seite](../data-modeling/metadata-editing.md) (nur für Administratoren), oder
- direkt aus der Datenbank.
2. Wandeln Sie die Spalte in einen Datentyp um, der dem gewünschten [Filtertyp] entspricht(../questions/query-builder/filters.md#filter-types). Sie können:
- [Strings oder Zahlen in Daten umwandeln](../data-modeling/metadata-editing.md#casting-to-a-spezifical-data-type) auf der Seite Tabellenmetadaten, oder
- den Datentyp der Spalte in Ihrer Datenbank ändern und das Datenbankschema [neu synchronisieren](../databases/sync-scan.md#manually-syncing-tables-and-columns).


Wenn Sie kein Metabase-Administrator sind, müssen Sie möglicherweise Ihren Administrator bitten, Ihnen bei einigen dieser Schritte zu helfen.


**Erläuterung**


Metabase muss den Datentyp einer Spalte kennen, um Ihnen eine kuratierte Auswahl an Filtertypen präsentieren zu können. Manchmal werden diese Spalten falsch getippt - wenn eine Spalte Ihre Zahlen als Strings speichert, zeigt Ihnen Metabase nur Text- oder Kategoriefilter (mit Optionen wie "ist", "ist nicht") anstelle von Zahlenfiltern (mit Optionen wie "größer als", "kleiner als").


Vor allem Zeitstempel sind die Wurzel allen Übels, also haben Sie bitte Geduld mit Ihrem Metabase-Administrator (oder mit sich selbst!), wenn Sie versuchen, den richtigen Datentyp zu finden.


## Feldfilter in BigQuery und Oracle


Wenn Sie bei der Verwendung von Feldfiltern in BigQuery oder Oracle einen Fehler erhalten, vergewissern Sie sich, dass Sie die richtige Syntax für die FROM-Klausel verwenden. Siehe [Feldfilter in BigQuery und Oracle](../questions/native-editor/sql-parameters.md#field-filters-in-bigquery-and-oracle).


## Fehlende oder falsche Filterwerte


Wenn Ihr Filter-Dropdown-Menü die falschen Werte für eine Spalte anzeigt:


1. Gehen Sie zu **Admin-Einstellungen** > **Tabellen-Metadaten**.
2. Suchen Sie Ihre Datenbank, Tabelle und Spalte.
3. Klicken Sie auf das Symbol **Zahnrad** auf der rechten Seite des Einstellungsfeldes einer Spalte.
4. Blättern Sie zu **Feldwerte im Cache**.
5. Optional: Klicken Sie auf **Zwischengespeicherte Feldwerte verwerfen**.
6. Klicken Sie auf **Dieses Feld erneut scannen**.


**Erläuterung**


Metabase [scans](../databases/sync-scan.md#how-database-scans-work) ermitteln die Werte für Ihre Filter-Dropdown-Menüs durch Abfrage und Zwischenspeicherung der ersten 1.000 eindeutigen Datensätze aus einer Tabelle. Sie können veraltete Filterwerte sehen, wenn Ihre Tabellen im Vergleich zu Ihrem [Scan-Zeitplan] häufiger aktualisiert werden(../databases/sync-scan.md#scanning-for-filter-values).


## Verwandte Themen


- [Fehlerbehebung bei verknüpften Filtern](./linked-filters.md)
- [Fehlerbehebung bei SQL-Variablen und Feldfiltern](./sql.md#sql-variables-and-field-filters)
- [Fehlerbehebung bei Datums- und Zeitangaben](./timezones.md)
- [Erstellen von Dropdown-Filtern](../data-modeling/metadata-editing.md#changing-a-search-box-filter-to-a-dropdown-filter)
- [SQL-Filter erstellen](../questions/native-editor/sql-parameters.md)


## Stecken Sie immer noch fest?


Wenn Sie Ihr Problem nicht mit Hilfe der Anleitungen zur Fehlerbehebung lösen können:

- Search or ask the [Metabase community](https://discourse.metabase.com/).
- Search for [known bugs or limitations](./known-issues.md).
