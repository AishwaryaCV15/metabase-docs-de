---
Titel: Fragen zur Fehlerbehebung und Dashboard-Visualisierungen
---


# Frage zur Fehlerbehebung und Dashboard-Visualisierungen


Prüfen Sie zunächst, ob Ihre aktuellen Browsereinstellungen mit Metabase kompatibel sind:


1. Löschen Sie Ihren Browser-Cache und aktualisieren Sie die Seite.
2. Deaktivieren Sie alle Erweiterungen und Plugins. Laden Sie die Seite erneut.
3. Versuchen Sie es ein letztes Mal - öffnen Sie Ihre Seite in einer privaten/inkognitiven Sitzung oder in einem anderen Browser.


## Formatierung der Dashboard-Karten


1. Vergewissern Sie sich, dass Sie die Änderungen in denEinstellungen der [Karte](../dashboards/introduction.md#changing-a-cards-visualization-settings) vornehmen und speichern (_nicht_ die Einstellungen der ursprünglichen Frage).
2. [Die Visualisierungseinstellungen Ihrer Karte zurücksetzen](../dashboards/introduction.md#resetting-a-cards-visualization-settings).


**Erläuterung**


Die Visualisierungseinstellungen auf einer Karte sind unabhängig von den Einstellungen auf der ursprünglichen Frage. Wenn Sie zum ersten Mal eine Frage erstellen, wird der ausgewählte Visualisierungstyp zusammen mit der Abfrage gespeichert. Wenn Sie diese Frage zu einem Dashboard hinzufügen, zeigt das Dashboard standardmäßig dieselbe Visualisierung an wie die ursprüngliche Frage. Sie können den ursprünglichen Visualisierungstyp überschreiben, indem Sie die [Visualisierungseinstellungen der Karte](../dashboards/introduction.md#changing-a-cards-visualization-settings) verwenden.


## Visualisierung von SQL-Fragen


Gehen Sie zu Ihrer SQL-Frage und [ändern Sie den Visualisierungstyp](../questions/visualizations/visualizing-results.md) in eine Tabelle. Prüfen Sie dann, ob eine der folgenden Situationen auf die Rohabfrageergebnisse zutrifft:


- [Aggregationen (Zählungen, Summen usw.) sind falsch](https://www.metabase.com/learn/sql/debugging-sql/sql-logic#aggregated-results-counts-sums-etc-are-wrong).
- [Ergebnisse haben doppelte Zeilen](https://www.metabase.com/learn/sql/debugging-sql/sql-logic-duplicated-data).
- [Ergebnisse haben fehlende Zeilen](https://www.metabase.com/learn/sql/debugging-sql/sql-logic-missing-data).


**Erläuterung**


Wenn Ihre Frage oder Dashboardkarte durch eine handgeschriebene [SQL-Abfrage](../questions/native-editor/writing-sql.md) und nicht durch den [query builder](../questions/query-builder/editor.md) gespeist wird, reagiert Ihre Visualisierung empfindlicher auf Änderungen in den zugrunde liegenden Daten (z. B. umbenannte Felder oder das plötzliche Auftreten eines wilden Nullwertes). Um mehr darüber zu erfahren, lesen Sie [Häufige Gründe für unerwartete Abfrageergebnisse](https://www.metabase.com/learn/sql/debugging-sql/sql-logic#common-reasons-for-unexpected-query-results).


Wenn Sie Probleme mit Dingen wie SQL-Syntaxfehlern oder [SQL-Variablen](https://www.metabase.com/glossary/variable#example-variable-in-metabase) haben, finden Sie unter [Troubleshooting SQL questions](./sql.md) weitere Hilfe.


## Verwandte Probleme


- [Meine Daten und Zeiten sind falsch](./timezones.md).
- [Mein Dashboard ist langsam oder wird nicht geladen](./my-dashboard-is-slow.md).
- [Ich kann meine Frage oder mein Dashboard nicht anzeigen oder bearbeiten](./cant-view-or-edit.md).
- [Ich kann meine Tabellen nicht sehen](./cant-see-tables.md).


## Stecken Sie immer noch fest?


Wenn Sie Ihr Problem nicht mit Hilfe der Anleitungen zur Fehlerbehebung lösen können:


- Suchen oder fragen Sie die [Metabase-Community](https://discourse.metabase.com/).
- Suchen Sie nach [bekannten Fehlern oder Einschränkungen](./known-issues.md).

