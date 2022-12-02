#!/usr/bin/python3
"""
  Request from API;
  Return TODO list progress given employee ID
  and Export this data in the JSON format.
"""
import csv
import json
import requests
from sys import argv


def all_tasks_to_json():
    """
      This return API data
    """
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """
      This export to json
    """
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_tasks_to_json()
