import csv
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
            user_id = response.json()["id"]
            print(f"Benutzer {user_data['displayName']} erfolgreich erstellt. ID: {user_id}")
            return user_id
        else:
            print(f"Fehler beim Erstellen des Benutzers: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Fehler bei der Anfrage: {e}")
        return None

def assign_user_to_groups(token, user_id, group_ids):
    """Weist einen Benutzer einer oder mehreren Gruppen zu."""
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

def load_users_from_csv(file_path):
    """Lädt die Benutzerinformationen aus einer CSV-Datei."""
    users = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                group_ids = row["groupIds"].split(";")  # Gruppenzuweisungen durch Semikolon getrennt
                users.append({
                    "displayName": row["displayName"],
                    "mailNickname": row["mailNickname"],
                    "userPrincipalName": row["userPrincipalName"],
                    "password": row["password"],
                    "groupIds": group_ids
                })
        return users
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        return []
    except KeyError as e:
        print(f"Fehlende Spalte in der CSV-Datei: {e}")
        return []

def main():
    # Pfad zur CSV-Datei
    csv_file_path = "users.csv"

    print("Lese Benutzerdaten aus CSV-Datei...")
    users = load_users_from_csv(csv_file_path)

    if not users:
        print("Keine Benutzerdaten gefunden. Prozess abgebrochen.")
        return

    print("Hole Access Token...")
    token = get_access_token()

    if not token:
        print("Token konnte nicht abgerufen werden. Prozess abgebrochen.")
        return

    for user in users:
        print(f"Erstelle Benutzer: {user['displayName']}...")
        user_id = create_user(token, user)

        if user_id:
            print(f"Weise Benutzer {user['displayName']} Gruppen zu...")
            assign_user_to_groups(token, user_id, user["groupIds"])

    print("Onboarding abgeschlossen.")

if __name__ == "__main__":
    main()
