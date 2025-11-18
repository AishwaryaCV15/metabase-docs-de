---
Titel: Metabase logs
redirect_from:
- /docs/latest/operations-guide/log-configuration
summary: Konfigurieren Sie, wie viele Informationen die Metabase in ihren Protokollen anzeigt.
---


# Metabase logs


Metabase protokolliert standardmäßig eine ganze Reihe von Informationen. Metabase verwendet [Log4j 2](https://logging.apache.org/log4j/2.x/) unter der Haube, so dass Sie konfigurieren können, wie viele Informationen Metabase protokolliert.


## Metabase-Protokolle anzeigen und herunterladen


Sie finden die Metabase-Protokolle unter **Admin-Einstellungen** > **Fehlerbehebung** > **Protokolle**. Sie können die Protokolle nach Schlüsselwörtern filtern (z. B. "sync") und als Textdatei herunterladen.


Wenn Sie die selbst gehostete Metabase verwenden, können Sie die Protokolle auch im Terminal anzeigen.


## So lesen Sie die Metabase-Protokolle


Siehe [Wie man Logs liest](../troubleshooting-guide/server-logs.md).


## Konfigurieren der Protokollierungsebene


Metabase verwendet [log4j](https://logging.apache.org/log4j/2.x/)für die Konfiguration der Protokollierung. Hier ist die [Standardkonfiguration für die Protokollierung] der Metabase(https://github.com/metabase/metabase/blob/master/resources/log4j2.xml). Bei einigen Aufgaben zur Fehlerbehebung kann es erforderlich sein, diese Protokollierungskonfiguration zu überschreiben (z. B. um mehr Details zu Fehlern anzuzeigen). Siehe Log4j's docs für Informationen über [log levels](https://logging.apache.org/log4j/2.x/manual/customloglevels.html).


### Logging-Konfiguration vorübergehend außer Kraft setzen


Um die Protokollierungskonfiguration vorübergehend anzupassen, gehen Sie zu **Admin-Einstellungen** > **Fehlerbehebung** > **Protokolle** und klicken Sie auf **Protokollstufen anpassen**.


Sie können aus den Voreinstellungen für die Protokollierungsebene für allgemeine Fehlerbehebungsaufgaben wählen (z. B. Fehlerbehebung bei Synchronisierungsproblemen) oder Ihre eigene Konfiguration als JSON bereitstellen. Hier ist zum Beispiel eine Überschreibungskonfiguration, die die Protokollierung für die Fehlersuche bei verknüpften Filtern erhöht:


```json
{
"metabase.parameters.chain-filter": "debug",
"metabase.parameters.chain-filter.dedupe-joins": "debug"
}
```


Die Überschreibung der Verwaltungseinstellungen ist zeitlich begrenzt. Sie können auswählen, wie lange die Überschreibung gelten soll (z. B. 60 Minuten). Wenn die Überbrückungszeit abgelaufen ist, wird die Protokollierungskonfiguration auf die Standardkonfiguration zurückgesetzt (oder eine benutzerdefinierte Konfiguration, wenn Sie eine [benutzerdefinierte Protokolldatei](#use-a-custom-log-configuration-file)) verwenden).


### Eine benutzerdefinierte Protokollkonfigurationsdatei verwenden


Sie können Metabase auf eine benutzerdefinierte Protokollkonfigurationsdatei verweisen.


1. Erstellen Sie eine [Kopie der Standarddatei"log4j2.xml"](https://github.com/metabase/metabase/blob/master/resources/log4j2.xml)
2. Passen Sie sie an Ihre Bedürfnisse an.


Sie können verschiedene Protokollstufen für verschiedene Bereiche der Anwendung einstellen, z.B.:



```
<Loggers>
    <Logger name="metabase" level="INFO"/>
    <Logger name="metabase-enterprise" level="INFO"/>
    <Logger name="metabase.plugins" level="DEBUG"/>
    <Logger name="metabase.server.middleware" level="DEBUG"/>
    <Logger name="com.mchange" level="ERROR"/>

    <!-- Example: Add trace logging to the Metabase analysis process, which can help debugging trouble with syncing, fingerprinting and scanning -->
    <Logger name="metabase.sync" level="TRACE"/>

    <Root level="WARN">
      <AppenderRef ref="STDOUT"/>
    </Root>
</Loggers>
```


<!-- Beispiel: Hinzufügen von Trace-Logging zum Metabase-Analyseprozess, was bei der Fehlersuche bei Problemen mit Synchronisierung, Fingerprinting und Scanning helfen kann -->
