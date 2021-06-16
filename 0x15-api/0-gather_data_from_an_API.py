#!/usr/bin/python3
""" API request """

import requests
import sys


def get_employee_tasks(employeeId):
    # Variables
    name = ''
    task_list = []
    completed_counter = 0

    # API GET requests
    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(employeeId))

    # Convert responses from JSON
    name = userRes.json().get('name')
    todosJson = todosRes.json()

    # Loop through tasks
    for task in todosJson:
        if task.get('completed') is True:
            completed_counter += 1
            # save task title to task_list
            task_list.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_counter, len(todosJson)))

    for title in task_list:
        print("\t{}".format(title))

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
