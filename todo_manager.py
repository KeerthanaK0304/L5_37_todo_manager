
import json
from datetime import datetime

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def addTask(title, priority="medium", labels=[]):
    taskId = len(tasks) + 1
    labels.append(priority)
    tasks[taskId] = {
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat()
    }
    return taskId


def completeTask(taskId):
    if taskId in tasks:
        tasks[taskId]["done"] = True
        return True
    print("No task with id", taskId)
    return False


def pendingTasks():
    pending = [
        task for task in tasks.values() if not task["done"]
    ]
    pending.sort(
        key=lambda task: PRIORITY_ORDER[task["priority"]]
    )
    return [task["title"] for task in pending]


def findTask(keyword):
    for taskId, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return taskId


def saveTasks(fileName="tasks.json"):
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def loadTasks(fileName="tasks.json"):
    with open(fileName, "r", encoding="utf-8") as file:
        loaded_tasks = json.load(file)

    return {
        int(task_id): task
        for task_id, task in loaded_tasks.items()
    }


def exportJson(fileName="tasks.json"):
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def main():
    addTask("Submit lab report", "high")
    addTask("Buy groceries")
    addTask("Call plumber", "low")
    addTask("Book train tickets", "high")

    completeTask(2)
    completeTask(99)

    print("Pending tasks:", pendingTasks())
    print("Task id for 'plumber':", findTask("plumber"))
    print("Task id for 'gym':", findTask("gym"))

    pending = pendingTasks()
    suggestion = pending[0] if pending else "No pending tasks"
    print("Try this next:", suggestion)

    saveTasks()
    restored = loadTasks()
    print("Tasks restored from file:", len(restored))
    exportJson()
    print("Exported tasks to tasks.json")


main()
