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
    NUMBER_OF_DONE_TASKS = 0
    tasks_done = ""
    for tasks in TODO:
        if tasks["completed"]:
            task = tasks["title"]
            tasks_done += f"\t {task}\n"
            NUMBER_OF_DONE_TASKS += 1

    info = f"Employee {EMPLOYEE_NAME} is done with tasks(\
{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):\n" + \
        tasks_done[:-1]
    print(info)
