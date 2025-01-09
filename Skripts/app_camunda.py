from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker


# configuration for the Client
default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

def handle_task(task: ExternalTask) -> TaskResult:

    displayname = task.get_variable("displayname")
    mailnickname = task.get_variable("mailnickname")
    userprincipalname = task.get_variable("userprincipalname")
    password = task.get_variable("password")
    groupids = task.get_variable("groupids")
    jobtitel = task.get_variable("jobtitel")
    phonenumber = task.get_variable("phonenumber")
    department = task.get_variable("department")
    skuid = task.get_variable("skuid")

    print(displayname, mailnickname, userprincipalname, password, groupids, jobtitel, phonenumber, department, skuid)

    return task.complete({"success": True, "ResultText": ""})

if __name__ == '__main__':
    ExternalTaskWorker(worker_id="2", config=default_config).subscribe("usergenerate", handle_task)