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


def expor_to_json():
    """
      return API data
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """
      This export to json
    """
    t = []
    for task in TASK_STATUS_TITLE:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    expor_to_json()
