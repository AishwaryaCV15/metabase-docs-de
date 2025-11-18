---
Titel: Eingebettete Analytik SDK - Plugins
---


# Eingebettetes Analyse-SDK - Plugins


{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}


Das Metabase Embedded analytics SDK unterstützt Plugins zur Anpassung des Verhaltens von Komponenten. Diese Plugins können in einem globalen Kontext oder auf Basis einzelner Komponenten verwendet werden.


## Globale Plugins


Um ein Plugin global zu verwenden, fügen Sie das Plugin in die "pluginsConfig" -Eigenschaft des "MetabaseProvider" ein:


``typescript
{% include_file "{{ dirname }}/snippets/plugins/global-plugins.tsx" snippet="example" %}
```


## Komponenten-Plugins


Um ein Plugin für eine einzelne Komponente zu verwenden, übergeben Sie das Plugin als Prop an die Komponente:


````typescript
{% include_file "{{ dirname }}/snippets/plugins/component-plugins.tsx" snippet="example" %}
```


## Weitere Lektüre


- [Interaktive Frage-Plugins](./questions.md#interactive-question-plugins)
- [Dashboard-Plugins](./dashboards.md#dashboard-plugins)

