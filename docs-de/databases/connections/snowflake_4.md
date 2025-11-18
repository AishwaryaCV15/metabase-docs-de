---
Titel: Schneeflocke
redirect_from:
- /docs/latest/administration-guide/databases/snowflake
---


# Schneeflocke


Um eine Datenbankverbindung hinzuzufügen, klicken Sie auf das **Zahnradsymbol** oben rechts, und navigieren Sie zu **Verwaltungseinstellungen** > **Datenbanken** > **Datenbank hinzufügen**.


Sie können diese Einstellungen jederzeit bearbeiten. Denken Sie nur daran, Ihre Änderungen zu speichern.


## Anzeigename


Der Anzeigename für die Datenbank in der Metabase-Schnittstelle.


## Kontoname oder Hostname


Sie haben die Möglichkeit, einen Kontonamen oder einen Hostnamen zu verwenden. Ihr Hostname ist die IP-Adresse Ihrer Datenbank oder ihr Domänenname (z. B. database.example.com).


Wenn Ihre URL die Region Ihrer Datenbank enthält, können Sie eine Verbindung über einen Kontonamen herstellen, andernfalls über einen Hostnamen.


### AWS


Verbinden Sie sich mit einem Kontonamen.


Geben Sie Ihren Kontobezeichner mit der Region ein, in der Ihr Snowflake-Cluster läuft. Z. B. "xxxxxxxxx.us-east-3.aws". Wenn Sie zum Beispiel Snowflake auf AWS betreiben und Ihre Konto-URL lautet `https://az12345.ca-central-1.snowflakecomputing.com`:


- `<account_identifier>`: `az12345.ca-central-1`
- `<cloud_platform>`: `aws`



Sie geben "az12345.ca-central-1.aws" als Kontonamen in Metabase ein.


Nicht alle Regionen benötigen die Kennung der Cloud-Plattform. Wenn Sie sich in ` us-west-2` befinden, würden Sie ` az12345` als Kontonamen eingeben. Die Anforderungen für die einzelnen Regionen finden Sie in [der offiziellen Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#non-vps-account-locator-formats-by-cloud-platform-and-region).


### app.snowflake.com


Verbinden Sie sich mit einem Hostnamen.


Sie erhalten Ihren Hostnamen, indem Sie zu Verwaltung > Konten gehen. Der Kontoname wird unter Konten angezeigt. Klicken Sie auf das Konto, das Sie verwenden möchten, und klicken Sie auf das Link-Symbol, um die Host-URL zu kopieren: das ist Ihr Host-Name. Auf dem Bild unten verdeckt Metabot diskret sensible Informationen. Der Link "Konto-URL kopieren" auf der rechten Seite ist das, wonach Sie suchen:


![Snowflake-Konto-URL kopieren](../images/snowflake-copy-account-url.png)


Erfahren Sie mehr über [Kontoidentifikatoren in Snowflake](https://docs.snowflake.com/en/user-guide/admin-account-identifier).


## Benutzername


Der Datenbank-Benutzername für das Konto, das Sie für die Verbindung zu Ihrer Datenbank verwenden möchten. Sie können mehrere Verbindungen zu derselben Datenbank einrichten, indem Sie verschiedene Benutzerkonten mit unterschiedlichen [Privilegien](../users-roles-privileges.md) für die Verbindung zu derselben Datenbank verwenden.


Auf Ihrer app.snowflake.com Kontoseite finden Sie Benutzer und Rollen unter Admin > Benutzer & Rollen.


## Passwort


Das Passwort für den Benutzernamen, den Sie für die Verbindung zur Datenbank verwenden.


## Privater RSA-Schlüssel (PEM)


Nicht erforderlich. Sie haben die Möglichkeit, einen **Lokalen Dateipfad** oder einen **Hochgeladenen Dateipfad** zu verwenden. Wenn Sie die Metabase Cloud nutzen, müssen Sie den**Hochgeladenen Dateipfad** wählen und Ihr Zertifikat hochladen.
