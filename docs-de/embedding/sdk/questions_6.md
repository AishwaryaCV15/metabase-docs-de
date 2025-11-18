---
Titel: "Eingebettete Analytik SDK - Fragen"
Beschreibung: Wie Sie mit dem Embedded Analytics SDK Diagramme in Ihre App einbetten.
---


# Embedded analytics SDK - Fragen


{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}


Es gibt verschiedene Möglichkeiten, wie Sie Fragen einbetten können:


- [Statische Frage](#staticquestion). Bettet ein Diagramm ein. Ein Klick auf das Diagramm führt zu nichts.
- [Interaktive Frage](#interactivequestion). Wenn Sie auf das Diagramm klicken, erhalten Sie das Drill-Through-Menü.
- [Query builder](#embedding-the-query-builder-for-creating-new-questions). Bindet den grafischen Abfragegenerator ohne vordefinierte Abfrage ein.


## Einbetten einer Frage


Sie können eine Frage einbetten, indem Sie eine der Fragekomponenten verwenden:


### `StaticQuestion`


Eine leichtgewichtige Fragekomponente. Verwenden Sie diese Komponente, wenn Sie Ergebnisse anzeigen möchten, ohne dass die Benutzer mit den Daten interagieren können.


![Statische Frage](../images/static-question.png)


Die Komponente hat eine voreingestellte Höhe, die mit dem Parameter ` height` angepasst werden kann. Um die Höhe vom übergeordneten Container zu erben, können Sie`100%` an die Höhenangabe übergeben.


#### API-Referenz
- [Komponente](./api/StaticQuestion.html)
- [Requisiten](./api/StaticQuestionProps.html)


#### Beispiel


````Typescript
{% include_file "{{ dirname }}/snippets/questions/static-question.tsx" %}
```


#### Requisiten


{% include_file "{{ dirname }}/api/snippets/StaticQuestionProps.md" snippet="properties" %}


### `InteractiveQuestion`


Verwenden Sie diese Komponente, wenn Sie den Teilnehmern die Möglichkeit geben wollen, ihre Daten zu erkunden und das Layout der Fragen anzupassen.


![Interaktive Frage](../images/interactive-question.png)


#### API-Referenz
- [Komponente](./api/InteraktiveFrage.html)
- [Requisiten](./api/InteraktiveFrageProps.html)


#### Beispiel


````Typescript
{% include_file "{{ dirname }}/snippets/questions/interactive-question.tsx" %}
```


#### Requisiten


{% include_file "{{ dirname }}/api/snippets/InteractiveQuestionProps.md" snippet="properties" %}


## Übergabe von SQL-Parametern an SQL-Fragen mit `initialSqlParameters`


Mit dem Parameter`initialSqlParameters` können Sie Parameterwerte an Fragen übergeben, die mit SQL definiert wurden, und zwar im Format `{parameter_name: parameter_value}`. Erfahren Sie mehr über [SQL-Parameter](../../questions/native-editor/sql-parameters.md).


````Typescript
{% include_file "{{ dirname }}/snippets/questions/initial-sql-parameters.tsx" snippet="example" %}
```


initialSqlParameters` kann nicht mit Fragen verwendet werden, die mit dem Query Builder erstellt wurden.


## Anpassen interaktiver Fragen


Standardmäßig bietet das Embedded Analytics SDK ein Standardlayout für interaktive Fragen, mit dem Sie Ihre Fragen anzeigen, Filter und Aggregationen anwenden und auf Funktionen innerhalb des Query Builders zugreifen können.---
Titel: "Eingebettete Analytik SDK - Fragen"
Beschreibung: Wie Sie mit dem Embedded Analytics SDK Diagramme in Ihre App einbetten.
---

# Embedded analytics SDK - Fragen

{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}

Es gibt verschiedene Möglichkeiten, wie Sie Fragen einbetten können:

- [Statische Frage](#staticquestion). Bettet ein Diagramm ein. Ein Klick auf das Diagramm führt zu nichts.
- [Interaktive Frage](#interactivequestion). Wenn Sie auf das Diagramm klicken, erhalten Sie das Drill-Through-Menü.
- [Query builder](#embedding-the-query-builder-for-creating-new-questions). Bindet den grafischen Abfragegenerator ohne vordefinierte Abfrage ein.

## Einbetten einer Frage

Sie können eine Frage einbetten, indem Sie eine der Fragekomponenten verwenden:

###  `StaticQuestion`

Eine leichtgewichtige Fragekomponente. Verwenden Sie diese Komponente, wenn Sie Ergebnisse anzeigen möchten, ohne dass die Benutzer mit den Daten interagieren können.

![Statische Frage](../images/static-question.png)

Die Komponente hat eine voreingestellte Höhe, die mit dem Parameter ` height` angepasst werden kann. Um die Höhe vom übergeordneten Container zu erben, können Sie`100%` an die Höhenangabe übergeben.

#### API-Referenz
- [Komponente](./api/StaticQuestion.html)
- [Requisiten](./api/StaticQuestionProps.html)

#### Beispiel

````Typescript
{% include_file "{{ dirname }}/snippets/questions/static-question.tsx" %}
```

#### Requisiten

{% include_file "{{ dirname }}/api/snippets/StaticQuestionProps.md" snippet="properties" %}

###  `InteractiveQuestion`

Verwenden Sie diese Komponente, wenn Sie den Teilnehmern die Möglichkeit geben wollen, ihre Daten zu erkunden und das Layout der Fragen anzupassen.

![Interaktive Frage](../images/interactive-question.png)

#### API-Referenz
- [Komponente](./api/InteraktiveFrage.html)
- [Requisiten](./api/InteraktiveFrageProps.html)

#### Beispiel

````Typescript
{% include_file "{{ dirname }}/snippets/questions/interactive-question.tsx" %}
```

#### Requisiten

{% include_file "{{ dirname }}/api/snippets/InteractiveQuestionProps.md" snippet="properties" %}

## Übergabe von SQL-Parametern an SQL-Fragen mit `initialSqlParameters`

Mit dem Parameter`initialSqlParameters` können Sie Parameterwerte an Fragen übergeben, die mit SQL definiert wurden, und zwar im Format `{parameter_name: parameter_value}`. Erfahren Sie mehr über [SQL-Parameter](../../questions/native-editor/sql-parameters.md).

````Typescript
{% include_file "{{ dirname }}/snippets/questions/initial-sql-parameters.tsx" snippet="example" %}
```

initialSqlParameters` kann nicht mit Fragen verwendet werden, die mit dem Query Builder erstellt wurden.

## Anpassen interaktiver Fragen

Standardmäßig bietet das Embedded Analytics SDK ein Standardlayout für interaktive Fragen, mit dem Sie Ihre Fragen anzeigen, Filter und Aggregationen anwenden und auf Funktionen innerhalb des Query Builders zugreifen können.

