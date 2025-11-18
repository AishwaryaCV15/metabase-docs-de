---
Titel: "Embedded analytics SDK - Erscheinungsbild"
---


# Embedded analytics SDK - Aussehen


{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}


Sie können Ihre eingebetteten Metabase-Komponenten mit einem Thema gestalten.


Hier ist ein Beispiel, das die verschiedenen verfügbaren Styling-Optionen zeigt:


```ts
{% include_file "{{ dirname }}/snippets/appearance/theme.ts" %}
```


### Anpassen von Lade- und Fehlerkomponenten


Sie können Ihre eigenen Komponenten für Lade- und Fehlerzustände bereitstellen, indem Sie ` loaderComponent` und ` errorComponent` als Requisiten für ` MetabaseProvider` angeben.


```tsx
{% include_file "{{ dirname }}/snippets/auftritt/anpassung-lader-und-komponenten.tsx" snippet="imports" %}


{% include_file "{{ dirname }}/snippets/auftritt/anpassung-lader-und-komponenten.tsx" snippet="beispiel" %}
```


## Beschränkungen


- CSS-Variablen werden noch nicht unterstützt. Wenn Sie möchten, dass Metabase CSS-Variablen unterstützt, stimmen Sie bitte diesem [Feature Request](https://github.com/metabase/metabase/issues/59237) zu.
- Farben, die in den Visualisierungseinstellungen für eine Frage festgelegt werden, haben Vorrang vor den Themenfarben.

