import requests
from msal import ConfidentialClientApplication

# Azure Konfiguration
CLIENT_ID = "xxxx"
CLIENT_SECRET = "xxxx"
TENANT_ID = "xxxx"

GRAPH_API_URL = "https://graph.microsoft.com/v1.0"
scopes = ["https://graph.microsoft.com/.default"]

def get_access_token():
    try:
        app = ConfidentialClientApplication(
            CLIENT_ID,
            authority=f"https://login.microsoftonline.com/{TENANT_ID}",
            client_credential=CLIENT_SECRET,
        )
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        if "access_token" in result:
            return result["access_token"]
        else:
            raise Exception("Konnte kein Access Token abrufen.")
    except Exception as e:
        print(f"Fehler beim Abrufen des Access Tokens: {e}")
        return None

def create_user(token, user_data):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = {
        "accountEnabled": True,
        "displayName": user_data["displayname"],
        "mailNickname": user_data["mailnickname"],
        "userPrincipalName": user_data["userprincipalname"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": user_data["password"],
        },
        "jobTitle": user_data.get("jobtitle", ""),
        "businessPhones": user_data.get("phonenumber", []),
        "department": user_data.get("department", ""),
        "usageLocation": "CH"
    }

    try:
        response = requests.post(f"{GRAPH_API_URL}/users", headers=headers, json=body)
        if response.status_code == 201:
            user_id = response.json()["id"]
            print(f"Benutzer {user_data['displayname']} erfolgreich erstellt. ID: {user_id}")
            return user_id
        else:
            print(f"Fehler beim Erstellen des Benutzers: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")
        return None

def assign_user_to_groups(token, user_id, group_ids):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    for group_id in group_ids:
        try:
            url = f"{GRAPH_API_URL}/groups/{group_id}/members/$ref"
            body = {
                "@odata.id": f"{GRAPH_API_URL}/directoryObjects/{user_id}"
            }
            response = requests.post(url, headers=headers, json=body)
            if response.status_code == 204:
                print(f"Benutzer erfolgreich der Gruppe {group_id} hinzugefügt.")
            else:
                print(f"Fehler beim Hinzufügen des Benutzers zu Gruppe {group_id}: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Fehler bei der Gruppenanfrage: {e}")

def assign_license_to_user(token, user_id, sku_id):
    """Weist einem Benutzer eine Lizenz zu."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    url = f"{GRAPH_API_URL}/users/{user_id}/assignLicense"
    body = {
        "addLicenses": [
            {
                "skuId": sku_id
            }
        ],
        "removeLicenses": []
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            print(f"Lizenz erfolgreich dem Benutzer {user_id} zugewiesen.")
        else:
            print(f"Fehler beim Zuweisen der Lizenz: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Fehler bei der Lizenzanfrage: {e}")