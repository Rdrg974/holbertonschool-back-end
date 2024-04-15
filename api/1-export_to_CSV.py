#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""
import csv
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

    with open("{}.csv".format(user_id), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, EMPLOYEE_NAME,
                             task.get("completed"), task.get("title")])
