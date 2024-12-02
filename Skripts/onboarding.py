import json
import requests
from msal import ConfidentialClientApplication

# Azure Konfiguration
CLIENT_ID = "deine-client-id"
CLIENT_SECRET = "dein-client-secret"
TENANT_ID = "deine-tenant-id"

GRAPH_API_URL = "https://graph.microsoft.com/v1.0"

def get_access_token():
    """Holt ein Access Token von Azure AD."""
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
    """Erstellt einen neuen Benutzer in Azure AD."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = {
        "accountEnabled": True,
        "displayName": user_data["displayName"],
        "mailNickname": user_data["mailNickname"],
        "userPrincipalName": user_data["userPrincipalName"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": user_data["password"],
        },
    }

    try:
        response = requests.post(f"{GRAPH_API_URL}/users", headers=headers, json=body)
        if response.status_code == 201:
            print(f"Benutzer {user_data['displayName']} erfolgreich erstellt.")
        else:
            print(f"Fehler beim Erstellen des Benutzers: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")

def main():
    # Beispiel-Mitarbeiterdaten
    users = [
        {
            "displayName": "Joya Dubach",
            "mailNickname": "joya.dubach",
            "userPrincipalName": "joya.dubach@itnetx",
            "password": "7qbSqVs2tCkk",
        },
        {
            "displayName": "Anna Schmidt",
            "mailNickname": "anna.schmidt",
            "userPrincipalName": "anna.schmidt@itnetx",
            "password": "UW6udkBycJed",
        },
    ]

    print("Hole Access Token...")
    token = get_access_token()

    if not token:
        print("Token konnte nicht abgerufen werden. Prozess abgebrochen.")
        return

    for user in users:
        print(f"Erstelle Benutzer: {user['displayName']}...")
        create_user(token, user)

    print("Onboarding abgeschlossen.")

if __name__ == "__main__":
    main()
