---
Titel: "Embedded analytics SDK - Dashboards"
---


# Embedded analytics SDK - Dashboards


{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}


Sie können ein interaktives, bearbeitbares oder statisches Dashboard einbetten.


**Bitte beachten Sie, dass das Einbetten von mehreren Dashboards auf derselben Seite noch nicht unterstützt wird.


## Einbetten eines Dashboards


Sie können ein Dashboard einbetten, indem Sie eine der Dashboard-Komponenten verwenden:


### `StaticDashboard`


Eine leichtgewichtige Dashboard-Komponente. Verwenden Sie diese Komponente, wenn Sie Ergebnisse anzeigen möchten, ohne dass die Benutzer mit den Daten interagieren können.


#### API-Referenz
- [Komponente](./api/StaticDashboard.html)
- [Requisiten](./api/StaticDashboardProps.html)


#### Props


{% include_file "{{ dirname }}/api/snippets/StaticDashboardProps.md" snippet="properties" %}


### `InteractiveDashboard`


Eine Dashboard-Komponente mit Drilldowns, Klickverhalten und der Möglichkeit, Fragen anzuzeigen und anzuklicken. Verwenden Sie diese Komponente, wenn Sie Personen die Möglichkeit geben wollen, ihre Daten zu erkunden.


#### API-Referenz
- [Komponente](./api/InteractiveDashboard.html)
- [Requisiten](./api/InteractiveDashboardProps.html)


#### Props


{% include_file "{{ dirname }}/api/snippets/InteractiveDashboardProps.md" snippet="properties" %}


### `EditableDashboard`


Eine Dashboard-Komponente mit den Funktionen, die in der Komponente "InteractiveDashboard" verfügbar sind, sowie der Möglichkeit, Fragen, Layout und Inhalt innerhalb Ihres Dashboards hinzuzufügen und zu aktualisieren. Verwenden Sie diese Komponente, wenn Sie Personen die Möglichkeit geben wollen, Ihre Dashboards zu ändern, z. B. in einem Verwaltungsbereich in Ihrer Anwendung.


#### API-Referenz
- [Komponente](./api/EditableDashboard.html)
- [Requisiten](./api/EditableDashboardProps.html)


#### Props


{% include_file "{{ dirname }}/api/snippets/EditableDashboardProps.md" snippet="properties" %}


## Beispiel eingebettetes Dashboard mit `InteractiveDashboard` Komponente


````Typescript
{% include_file "{{ dirname }}/snippets/dashboards/interactive-dashboard.tsx" %}
```


## Höhe des Dashboards anpassen


Standardmäßig nehmen die Dashboard-Komponenten die volle Seitenhöhe (100vh) ein. Sie können dies mit benutzerdefinierten Stilen außer Kraft setzen, die über die Requisiten "style" oder "className" übergeben werden.
