---
Titel: Fehlersuche bei Modellen
---


# Fehlersuche bei Modellen


Welche Art von Problem haben Sie mit Ihrem [model][model-docs]?


## Kann kein Modell erstellen


Wenn Sie [die Modell-Schaltfläche][Modell-Schaltflächen-Bild] (drei Quadrate) nicht sehen:


1. Prüfen Sie, ob Sie eine Metabase-Version von 0.42.0 oder höher verwenden, indem Sie oben rechts auf dem Bildschirm auf das Symbol **Zahnrad** > **Über Metabase** klicken.
2. Löschen Sie Ihren Browser-Cache.
3. Bitten Sie Ihren Metabase-Administrator, den Proxy-Cache zu löschen (falls Sie einen solchen verwenden).


## Änderungen an einem Modell können nicht bearbeitet oder gespeichert werden


Wenn Ihre Änderungen an den Metadaten eines Modells oder der zugrunde liegenden Frage nicht angezeigt werden:


1. Aktualisieren Sie Ihren Browser, um sicherzustellen, dass Sie keine zwischengespeicherten Ergebnisse sehen.
2. Suchen Sie nach [bekannten Modellproblemen][known-issues-models], indem Sie das Label `Querying/Models` verwenden. Weitere Informationen finden Sie unter [How to find a known bug or limitation][known-issues].


## Die Modellleistung ist schlecht


1. Verwenden Sie die Modellpersistenz.


- Metabase kann [zurück in Ihr Data Warehouse schreiben][model-persistence]. Wenn Sie die Modellpersistenz aktivieren, liest Metabase eine vorberechnete und materialisierte Version des Modells direkt aus der Datenbank, anstatt die Abfrage von Grund auf neu auszuführen. Bitte beachten Sie, dass diese Option nur in einigen unterstützten Data Warehouses verfügbar ist.


2. Optimieren Sie die zugrunde liegende gespeicherte Frage oder SQL-Abfrage.


- [Weniger Daten anfordern][limit-data-learn].
- Bei Modellen, die SQL-Fragen verwenden, [suchen Sie mit SQL EXPLAIN nach Engpässen][sql-explain-learn].


3. Optimieren Sie Ihre Datenbankschemata.


-Aggregieren Sie Daten im Voraus mit Übersichtstabellen][summary-tables-learn].
-Häufig abgefragte Spalten indizieren][indexes-learn].
- [Daten denormalisieren][denormalize-data-learn].
- [Ansichten materialisieren][materialize-views-learn].
- [Daten aus JSON herausziehen und ihre Schlüssel in Spalten einfügen][flatten-json-learn].


4. Optimieren Sie Ihr(e) Data Warehouse(s) oder Datenbank(en).


- [Replizieren Sie Ihre Datenbank][replicate-database-learn].
- [Betrachten Sie eine für Analysen optimierte Datenbank][analytics-database-learn].


**Erläuterung**


Modelle sind eine Art von gespeicherten Fragen. Sie sind daher nur so schnell wie die ursprüngliche Frage oder SQL-Abfrage.


Wenn Sie die Leistung eines Modells verbessern möchten, können Sie Optimierungen auf Abfrage-, Schema- oder Datenbankebene vornehmen (je nach Ihren Datenberechtigungen, Ihrem technischen Fachwissen und Ihrer Bereitschaft zum Tüfteln).


## Stecken Sie immer noch fest?


Wenn Sie Ihr Problem nicht mit Hilfe der Anleitungen zur Fehlerbehebung lösen können:


- Suchen oder fragen Sie in der [Metabase-Community][Diskurs].
- Suchen Sie nach [bekannten Modellproblemen][known-issues-models] mit dem Label `Querying/Models`. Weitere Informationen finden Sie unter [How to find a known bug or limitation][known-issues].

[analytics-database-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#consider-a-database-optimized-for-analytics
[denormalize-data-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#denormalize-data
[discourse]: https://discourse.metabase.com/
[flatten-json-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#pull-data-out-of-json-and-slot-its-keys-into-columns
[indexes-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#index-frequently-queried-columns
[known-issues]: ./known-issues.md
[known-issues-models]: https://github.com/metabase/metabase/labels/Querying%2FModels
[limit-data-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#ask-for-less-data
[materialize-views-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#materialize-views-create-new-tables-to-store-query-results
[model-button-image]: https://www.metabase.com/learn/images/models/model-icon.png
[model-docs]: ../data-modeling/models.md
[replicate-database-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#replicate-your-database
[sql-explain-learn]: https://www.metabase.com/learn/sql/working-with-sql/sql-best-practices#explain
[summary-tables-learn]: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/making-dashboards-faster#aggregate-data-ahead-of-time-with-summary-tables
[troubleshooting-sandboxing]: ./sandboxing.md
[model-persistence]: ../data-modeling/model-persistence.md
