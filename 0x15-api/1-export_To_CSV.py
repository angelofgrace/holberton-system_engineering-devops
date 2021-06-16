#!/usr/bin/python3
""" Convert API requested info to CSV file export """

import csv
import requests
import sys

# File -> CSV
# Open /create/ specific file (ID.csv) and write
# all tasks for users ->


def save_tasks_to_csv(employeeId):
    """ By eId, export completed value of each task """

    name = ''
    allTasks = []

    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(employeeId))

    name = userRes.json().get('username')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(name)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))

        allTasks.append(taskRow)

    with open("{}.csv".format(employeeId), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(allTasks)

if __name__ == "__main__":
    save_tasks_to_csv(sys.argv[1])
