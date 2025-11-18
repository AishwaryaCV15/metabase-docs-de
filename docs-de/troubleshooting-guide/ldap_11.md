---
## LDAP-Beispielkonfiguration
---

Sie können Metabase mit LDAP testen, indem Sie diese "docker-compose" Definition verwenden:


```Yml
version: "3.7"
Dienste:
metabase-ldap:
image: metabase/metabase:latest
container_name: metabase-ldap
Rechnername: metabase-ldap
Volumes:
- /dev/urandom:/dev/random:ro
Ports:
- 3000:3000
Netzwerke:
- metanet1
Umgebung:
- "MB_LDAP_BIND_DN=cn=admin,dc=example,dc=org"
- "MB_LDAP_ENABLED=true"
- "MB_LDAP_GROUP_BASE=cn=Leser"
- "MB_LDAP_HOST=openldap"
- "MB_LDAP_PASSWORD=adminpassword"
- "MB_LDAP_PORT=1389"
- MB_LDAP_USER_BASE=ou=users,dc=example,dc=org"
- "MB_LDAP_ATTRIBUTE_EMAIL=uid"
# Wir verwenden dasselbe Feld für E-Mail und Vorname, nur damit dieses Beispiel ohne Änderungen an den LDAP-Objekten funktioniert
- "MB_LDAP_ATTRIBUTE_FIRSTNAME=uid"
- "MB_LDAP_ATTRIBUTE_LASTNAME=sn"
openldap:
image: bitnami/openldap:2.4.57
hostname: openldap
container_name: openldap
Ports:
- 1389:1389
Umgebung:
- LDAP_ADMIN_USERNAME=admin
- LDAP_ADMIN_PASSWORD=adminpassword
- LDAP_USERS=user01@metabase.com,user02@metabase.com
- LDAP_PASSWORDS=Passwort1!,Passwort2!
- LDAP_PORT_NUMBER=1389
- LDAP_ROOT=dc=example,dc=org
- LDAP_USER_DC=benutzer
- LDAP_GROUP=Leser
Netzwerke:
- metanet1
Netzwerke:
metanet1:
Treiber: Brücke
```


Wenn Sie der Metabase keine Umgebungsvariablen übergeben und die Umgebung manuell konfigurieren möchten, können Sie im Admin Panel unter "Einstellungen" die Option "Authentifizierung" und dann "LDAP-Konfiguration" auswählen und die folgenden Werte eingeben:


-`USERNAME ODER DN`:`cn=admin,dc=example,dc=org`
-`PASSWORT`: `adminpassword`
-`USER SEARCH BASE`: `ou=users,dc=example,dc=org`
-`BENUTZER-FILTER`: `(&(objectClass=inetOrgPerson)(|(uid={login})))`
-`GROUP SEARCH BASE`: `cn=readers`


Für den `USER FILTER` können Sie den Standardwert belassen, der nach der Benutzer-ID sowohl im Feld "uid" als auch im Feld "email" suchen wird.


## Verwandte Software zur Fehlerbehebung


Wenn Sie auf ein Problem stoßen, überprüfen Sie, ob Sie sich bei Ihrem LDAP-Verzeichnis anmelden und Abfragen mit einer Software wie [Apache Directory Studio][apache-directory-studio] durchführen können. Damit können Sie den gesamten LDAP-Baum sehen und die Protokolle Ihrer LDAP-Anwendung einsehen, um die durchgeführten Abfragen zu sehen.


<h2 id="current-limitations">Aktuelle Einschränkungen</h2>


- Wenn Sie Metabase Enterprise mit einer MySQL-Datenbank und aktiviertem LDAP verwenden, stellen Sie sicher, dass Sie die Synchronisierung von Binärfeldern aus Ihrem LDAP-Verzeichnis mithilfe der Umgebungsvariablen `MB_LDAP_SYNC_USER_ATTRIBUTES_BLACKLIST` deaktivieren. Wenn Sie dies nicht tun, stoßen Sie möglicherweise an die 60K-Feldgrößenbeschränkung des Textfeldes in MySQL, was Sie daran hindert, Benutzer anzulegen oder diese Benutzer anzumelden.


[apache-directory-studio]: https://directory.apache.org/studio/


## Stecken Sie immer noch fest?


Wenn Sie Ihr Problem nicht mit Hilfe der Anleitungen zur Fehlerbehebung lösen können:


- Suchen oder fragen Sie die [Metabase-Community](https://discourse.metabase.com/).
- Suchen Sie nach [bekannten Fehlern oder Einschränkungen](./known-issues.md).

