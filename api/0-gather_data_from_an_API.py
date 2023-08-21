#!/usr/bin/python3
""" 
requests TODO from jsonplaceholder and 
prints the employee with all the tasks done
"""
import requests
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    USER_INFO = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            USER)).json()
    TODO = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER)).json()
    EMPLOYEE_NAME = USER_INFO["name"]
    TOTAL_NUMBER_OF_TASKS = len(TODO)
    tasks_done = []
    for tasks in TODO:
        if tasks["completed"] == True:
            tasks_done.append(tasks)
    NUMBER_OF_DONE_TASKS = len(tasks_done)

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for tasks in tasks_done:
        print("\t {}".format(tasks["title"]))
