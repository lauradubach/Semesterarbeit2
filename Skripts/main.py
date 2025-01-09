import user  # Das Skript mit den Azure-Funktionen
import app_camunda  # Das Skript mit der Camunda-Integration
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker

# Standardwerte für Gruppen-IDs und Lizenz-ID
DEFAULT_GROUP_IDS = ["3a562661-05d1-4486-873c-370b37fe4cbe"]
DEFAULT_SKU_ID = "f30db892-07e9-47e9-837c-80727f46fd3d"

def main():
    # Schritt 1: Token abrufen
    print("Token wird abgerufen...")
    token = user.get_access_token()
    if not token:
        print("Konnte kein Token abrufen. Beende das Skript.")
        return

    # Schritt 2: Camunda-Task abholen und verarbeiten
    def handle_task(task: ExternalTask) -> TaskResult:
        try:
            # Variablen aus dem Camunda-Task lesen
            user_data = {
                "displayname": task.get_variable("displayname"),
                "mailnickname": task.get_variable("mailnickname"),
                "userprincipalname": task.get_variable("userprincipalname"),
                "password": task.get_variable("password"),
                "jobtitle": task.get_variable("jobtitel"),
                "phonenumber": task.get_variable("phonenumber"),
                "department": task.get_variable("department"),
            }

            # Verwende Standardwerte für Gruppen-IDs und SKU-ID
            group_ids = task.get_variable("groupids") or DEFAULT_GROUP_IDS
            group_ids_list = group_ids.split(",")
            sku_id = task.get_variable("skuid") or DEFAULT_SKU_ID

            # Debbuging
            print (group_ids_list)
            print(f"Übergebene Gruppen-IDs: {group_ids}")
            print(f"Übergebene SKU-ID: {sku_id}")

            # Schritt 3: Benutzer erstellen
            print(f"Erstelle Benutzer: {user_data['displayname']}...")
            user_id = user.create_user(token, user_data)
            if not user_id:
                print("Fehler beim Erstellen des Benutzers.")
                return task.failure(
                    error_message="User creation failed",
                    error_details="Der Benutzer konnte nicht erstellt werden.",
                    max_retries=0,
                    retry_timeout=0,
                )

            # Schritt 4: Benutzer zu Gruppen hinzufügen
            if group_ids_list:
                print(f"Benutzer {user_data['displayname']} wird zu Gruppen hinzugefügt...")
                user.assign_user_to_groups(token, user_id, group_ids_list)

            # Schritt 5: Lizenz zuweisen
            if sku_id:
                print(f"Lizenz wird Benutzer {user_data['displayname']} zugewiesen...")
                user.assign_license_to_user(token, user_id, sku_id)

            print(f"Benutzer {user_data['displayname']} erfolgreich verarbeitet.")
            return task.complete({"success": True, "ResultText": "Benutzer erstellt und konfiguriert."})

        except Exception as e:
            print(f"Fehler bei der Bearbeitung des Tasks: {e}")
            # Fehler an Camunda zurückmelden
            return task.failure(
                error_message="Task processing failed",
                error_details=str(e),
                max_retries=1,  # Ein Wiederholungsversuch
                retry_timeout=5000,  # Wartezeit von 5 Sekunden vor Wiederholung
            )

    # Camunda-Task-Worker starten
    print("Starte Camunda-Task-Worker...")
    ExternalTaskWorker(worker_id="azure_worker", config=app_camunda.default_config).subscribe("usergenerate", handle_task)

if __name__ == '__main__':
    main()
