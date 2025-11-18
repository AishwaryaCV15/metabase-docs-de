---
Titel: Anleitung zum Schreiben eines Metabase-Treibers
---


# Anleitung zum Schreiben eines Metabase-Treibers


Folgendes Szenario: Sie lieben Metabase. Es hat Ihr Leben verändert. Aber Sie haben einige Daten in einer Visual Fox Pro '98-Datenbank und müssen damit Diagramme erstellen, und es könnte eine Weile dauern, bis das Metabase-Kernteam einen Treiber für Visual Fox Pro '98 schreibt. Kein Problem! Das Schreiben eines Treibers kann Spaß machen.


## Gibt es bereits einen Treiber für Ihre Datenquelle?


Bevor Sie mit der Erstellung eines neuen Treibers beginnen, sehen Sie nach, ob es bereits einen gibt, zu dem Sie beitragen können:


- [Offiziell unterstützte Treiber](../../databases/connecting.md#connecting-to-supported-databases)
- [Gemeinschaftstreiber](../community-drivers.md)


## Einrichten


Bevor Sie mit der Arbeit an einem Treiber beginnen, müssen Sie Ihre [Entwicklungsumgebung](../devenv.md) einrichten.


Ein tiefgreifendes Verständnis von Clojure ist beim Schreiben von JDBC-basierten Treibern weniger wichtig, da deren Implementierung einfacher ist - ein Großteil der Arbeit wird bereits für Sie erledigt - aber es wäre trotzdem hilfreich zu verstehen, was Dinge wie [multimethods](https://clojure.org/reference/multimethods) sind. Siehe [Arbeiten mit Clojure](../clojure.md).


## Einen Treiber schreiben


Vermeiden Sie es, direkt zu der Seite zu springen, von der Sie glauben, dass sie den Code enthält, den Sie zum Kopieren benötigen. Obwohl Metabase-Treiber oft recht klein sind (manche bestehen aus nur fünfzig Zeilen Code), sollten Sie sich genau überlegen, was in diese fünfzig Zeilen gehört. Dann fällt es Ihnen leichter, den Treiber zu schreiben, und Sie haben am Ende einen besseren Treiber.


1. [Treiber-Grundlagen](basics.md)
2. [Plugin-Manifeste](plugins.md)
3. [Implementierung von Multimethoden für Ihren Treiber](multimethods.md)
4. [Einreichen eines PR für Ihren Treiber](driver-tests.md)


## Beispieltreiber


- [Beispieltreiber](https://github.com/metabase/sample-driver)
- [Metabase-Treibermodule](https://github.com/metabase/metabase/tree/master/modules/drivers)
- [Ein Beispiel für einen Sudoku-Treiber](https://github.com/metabase/sudoku-driver)


## Ankündigungen zur Treiberentwicklung


Gelegentlich werden wir Änderungen an der Metabase vornehmen, die sich auf die Datenbanktreiber auswirken. Wir werden versuchen, alle Beteiligten so weit wie möglich vorzuwarnen. Wenn Sie über mögliche Treiberänderungen benachrichtigt werden möchten, abonnieren Sie die [Metabase Community Authors mailing list](http://eepurl.com/gQcIO9).

