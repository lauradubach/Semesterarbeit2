# Teil 3 Realisieren
Kommen wir zur Umsetzung des Projektes. In diesem Teil wird genau beschrieben, wie alles realisiert wurde und wie ich vorgegangen bin. Es wird getestet und geprüft, sodass ersichtlich ist, ob alles funktioniert wie es soll. Falls Probleme aufgetaucht sind, werden diese ebenfalls beschrieben, inklusive Lösungsweg.

- [Teil 3 Realisieren](#teil-3-realisieren)
- [Realisieren](#realisieren)
  - [Implementierungsplan](#implementierungsplan)
  - [Modellierung in Camunda](#modellierung-in-camunda)
  - [Entwicklung Python Skript](#entwicklung-python-skript)
    - [Aufgetretene Probleme](#aufgetretene-probleme)
  - [Fallbacksolution](#fallbacksolution)
- [Kontrollieren](#kontrollieren)
  - [Testing](#testing)
    - [Testkonzept](#testkonzept)
    - [Testdurchführung](#testdurchführung)
  - [Schulung Team](#schulung-team)


# Realisieren
Nun wird die Realisierung beschrieben. Zuerst wird ein Plan erstellt, wie genau Implementiert wird und danach wird umgesetzt. Eine Fallbacksolution wird ebenfalls beschrieben, imfalle das etwas schief geht.

## Implementierungsplan
Hier wird grob dargestellt, wie in diesem Projekt vorgegangen wird.

![Implementierungsplan](../Pictures/Implementierungsplan.png)

Der Implementierungsplan für den automatisierten Onboarding-Prozess zeigt die sieben Hauptarbeiten die ausgeführt werden. Jeder dieser Arbeiten ist sher wichtig für das Gesamtprodukt und keines davon kann weggelassen werden.

## Modellierung in Camunda

## Entwicklung Python Skript

Meine API Permissions:

![APIPermissions](<../Pictures/API Permissions.png>)

### Aufgetretene Probleme

Zuerst hatte ich folgendes Problem:

![Problem1](../Pictures/Problem1.png)

Lösung: 

`pip install requests`

Danach hatte ich folgendes Problem:

![Problem2](../Pictures/Problem2.png)

Lösung: 

`pip install msal`

Nun hatte ich folgendes Problem:

![Problem3](../Pictures/Problem3.png)

Um herauszufinden was das Problem ist, habe ich folgendes Skript verwendet:

```bash
import msal

# Konfigurationsvariablen

CLIENT_ID = "xxxx"
CLIENT_SECRET = "xxxx"
TENANT_ID = "xxxx"

# Authority-URL
authority = f"https://login.microsoftonline.com/{TENANT_ID}"

# MSAL-Client erstellen
app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=authority,
    client_credential=CLIENT_SECRET)

# Versuche, ein Access Token abzurufen
print("Hole Access Token...")
response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

# Debugging: Gibt die vollständige Antwort aus
print("Antwort vom Token-Abruf:")
print(response)

# Überprüfe, ob das Token erfolgreich abgerufen wurde
if "access_token" in response:
    print("Access Token erfolgreich abgerufen!")
    access_token = response["access_token"]
else:
    print("Fehler beim Abrufen des Access Tokens:")
    print(response.get("error"))
    print(response.get("error_description"))
    print("Prozess abgebrochen.")
    exit()  # Beendet das Skript`
```

Nun konnte ich im debugger sehen dass es am Client secret lag und ich den value hinterlegen muss und nicht die ID.

Nun erhielt ich aber folgenden Error:

```bash
Fehler beim Erstellen des Benutzers: 403 - {"error":{"code":"Authorization_RequestDenied","message":"Insufficient privileges to complete the operation.","innerError":{"date":"2024-12-05T12:07:47","request-id":"3957016c-f6a7-40df-a671-84f3581a6e7a","client-request-id":"3957016c-f6a7-40df-a671-84f3581a6e7a"}}}
```
Als ich den Fehlercode gesucht habe, habe ich herausgefunden, dass mir noch folgende Rechte gefehlt haben:

- `User.ReadWrite.All`
- `Directory.ReadWrite.All`

Nun musste ich beim Admin die Freigabe dieser Rechte anfragen. Sobald ich die Rechte hatte, hat es geklappt:

![Lösung](../Pictures/Lösung.png)

Das vollendete Skript ist hier abgelegt:

> [Skript](https://github.com/lauradubach/Semesterarbeit2/tree/main/Skripts)


## Fallbacksolution

Da das Projekt auf dem Demo Tenant durchgeführt wurde, benötigt es keine Fallbacksolution. Falls etwas nicht klappt während dem Betrieb kann das Onboarding einfach Manuell durchgeführt werden, bis das Problem behoben wird.

# Kontrollieren
Die Kontrolle ist sehr wichtig. So kann versichert werden, dass das Enprodukt funktioniert und alle Tests erfolgreich geklappt haben.

## Testing
### Testkonzept
| Testperson | Datum |
| ---------- | ----- |

### Testdurchführung

## Schulung Team

Das ganze Support Team erhält täglich Onboardings. So muss dem Team gezeigt werden, wie genau Sie das Skript verwenden müssen. Dies kann am besten in einer kurzen Demo-Session demonstriert werden. Es wird gezeigt wie die Daten eingetragen werden und wie dann das Skript ausgeführt wird. 

> Back [Page](https://github.com/lauradubach/Semesterarbeit2/blob/main/Sites/Teil%202%20Vorbereitung.md)
>
> Next [Page](https://github.com/lauradubach/Semesterarbeit2/blob/main/Sites/Teil%204%20Abschluss.md)