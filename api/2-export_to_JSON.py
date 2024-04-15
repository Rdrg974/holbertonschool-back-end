#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    EMPLOYEE_NAME = user.get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    todos = response.json()

    tacks = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": EMPLOYEE_NAME
        }
        tacks.append(task)

    data = {user_id: tacks}

    with open("{}.json".format(user_id), "w") as json_file:
        json_file.write(json.dumps(data))
