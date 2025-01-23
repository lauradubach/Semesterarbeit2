# Module Importieren
from camunda.external_task.external_task import ExternalTask, TaskResult # Klassen für die Arbeit mit Camunda-Tasks
from camunda.external_task.external_task_worker import ExternalTaskWorker #  Klasse, um Worker für Camunda zu starten


# Konfiguration für den Camunda-Client
default_config = {
    "maxTasks": 1, # Maximale Anzahl an gleichzeitig verarbeiteten Aufgaben
    "lockDuration": 10000, # Zeit (in ms), während eine Aufgabe gesperrt ist
    "asyncResponseTimeout": 5000, # Timeout für asynchrone Antworten (in ms)
    "retries": 3, # Anzahl der Wiederholungsversuche bei Fehlern
    "retryTimeout": 5000, # Zeit (in ms) zwischen Wiederholungsversuchen
    "sleepSeconds": 30 # Wartezeit (in Sekunden), wenn keine Aufgaben verfügbar sind
}

# Funktion zur Verarbeitung einer Aufgabe aus Camunda
def handle_task(task: ExternalTask) -> TaskResult:
    # Auslesen von Variablen aus der Camunda-Aufgabe
    displayname = task.get_variable("displayname")
    mailnickname = task.get_variable("mailnickname")
    userprincipalname = task.get_variable("userprincipalname")
    password = task.get_variable("password")
    groupids = task.get_variable("groupids")
    jobtitel = task.get_variable("jobtitel")
    phonenumber = task.get_variable("phonenumber")
    department = task.get_variable("department")
    skuid = task.get_variable("skuid")

    # Debug-Ausgabe aller Variablen
    print(displayname, mailnickname, userprincipalname, password, groupids, jobtitel, phonenumber, department, skuid)

    # Aufgabe als erfolgreich abgeschlossen markieren
    return task.complete({"success": True, "ResultText": ""})

# Hauptteil: Startet den Worker, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    # Startet den Camunda-Task-Worker mit der Konfiguration und der "usergenerate"-Subscription
    ExternalTaskWorker(worker_id="2", config=default_config).subscribe("usergenerate", handle_task)