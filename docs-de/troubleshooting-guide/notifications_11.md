---
Titel: Fehlersuche Meldungen
---


# Fehlersuche bei Benachrichtigungen


Die Metabase sendet keine Benachrichtigungen wie Alarme oder Dashboard-Abonnements.


**Ursache:**


Wenn lange laufende Abfragen in der Warteschlange stecken bleiben, können sie die Ausführung aller anderen Abfragen blockieren.


**Zu ergreifende Schritte:**


1. Erhöhen Sie die Größe des Benachrichtigungs-Thread-Pools mit der Umgebungsvariablen [`MB_NOTIFICATION_THREAD_POOL_SIZE`](../configuring-metabase/environment-variables.md#mb_notification_thread_pool_size) und starten Sie den Server neu.


Sie können zum Beispiel die Größe des Thread-Pools auf ` 10` setzen, indem Sie die Umgebungsvariable setzen:
`MB_NOTIFICATION_THREAD_POOL_SIZE=10`.


Hinweis: Denken Sie daran, dass die Metabase alte, fehlgeschlagene Aufgaben nicht aufgreift, so dass Sie die Auswirkungen dieser Änderung im nächsten Benachrichtigungszeitraum sehen werden.

