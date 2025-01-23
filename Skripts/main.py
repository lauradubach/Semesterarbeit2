import user  # Import Skript mit Azure-Funktionen
import app_camunda  # Import Skript mit Camunda-Integration und Worker-Konfiguration
# Module Importieren
from camunda.external_task.external_task import ExternalTask, TaskResult # Klassen für Camunda-Tasks
from camunda.external_task.external_task_worker import ExternalTaskWorker # Klasse zum Starten eines Task-Workers

# Standardwerte für Gruppen-IDs und Lizenz-ID
DEFAULT_GROUP_IDS = ["3a562661-05d1-4486-873c-370b37fe4cbe"]
DEFAULT_SKU_ID = "f30db892-07e9-47e9-837c-80727f46fd3d"

# Hauptfunktion des Skripts
def main():
    # Abrufen eines Access Tokens
    print("Token wird abgerufen...")
    token = user.get_access_token() # Holt ein Access Token über die Funktion in "user.py"
    if not token:
        print("Konnte kein Token abrufen. Beende das Skript.")
        return

    # Funktion zur Verarbeitung eines Camunda-Tasks definieren
    def handle_task(task: ExternalTask) -> TaskResult:
        try:
            # Variablen aus der Aufgabe auslesen
            user_data = {
                "displayname": task.get_variable("displayname"),
                "mailnickname": task.get_variable("mailnickname"),
                "userprincipalname": task.get_variable("userprincipalname"),
                "password": task.get_variable("password"),
                "jobtitle": task.get_variable("jobtitel"),
                "phonenumber": task.get_variable("phonenumber").split(","),
                "department": task.get_variable("department"),
            }

            # Verwende Standardwerte für Gruppen-IDs und SKU-ID
            group_ids = task.get_variable("groupids") or DEFAULT_GROUP_IDS
            group_ids_list = group_ids.split(",")
            sku_id = task.get_variable("skuid") or DEFAULT_SKU_ID

            # Benutzer erstellen
            print(f"Erstelle Benutzer: {user_data['displayname']}...")
            user_id = user.create_user(token, user_data) # Benutzer mit Azure-API erstellen
            if not user_id:
                print("Fehler beim Erstellen des Benutzers.")
                return task.failure(
                    error_message="User konnte nicht erstellt werden",
                    error_details="Der Benutzer konnte nicht erstellt werden.",
                    max_retries=0,
                    retry_timeout=0,
                )

            # Benutzer zu Gruppen hinzufügen
            if group_ids_list:
                print(f"Benutzer {user_data['displayname']} wird zu Gruppen hinzugefügt...")
                user.assign_user_to_groups(token, user_id, group_ids_list)

            # Lizenz zuweisen
            if sku_id:
                print(f"Lizenz wird Benutzer {user_data['displayname']} zugewiesen...")
                user.assign_license_to_user(token, user_id, sku_id)

            # Erfolgsmeldung
            print(f"Benutzer {user_data['displayname']} erfolgreich verarbeitet.")
            return task.complete({"success": True, "ResultText": "Benutzer erstellt und konfiguriert."})

        except Exception as e:
            # Fehlerbehandlung: Fehler an Camunda melden
            print(f"Fehler bei der Bearbeitung des Tasks: {e}")
            return task.failure(
                error_message="Task Prozess fehlgeschlagen",
                error_details=str(e),
                max_retries=1,  # Ein Wiederholungsversuch
                retry_timeout=5000,  # Wartezeit von 5 Sekunden vor Wiederholung
            )

    # Camunda-Task-Worker starten
    print("Starte Camunda-Task-Worker...")
    ExternalTaskWorker(worker_id="azure_worker", config=app_camunda.default_config).subscribe("usergenerate", handle_task)

# Skript ausführen, wenn es direkt gestartet wird
if __name__ == '__main__':
    main()
