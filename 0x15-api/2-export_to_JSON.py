#!/usr/bin/python3
""" Convert API requested info JSON export """

import json
import requests
import sys


def save_tasks_to_json(employeeId):
    """ By eId, export completed value of each task """

    name = ''
    userDict = {}

    userRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(employeeId))

    name = userRes.json().get('username')
    todosJson = todosRes.json()

    userDict[employeeId] = []
    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = name
        taskDict['completed'] = task.get('completed')
        
        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

    return 0

if __name__ == "__main__":
    save_tasks_to_json(sys.argv[1])
