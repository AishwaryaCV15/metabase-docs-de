---
Titel: Fehlersuche bei Berechtigungen
---


# Fehlersuche bei Berechtigungen


Wenn jemand die falsche Zugriffsebene für ein Dashboard oder eine Frage hat, kann das Problem von Gruppeneinstellungen, Sammlungsberechtigungen oder Datenberechtigungen herrühren.


1. Gehen Sie zu **Admin** > **Personen** und prüfen Sie, ob die Person in [mehr als einer Gruppe mit unterschiedlichen Berechtigungen][Gruppenberechtigungen] ist.
2. Wenn eine Person** Fragen oder Dashboardsnicht anzeigen oder bearbeiten kann, siehe [Fehlersuche bei Sammlungsberechtigungen](#troubleshooting-collection-permissions).
3. Wenn eine Person **nicht auf Daten**zugreifen kann, wie z. B. Schema, Tabellen, Zeilen oder Spalten, siehe [Troubleshooting data-permissions](#troubleshooting-data-permissions).


Wenn Sie ein anderes Problem haben, siehe [verwandte Probleme](#do-you-have-a-different-problem).


## Fehlersuche bei Sammlungsberechtigungen


- [Eine Benutzergruppe kann nicht auf ein Dashboard in einer Sammlung zugreifen, für die sie Berechtigungen hat][troubleshooting-viewing-editing].
- [Eine Benutzergruppe kann Sammlungen anzeigen, die eingeschränkte Daten enthalten][collections-restricted-data].


## [Fehlerbehebung Datenberechtigungen][troubleshooting-data-permissions]


### Zeilen- und Spaltenberechtigungen


- [troubleshooting-data-sandboxing] [troubleshooting-data-sandboxing].


### Native Abfrage (SQL) Berechtigungen


- [Eine Benutzergruppe kann nicht auf den SQL-Editor zugreifen][sql-access].
- [Eine Benutzergruppe mit SQL-Berechtigungen wird nicht durch ihre Daten-Sandbox eingeschränkt][sql-sandboxing].


### Tabellen- oder Schema-Berechtigungen


- [Eine Benutzergruppe hat den falschen Zugriff auf eine Tabelle oder ein Schema][table-schema-access].
- [Fehlermeldung "Zugriff verweigert" erhalten][permission-denied].
- [Überprüfen des Zugriffs von jemandem auf eine Tabelle oder ein Schema](./data-permissions.md#checking-someones-access-to-a-table-or-schema)


## Haben Sie ein anderes Problem?


- [Ich kann meine Frage oder das Dashboard nicht speichern][Proxies].
- [Ich kann meine Tabellen nicht sehen](./cant-see-tables.md).


## Stecken Sie immer noch fest?


Wenn Sie Ihr Problem nicht mit Hilfe der Anleitungen zur Fehlerbehebung lösen können:


- Suchen oder fragen Sie in der [Metabase-Community][Diskurs].
- Suchen Sie nach [bekannten Fehlern oder Einschränkungen][known-issues].

[admin-permissions]: ../permissions/start.md
[collection-permissions]: ../permissions/collections.md
[collections-restricted-data]: ./data-permissions.md#a-user-group-can-view-collections-that-contain-restricted-data
[connecting-database]: ../databases/connecting.md
[data-browser]: https://www.metabase.com/learn/metabase-basics/querying-and-dashboards/data-browser
[data-model]: ../data-modeling/metadata-editing.md
[data-permissions]: ../permissions/data.md
[discourse]: https://discourse.metabase.com/
[group-permissions]: ../permissions/introduction.md#key-points-regarding-permissions
[known-issues]: ./known-issues.md
[learn-permissions]: https://www.metabase.com/learn/metabase-basics/administration/permissions
[permission-denied]: ./data-permissions.md#getting-a-permission-denied-error-message
[proxies]: ./proxies.md
[sandboxing]: ./sandboxing.md
[setting-collection-permissions]: ../permissions/collections.md#setting-permissions-for-collections
[sql-access]: ./data-permissions.md#a-user-group-cant-access-the-sql-editor
[sql-sandboxing]: ./sandboxing.md#is-the-question-written-in-sql
[table-schema-access]: ./data-permissions.md#a-user-group-has-the-wrong-access-to-a-table-or-schema
[troubleshooting-data-permissions]: ./data-permissions.md
[troubleshooting-data-sandboxing]: ./sandboxing.md
[troubleshooting-viewing-editing]: ./cant-view-or-edit.md
