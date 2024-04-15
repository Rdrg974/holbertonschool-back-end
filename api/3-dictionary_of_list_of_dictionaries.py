#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
Records all tasks from all employees
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_data = {}
    for user in users:
        user_id = user.get("id")
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        response = requests.get(url)
        todos = response.json()
        all_data[user_id] = [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user.get("username")}
                             for task in todos]

    with open("todo_all_employees.json", "w") as json_file:
        json_file.write(json.dumps(all_data))
