#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
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
    with open("{}.json".format(user_id), "w") as json_file:
        json_file.write(" {")
        json_file.write("\"{}\": [".format(user_id))
        for task in todos:
            json_file.write("{")
            json_file.write("\"task\": \"{}\", ".format(task.get("title")))
            json_file.write("\"completed\": \"{}\", ".format(
                task.get("completed")))
            json_file.write("\"username\": \"{}\"".format(EMPLOYEE_NAME))
            json_file.write("}")
            if task != todos[-1]:
                json_file.write(", ")
        json_file.write("]}")
