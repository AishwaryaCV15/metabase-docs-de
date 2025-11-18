---
Titel: Die Daten und Zeiten in meinen Fragen und Diagrammen sind falsch
---


# Die Daten und Zeiten in meinen Fragen und Diagrammen sind falsch.


Sie führen Berechnungen mit Daten und Zeiten durch oder zeigen sie in Diagrammen an, aber:


- die Werte scheinen falsch zu sein, oder
- die zusammengefassten Werte sind falsch.

## Liegt das Problem an den Zeitzonen?


**Ursache:**Daten und Zeiten werden in verschiedenen Zeitzonen gespeichert, aber einige oder alle dieser Zeitzonen werden bei den Berechnungen nicht berücksichtigt (d. h. das Problem sind inkonsistente Daten).


**Zu unternehmende Schritte:**


Um dieses Problem zu lösen, benötigen Sie Antworten auf folgende Fragen:


1. Welches ist die korrekte Zeitzone der Daten, die Ihrer Meinung nach falsch angezeigt werden (d. h., wie lautet die richtige Antwort)?
2. Gibt es eine explizite Zeitzoneneinstellung für jeden Zeitstempel, oder werden einige oder alle Zeitstempel ohne Zeitzone gespeichert? Zum Beispiel enthält "1. Dezember 2019 00:00:00Z00" die Zeitzone (nach dem "Z"), aber "1. Dezember 2019" nicht.
3. In welcher Zeitzone befindet sich der Datenbankserver?
4. In welcher Zeitzone arbeitet die Metabase?


Sobald Sie diese Antworten haben, suchen Sie nach Fällen wie diesen:


1. Ihre Frage oder Ihr Diagramm vergleicht oder sortiert Werte mit inkonsistenten oder fehlenden Zeitzonen. Wenn beispielsweise die Abflug- und Ankunftszeiten eines Fluges in Ortszeit angegeben werden, kann es so aussehen, als ob der Flug ankommt, bevor er abgeflogen ist.
2. In Ihrer Frage geht es um die Aggregation von Zeitstempeln mit unterschiedlichen Zeitzonen: Die "täglichen" Gesamtwerte für den Datenverkehr auf Ihrer Website enthalten beispielsweise mehr als 24 Stunden, weil Sie die lokalen Daten aus Ostasien, Europa und Amerika verwenden.


Wenn Sie glauben, ein Problem identifiziert zu haben, sollten Sie es genauer untersuchen, um zu verstehen, welche Zeitzonenumstellung das Problem verursacht. Angenommen, Sie betrachten eine Zeitreihe mit täglichen Werten; wenn Ihr Fehler bei wöchentlichen Gesamtwerten auftritt, können Sie:


1. Wählen Sie einen bestimmten Tag, von dem Sie wissen, dass die Zahl falsch ist.
2. Klicken Sie auf den Datenpunkt in einem Diagramm oder eine Zelle in einer Ergebnistabelle und wählen Sie "Diese X sehen".
3. Öffnen Sie diese Frage in zwei weiteren Registerkarten in Ihrem Browser. Ändern Sie die Datumsfilter so, dass eine Registerkarte die Zeilen der zugrundeliegenden Tabelle vom _vorherigen_ Tag und die andere die Zeilen der zugrundeliegenden Tabelle vom _nächsten_ Tag enthält.
4. Überprüfen Sie, ob das Datumsfeld, das zur Gruppierung des Ergebnisses in der zugrunde liegenden Anzeige verwendet wird, korrekt ist. Wenn es sich von dem unterscheidet, was Sie in der Datenbank gespeichert haben, oder von dem, was Sie in einem anderen Tool haben, dann wird der Zeitstempel insgesamt falsch umgewandelt. Dies geschieht häufig, wenn Sie ein Datum oder eine Uhrzeit verwenden, die keine explizite Zeitzone enthalten.
5. Wenn die zugrundeliegenden Zeitstempel korrekt sind (was sie sein sollten, wenn sie explizite Zeitzonen haben), werden die einzelnen Zeiten wahrscheinlich zu Tagen in einer anderen Zeitzone als der von Ihnen gewünschten gruppiert.
6. Um herauszufinden, in welche Zeitzone sie umgerechnet werden, ändern Sie die Zeiten in den Datumsfiltern der jeweiligen Frage, indem Sie die Startzeit und das Startdatum um eine Stunde nach hinten verschieben, bis Sie entweder die richtige Zahl erhalten oder um 12 Stunden zurückgehen. (Wenn eine Ihrer Zeitzonen Indien, Neufundland oder ein anderes Land mit einer halbstufigen Zeitzone umfasst, müssen Sie dies möglicherweise in Halbstundenschritten tun).
7. Wenn das nicht funktioniert, versuchen Sie, die Start- und Endzeit um eine Stunde nach vorne zu verschieben, bis Sie entweder die richtige Zahl erhalten oder um 12 Stunden nach vorne gegangen sind.
8. Wenn Sie zu diesem Zeitpunkt den richtigen Wert haben, bedeutet dies, dass Ihre Zeitzone um die Anzahl der Stunden vorwärts oder rückwärts konvertiert wurde, die Sie den Filter manuell eingestellt haben. Ist dies der Fall, überprüfen Sie, ob der von Ihnen ermittelte Offset mit der Zeitzone des Data Warehouse oder der Zeitzone der Metabase selbst übereinstimmt.


