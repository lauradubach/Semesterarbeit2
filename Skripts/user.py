import requests # Bibliothek für HTTP-Requests, um APIs anzusprechen
from msal import ConfidentialClientApplication # Klasse für die Authentifizierung bei Microsoft Azure AD

# Azure Konfiguration
CLIENT_ID = "xxxx"
CLIENT_SECRET = "xxxx"
TENANT_ID = "xxxx"

GRAPH_API_URL = "https://graph.microsoft.com/v1.0" # Basis-URL für Microsoft Graph API
scopes = ["https://graph.microsoft.com/.default"] # Berechtigungen für die API

# Funktion: Access Token holen
def get_access_token():
    try:
        app = ConfidentialClientApplication(
            CLIENT_ID,
            authority=f"https://login.microsoftonline.com/{TENANT_ID}",
            client_credential=CLIENT_SECRET,
        )
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        if "access_token" in result:
            return result["access_token"] # Token zurückgeben
        else:
            raise Exception("Konnte kein Access Token abrufen.")
    except Exception as e:
        print(f"Fehler beim Abrufen des Access Tokens: {e}")
        return None

# Funktion: Benutzer erstellen
def create_user(token, user_data):
    headers = {
        "Authorization": f"Bearer {token}", # Access Token für Authentifizierung
        "Content-Type": "application/json", # JSON-Daten senden
    }
    body = {
        "accountEnabled": True, # Benutzerkonto aktivieren
        "displayName": user_data["displayname"],
        "mailNickname": user_data["mailnickname"],
        "userPrincipalName": user_data["userprincipalname"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True, # Passwortänderung beim ersten Login erzwingen
            "password": user_data["password"],
        },
        "jobTitle": user_data.get("jobtitle", ""),
        "businessPhones": user_data.get("phonenumber", []),
        "department": user_data.get("department", ""),
        "usageLocation": "CH"
    }

    try:
        response = requests.post(f"{GRAPH_API_URL}/users", headers=headers, json=body)
        if response.status_code == 201: # Erfolg: Benutzer erstellt
            user_id = response.json()["id"]
            print(f"Benutzer {user_data['displayname']} erfolgreich erstellt. ID: {user_id}")
            return user_id
        else:
            print(f"Fehler beim Erstellen des Benutzers: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")
        return None

# Funktion: Benutzer zu Gruppen hinzufügen
def assign_user_to_groups(token, user_id, group_ids):
    headers = {
        "Authorization": f"Bearer {token}", # Access Token für Authentifizierung
        "Content-Type": "application/json", # JSON-Daten senden
    }

    for group_id in group_ids:
        try:
            url = f"{GRAPH_API_URL}/groups/{group_id}/members/$ref" # URL zum Hinzufügen zu Gruppen
            body = {
                "@odata.id": f"{GRAPH_API_URL}/directoryObjects/{user_id}" # Referenz auf Benutzer-ID
            }
            response = requests.post(url, headers=headers, json=body)
            if response.status_code == 204: # Erfolg: Benutzer zur Gruppe hinzugefügt
                print(f"Benutzer erfolgreich der Gruppe {group_id} hinzugefügt.")
            else:
                print(f"Fehler beim Hinzufügen des Benutzers zu Gruppe {group_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Fehler bei der Gruppenanfrage: {e}")

# Funktion: Lizenz zuweisen
def assign_license_to_user(token, user_id, sku_id):
    headers = {
        "Authorization": f"Bearer {token}", # Access Token für Authentifizierung
        "Content-Type": "application/json", # JSON-Daten senden
    }
    url = f"{GRAPH_API_URL}/users/{user_id}/assignLicense" # URL zur Lizenzzuweisung
    body = {
        "addLicenses": [
            {
                "skuId": sku_id # Lizenz-ID
            }
        ],
        "removeLicenses": [] # Keine Lizenzen entfernen
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200: # Erfolg: Lizenz zugewiesen
            print(f"Lizenz erfolgreich dem Benutzer {user_id} zugewiesen.")
        else:
            print(f"Fehler beim Zuweisen der Lizenz: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Fehler bei der Lizenzanfrage: {e}")