---
Titel: "Personenübersicht"
redirect_from:
- /docs/latest/administration-guide/sso
- /docs/latest/personen-und-gruppen
---


# Personenübersicht


Benutzerkonten, Gruppen und Authentifizierung. Zu den Berechtigungen siehe [Übersicht über die Berechtigungen](../permissions/start.md).


## [Bearbeiten Ihrer Kontoeinstellungen](./account-settings.md)


Bearbeiten Sie Ihr Profil und Ihr Passwort, und sehen Sie sich Ihre Login-Historie an.


## [Personen und Gruppen verwalten](./managing.md)


Admin-Kontrollen für die Einrichtung von Benutzerkonten und deren Einteilung in Gruppen.


## [Passwortkomplexität ändern](./changing-password-complexity.md)


Bringen Sie die Leute dazu, längere und komplexere Passwörter zu verwenden.


## [Ändern der Sitzungsdauer](./changing-session-expiration.md)


Teilen Sie der Metabase mit, wie lange sie warten soll, bevor sie die Benutzer auffordert, sich erneut anzumelden.


## Authentifizierung


Metabase bietet mehrere Optionen für die Authentifizierung.


> Wenn Sie eine 2-Schritt- oder Multi-Faktor-Authentifizierung (2FA oder MFA) für Ihre Metabase einrichten müssen, sollten Sie eine der unten aufgeführten SSO-Optionen verwenden.


### SSO für Metabase Open Source und Starter-Pakete


- [Google-Anmeldung](./google-sign-in.md)
- [LDAP](./ldap.md)


### SSO für Metabase Pro und Enterprise-Pakete


Mit den [Pro- und Enterprise-Plänen](https://www.metabase.com/pricing/) haben Sie mehr Optionen, um viele Personen und Gruppen zu orchestrieren.


- [JWT][jwt]
- Erweiterte LDAP-Funktionen
- [Gruppenmitgliedschaftsfilter](./ldap.md#ldap-group-membership-filter)
- [Benutzerattribute synchronisieren](./ldap.md#syncing-user-attributes-with-ldap)
- [SAML][saml]
- [Auth0][saml-auth0]
- [Microsoft Entra ID][azure-ad]
- [Google][saml-google]
- [Keycloak][saml-keycloak]
- [Okta][saml-okta]


## [API-Schlüssel](./api-keys.md)


Erstellen von Schlüsseln zur Authentifizierung von API-Aufrufen.


## [User provisioning](./user-provisioning.md)


Die Metabase unterstützt die Bereitstellung von Benutzern über das SCIM-Protokoll.


[azure-ad]:. /saml-azure.md
[google-sign-in]:. /google-and-ldap.md#enabling-google-sign-in
[jwt]:. /authenticating-with-jwt.md
[ldap]:. /google-and-ldap.md#enabling-ldap-authentication
