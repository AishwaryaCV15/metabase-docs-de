---
Titel: Einführung in die Erlaubnis
redirect_from:
- /docs/latest/administration-guide/05-setting-permissions
---


# Einführung in die Rechtevergabe


Es wird immer sensible Informationen in Ihren Daten geben, und glücklicherweise bietet Metabase eine Reihe von Tools, mit denen Sie sicherstellen können, dass die Mitarbeiter Ihres Teams nur die Daten sehen, die sie sehen sollen.


Wenn Sie sich stattdessen fragen, welche Daten Metabase im Unternehmen einsehen kann, lesen Sie unsere Seite zu [Datenschutz und Sicherheit](https://www.metabase.com/security).


## Wichtige Punkte zu den Berechtigungen


- Berechtigungen werden für [Gruppen](../people-and-groups/managing.md#groups) erteilt, nicht für Personen. Sie können jedoch Benutzerattribute definieren, um Berechtigungen auf einzelne Personen anzuwenden.
- Personen können in mehr als einer Gruppe sein.
- Wenn eine Person mehreren Gruppen angehört, wird ihr der _freizügigste_ Zugriff für alle ihre Gruppen gewährt. Wenn eine Person zum Beispiel in drei Gruppen ist und eine dieser Gruppen den Zugriff "Kuratieren" auf eine Sammlung hat, dann hat diese Person den Zugriff "Kuratieren" auf diese Sammlung.
- Standardmäßig sind alle Personen in der Gruppe "Alle Benutzer", daher sollten Sie den Zugriff für diese Gruppe sperren, bevor Sie anderen Gruppen Berechtigungen erteilen. Glücklicherweise warnt Sie Metabase, wenn die Gruppe "Alle Benutzer" über mehr Rechte verfügt als die Gruppe, die Sie einschränken möchten.


## Für was Sie Berechtigungen festlegen können


- [Datenberechtigungen](./data.md) - Steuerung des Zugriffs auf Datenbanken, Schemata und Tabellen, einschließlich:
- [Daten anzeigen](./data.md#view-data-permissions)
- [Abfragen erstellen](./data.md#abfragen-erstellen-ermächtigen)
- [Ergebnisse herunterladen](./data.md#download-results-permissions)
- [Datenbank verwalten](./data.md#manage-database-permissions)
- [Sammlungsberechtigungen][Sammlungen] - Steuerung des Zugriffs auf Fragen, Dashboards, Modelle, Metriken, Ereignisse und Zeitleisten
- [Anwendungsberechtigungen](application.md) - Steuerung des Zugriffs auf Verwaltungsfunktionen (nur Pro- und Enterprise-Tarife):
- [Registerkarte "Einstellungen" im Verwaltungsbereich](application.md#settings-access)
- [Überwachungswerkzeuge und Fehlerbehebung](application.md#monitoring-access)
- [Dashboard-Abonnements und -Warnungen](application.md#subscriptions-and-alerts)
- [Snippet-Ordner-Berechtigungen][snippet-folders] - Steuerung des Zugriffs auf SQL-Snippet-Ordner (verfügbar für Pläne mit Snippet-Ordnern)


## Tools für die Verwaltung von Multi-Tenant-Konfigurationen


Auf einer hohen Ebene bietet Metabase mehrere Ansätze für die Verwaltung von Berechtigungen für verschiedene Multi-Tenant-Konfigurationen, je nachdem, wie Sie Ihre Daten aufgeteilt haben.


### Ihre Kunden teilen sich eine einzige Datenbank


Mit [Daten-Sandboxen](./data-sandboxes.md) können Sie Sicherheit auf Zeilen- und Spaltenebene anwenden, so dass jeder Kunde nur seine Daten in den Tabellen sieht.


### Jeder Kunde hat seine eigene Datenbank


Mit [Datenbank-Routing](./database-routing.md) können Sie eine Frage einmal erstellen und Metabase je nach Kunde eine Abfrage an eine andere Datenbank senden lassen.


### Sie möchten die Berechtigungen lieber über die Datenbank selbst verwalten


Mit [Connection impersonation](./impersonation.md) können Sie Berechtigungen mit Rollen verwalten, die Sie in Ihrer Datenbank definieren.


[Sammlungen]:. ./exploration-und-organisation/sammlungen.md
[Dashboard-Abonnements]:. ./Dashboards/Abonnements.md
[daten-berechtigungen]:. /data.md
[data-sandboxing]:. /data-sandboxes.md
[permissions]: https://www.metabase.com/learn/metabase-basics/administration/permissions
[Sandkasten-Spalten]: https://www.metabase.com/learn/metabase-basics/administration/permissions/data-sandboxing-column-permissions
[sandbox-rows]: https://www.metabase.com/learn/metabase-basics/administration/permissions/data-sandboxing-row-permissions
[slack-integration]:. ./configuring-metabase/slack.md
[Snippet-Ordner]:. ./Fragen/native-editor/snippets.md
[Fehlerbehebungs-Berechtigungen]:. ./Fehlerbehebungs-Leitfaden/Erlaubnisse.md

