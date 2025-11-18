---
Titel: Einführung in die Einbettung
redirect_from:
- /docs/latest/administration-guide/13-embedding
---


# Einführung in die Einbettung


Sie können Metabase-Tabellen, -Diagramme und -Dashboards - sogar den Query Builder der Metabase - in Ihre Website oder Anwendung einbetten.


Hier sind die verschiedenen Möglichkeiten, wie Sie Metabase einbetten können.


{% include shared/in-page-promo-einbettung-workshop.html %}


## Eingebettetes Analytik-SDK mit React


Mit dem [Embedded analytics SDK](./sdk/introduction.md) können Sie einzelne Metabase-Komponenten mit React einbetten (z. B. eigenständige Diagramme, Dashboards, den Query Builder und mehr). Sie können den Zugriff und die Interaktivität pro Komponente verwalten und haben erweiterte Anpassungsmöglichkeiten für ein nahtloses Styling.


**Wann Sie das SDK für eingebettete Analysen verwenden sollten**: Sie möchten die größtmögliche Kontrolle darüber haben, wie Sie Metabase in Ihre React-App einbetten.


## Interaktive Einbettung


Die interaktive Einbettung ist die einzige Art der Einbettung, die [mit SSO und Datenberechtigungen](./interactive-embedding.md)integriert ist, um einen echten Selbstbedienungszugriff auf die zugrunde liegenden Daten zu ermöglichen.


**Wann sollte man interaktive Einbettung verwenden**: Sie möchten [mandantenfähige, selbstverwaltete Analysen anbieten](https://www.metabase.com/blog/why-full-app-embedding). Mit der interaktiven Einbettung können Benutzer ihre eigenen Fragen, Dashboards, Modelle und mehr in ihrer eigenen Daten-Sandbox erstellen.


## Statische Einbettung


Die [statische Einbettung](./static-embedding.md), auch bekannt als signierte Einbettung, ist eine sichere Methode zur Einbettung von Diagrammen und Dashboards.


**Wann sollten Sie statische Einbettungen verwenden**: Sie möchten keine Ad-hoc-Abfragen oder Diagramm-Drill-Throughs anbieten. Um für den Betrachter relevante Daten zu filtern, können Sie statische Einbettungen mit [gesperrten Parametern](./static-embedding-parameters.md#locked-parameters-limit-the-values-available-to-other-editable-parameters) verwenden.


## Öffentliche Links und Einbettungen


Wenn Sie Ihre Daten mit den guten Menschen im Internet teilen möchten, können Administratoren einen [öffentlichen Link](./public-links.md) erstellen oder eine Frage oder ein Dashboard direkt in Ihre Website einbetten.


** ÖffentlicheLinks und Einbettungen**: Öffentliche Links und Einbettungen sind gut für einmalige Diagramme und Dashboards. Admins können sie verwenden, wenn Sie jemandem nur ein Diagramm oder Dashboard zeigen möchten, ohne anderen Personen Zugang zu Ihrer Metabase zu gewähren. Und es ist Ihnen egal, wer die Daten sieht; Sie wollen diese Statistiken für alle zugänglich machen.


## Vergleich der Einbettungstypen


| Action | [Embedded analytics SDK](./sdk/introduction.md) | [Interactive](./interactive-embedding.md) | [Static](./static-embedding.md) | [Public](../embedding/public-links.md) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------- | ------------------------------- | -------------------------------------- |
| Diagramme und Dashboards anzeigen | ✅ | ✅ | ✅ | ✅ |
| Interaktive [Filterwidgets] anzeigen(https://www.metabase.com/glossary/filter-widget) | ✅ | ✅ | ✅ | ✅ |
| Export results\* | ✅ | ✅ | ✅ | ✅ |
| Daten mit [gesperrten Filtern] einschränken(./static-embedding-parameters.md#restricting-data-in-a-static-embed-with-locked-parameters) | ❌ | ❌ | ✅ | ❌ |
| Daten mit [sandboxes] einschränken(../permissions/data-sandboxes.md) | ✅ | ✅ | ❌ | ❌ |
| Verwenden Sie das [Drill-Through-Menü](https://www.metabase.com/learn/metabase-basics/querying-and-dashboards/questions/drill-through) | ✅ | ✅ | ❌ | ❌ |
| Selbstbedienung über [query builder](https://www.metabase.com/glossary/query_builder) | ✅ | ✅ | ❌ | ❌ |
| Anzeigen der Nutzung von Einbettungen mit [usage analytics](../usage-and-performance-tools/usage-analytics.md) | ✅ | ✅ | ❌ | ❌ |
| [Aktionen auf Dashboards](../dashboards/actions.md) | ✅ | ✅ | ❌ | ❌ |
| Einzelne Metabase-Komponenten einbetten | ✅ | ❌ | ❌ | ❌ |
