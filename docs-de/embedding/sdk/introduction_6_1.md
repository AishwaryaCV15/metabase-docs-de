---
Titel: SDK für eingebettete Analytik
redirect_from:
- /docs/latest/embedding/sdk
---


# Embedded analytics SDK


{% include plans-blockquote.html feature="Embedded analytics SDK" sdk=true %}


Mit dem Embedded analytics SDK können Sie einzelne Metabase-Komponenten in React einbetten (z. B. eigenständige Diagramme, Dashboards, den Query Builder und mehr). Sie können den Zugriff und die Interaktivität pro Komponente verwalten und haben erweiterte Anpassungsmöglichkeiten für ein nahtloses Styling.


## Beispielanwendungen, die mit dem Embedded Analytics SDK erstellt wurden


Um Ihnen eine Vorstellung davon zu geben, was mit dem SDK möglich ist, haben wir unter [metaba.se/sdk-demo](https://metaba.se/sdk-demo) Beispielseiten zusammengestellt. Navigieren Sie zwischen verschiedenen Shop-Websites. Schauen Sie sich diese an und stöbern Sie in den Abschnitten "Produkte" und "Analysen" sowie in den Optionen "Neue Frage" und "Neues Dashboard".


(../images/pug-and-play.png)[Mops und Spiel, Beispielanwendung mit eingebettetem Analyse-SDK].


Hier ist der [Shoppy Quellcode](https://github.com/metabase/shoppy).


## Voraussetzungen für das Embedded Analytics SDK


- React-Anwendung mit React 18 oder React 19.
- Nodejs 20.x oder höher.
- Metabase Version 1.52 oder höher.


## Schnellstarts


- [Quickstart](./quickstart.md) (Wenn Sie eine Metabase und eine App haben)
- [Quickstart CLI](./quickstart-cli.md) (Wenn Sie eine Anwendung, aber keine Metabase haben)
- [Quickstart mit React-Beispielanwendung](./quickstart-with-sample-app.md) (Wenn Sie beides nicht haben)


## Installation


Um das SDK zu verwenden, müssen Sie das SDK in der Metabase aktivieren und in Ihrer React-Anwendung installieren.


### Aktivieren Sie das SDK in der Metabase


Aktivieren Sie das SDK für eingebettete Analysen, indem Sie zu**Admin-Einstellungen > Einstellungen > Einbettung** gehen. Schalten Sie das SDK ein und klicken Sie auf**Konfigurieren**. Geben Sie die Ursprünge für Ihre Website oder Anwendung ein, in die Sie das SDK einbetten möchten, getrennt durch ein Leerzeichen. Localhost ist automatisch enthalten.


### Installieren Sie das SDK in Ihrer React-Anwendung


Sie können das Embedded analytics SDK für React über npm installieren. Stellen Sie sicher, dass Sie das dist-Tag verwenden, das Ihrer Metabase-Version entspricht, z. B.: 53-stable für Metabase 53:


````bash
npm install @metabase/embedding-sdk-react@53-stable
```


oder mit Garn:


````bash
yarn add @metabase/embedding-sdk-react@53-stable
```


### Auflösen von `@types/react` Versionskonflikten


In seltenen Fällen kann es vorkommen, dass das Embedding SDK und Ihre Anwendung unterschiedliche Hauptversionen von`@types/react` verwenden, was zu TypeScript-Konflikten führt.


Um eine einzige "@types/react"- Version für alle Abhängigkeiten zu erzwingen, fügen Sie einen "overrides"- (npm) oder "resolutions" -Abschnitt (Yarn) zu Ihrer "package.json" hinzu und geben Sie die "@types/react"-Version an, die Ihre Anwendung verwendet.