## Ist die Zeitzone des Berichts falsch eingestellt?


**Ursache:** Falsche Zahlen in Fragen oder Diagrammen können durch eine falsche Übereinstimmung zwischen der von der Metabase verwendeten Zeitzone und der vom Data Warehouse verwendeten Zeitzone verursacht werden.


**Zu unternehmende Schritte:**


1. Überprüfen Sie die [Zeitzoneneinstellung für Berichte](../configuring-metabase/localization.md#report-timezone) unter **Admin-Einstellungen** > **Einstellungen** > **Lokalisierung**.
2. Wenn Sie eine Datenbank verwenden, die die Einstellung der Berichtszeitzone nicht unterstützt, stellen Sie sicher, dass die Zeitzone der Metabase mit der der Datenbank übereinstimmt. Die Zeitzone der Metabase ist die Zeitzone der Java Virtual Machine, die in der Regel über den Parameter "-Duser.timezone<...>" oder die Umgebungsvariable "JAVA_TIMEZONE" eingestellt wird; die genaue Einstellung hängt davon ab, wie Sie die Metabase starten. Beachten Sie, dass die Zeitzone der Metabase keine Auswirkungen auf Datenbanken hat, die eine Report Time Zone verwenden.


## Beachten SQL-Abfragen die Einstellung für die Berichtszeitzone nicht?


**Ursache:** Wir wenden derzeit keine Berichtszeitzone auf die Ergebnisse von SQL-Abfragen an.


**Zu ergreifende Schritte:**


Legen Sie in Ihrer SQL-Abfrage explizit eine Berichtszeitzone fest.


Mit PostgreSQL können Sie zum Beispiel etwas wie folgt schreiben:


```sql
SELECT spalte::TIMESTAMP AT TIME ZONE 'EST' AS spalte_est
```


Diese Anweisung wandelt die Spalte zunächst in einen Datentyp "timestamp" um und konvertiert dann den "timestamp" in einen Datentyp "timestamptz" mit der Zeitzone "EST".


## Werden Datumsangaben ohne explizite Zeitzone in einen anderen Tag konvertiert?


**Ursache:** Sie gruppieren nach einem Datum (statt nach einer Uhrzeit), dem eine Zeitzone fehlt.


**Zu ergreifende Schritte:**


1. Schauen Sie sich jedes Zeitfeld, das in Ihrer Frage verwendet wird, in der [Datenmodell-Referenz](../exploration-and-organization/data-model-reference.md) an und prüfen Sie, ob eines davon einfach ein "Datums"-Feld ist.
2. Wenn ja, vergewissern Sie sich, dass die Zeitzone des Servers mit der Zeitzone des Berichts übereinstimmt, denn wenn eine Abfrage in der Metabase ausgeführt wird, wendet der Server die konfigurierte Zeitzone auf dieses Datum an.


## Mischen Sie explizite und implizite Zeitzonen?


**Ursache:** Sie vergleichen oder rechnen mit zwei Daten, von denen eines eine explizite Zeitzone hat und das andere nicht.


**Zu unternehmende Schritte:**


1. Dies ist typischerweise bei einer Frage der Fall, die mehrere Felder verwendet: Sie filtern zum Beispiel nach einem Zeitstempel und gruppieren nach einem anderen. Überprüfen Sie die Zeitzonen der einzelnen Daten oder Zeiten, die Sie in Ihrer Frage verwenden.
2. Sie müssen die Zeitzone für jeden Wert, der keine explizite Zeitzone hat, explizit festlegen. Dies muss entweder in einer SQL-Abfrage geschehen oder durch Umwandlung der Daten in Ihrer Datenbank, um sicherzustellen, dass beide Zeitstempel Zeitzonen haben.
