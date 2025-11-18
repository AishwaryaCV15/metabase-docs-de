---
Titel: Konfigurieren von Berechtigungen für die Einbettung
Zusammenfassung: Erfahren Sie, welches Berechtigungstool Sie verwenden sollten, je nachdem, ob sich Ihre Kundendaten in einer Datenbank befinden oder über mehrere Datenbanken verteilt sind.
---


# Konfigurieren von Berechtigungen für die Einbettung


Sie können eine einzige Metabase verwenden, um die Berechtigungen für alle Ihre Kunden zu verwalten. Welches Metabase-Berechtigungstool Sie verwenden, hängt davon ab, wie Sie Ihre Kundendaten speichern.


- [Eine Datenbank für alle Kunden (gemischte Setups)](#one-database-for-all-customers-commingled-setups)
- [Eine Datenbank pro Kunde](#one-database-per-customer)
- [Ein Schema pro Kunde](#multiple-schemas-one-schema-per-customer)


## Eine Datenbank für alle Kunden (gemischte Einstellungen)


Wenn sich alle Ihre Kundendaten im selben Schema und in denselben Tabellen befinden (oft als "Datenvermischung" bezeichnet):


| Tenant_ID | Spalte 1 | Spalte 2 |
| --------- | -------- | -------- |
| A |... |... |
| B |... |... |
| C |... |... |


Sie können verwenden:


- [Data sandboxing](./data-sandboxes.md), um Zeilen und Spalten einzuschränken.
- [Connection impersonation](./impersonation.md), um die von Ihrer Datenbank festgelegten Rollen zu imitieren. Impersonation ist eine gute Wahl, wenn Sie Native SQL-Zugriff auf Ihre Daten gewähren wollen.


### Zeilen auf der Grundlage der Mieter-ID einschränken


Angenommen, Sie haben eine Tabelle mit dem Namen **Daten**, die wie folgt aussieht:


| Tenant_ID | Metrics | Insights |
| --------- | ------- | -------- |
| A |... |... |
| B |... |... |
| C |... |... |


Um eine gefilterte Version von **Daten** für verschiedene Tenants auf der Grundlage einer ` Tenant_ID` anzuzeigen, können Sie eine [einfache Sandbox](./data-sandboxes.md#types-of-data-sandboxes) erstellen.


Das bedeutet, dass Tenant A die Zeilen sieht, in denen `Tenant_ID = A` ist, und Tenant B die Zeilen, in denen `Tenant_ID = B` ist.


Die grundlegende Sandbox funktioniert folgendermaßen:


1. **Erstellen Sie eine Gruppe**, z. B. "Sandboxed Tenants", und fügen Sie die Metabase-Konten der Personen zu dieser Gruppe hinzu.
2. **Fügen Sie ein Benutzerattribut hinzu**. Fügen Sie für jedes Personenkontoein Benutzerattribut hinzu(../people-and-groups/managing.md#adding-a-user-attribute) wie z.B. `Tenant_ID`, wobei der Wert des Benutzerattributs auf "A", "B" oder "C" gesetzt wird.
3. **Sandbox der Tabelle** für die Gruppe, um die [Sicherheit auf Zeilenebene basierend auf Benutzerattributen] anzuwenden(./data-sandboxes.md#types-of-data-sandboxes).


### Einschränkung von Spalten auf der Grundlage der Mieterschaft


Angenommen, Ihre **Einblicke**-Spalte ist eine Premium-Funktion, und Mieter B ist der einzige Kunde, der dafür bezahlt, diese **Einblicke** zu sehen.


| Tenant ID | Metrics | Insights |
| --------- | ------- | --------------------------------- |
| A |... | {% include svg-icons/cross.svg %} |
| B |... |... |
| C |... | {% include svg-icons/cross.svg %} |


Um A und C daran zu hindern, die Spalte "Einblicke" zu sehen, können Sie eine [benutzerdefinierte Sandbox](./data-sandboxes.md#types-of-data-sandboxes) erstellen, um sowohl die Zeilen als auch die Spalten einzuschränken, die sie sehen, wenn sie die Tabelle betrachten.


1. **Erstellen Sie eine Gruppe** mit dem Namen "Metrics-Only Tenants".
2. **Fügen Sie Tenants A und C zur Gruppe**hinzu. Beachten Sie, dass Sie beim Sandboxing der Tabelle**Daten** für verschiedene Gruppen darauf achten, dass jedes Metabase-Konto nur zu einer einzigen Gruppe gehört.
3. [Fügen Sie ein Benutzerattribut hinzu](../people-and-groups/managing.md#adding-a-user-attribute) wie `Tenant_ID`, wobei der Wert des Benutzerattributs auf "A" oder "C" gesetzt wird.
4. Als Nächstes erstellen Sie eine SQL-Frage unter Verwendung der Tabelle **Daten** wie folgt:
