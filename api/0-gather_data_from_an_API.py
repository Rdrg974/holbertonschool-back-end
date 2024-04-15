#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    EMPLOYEE_NAME = user.get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    todos = response.json()

    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = [task for task
                            in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), TOTAL_NUMBER_OF_TASKS))
    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task.get("title")))
