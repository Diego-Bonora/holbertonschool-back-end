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
            USER))
    USER_INFO_json = USER_INFO.json()
    TODO = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER))
    TODO_json = TODO.json()
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    tasks_done = []
    for tasks in TODO_json:
        if tasks["completed"]:
            tasks_done.append(tasks["title"])
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
        else:
            TOTAL_NUMBER_OF_TASKS += 1

    print(
        f"Employee {USER_INFO_json['name']} is done with\
tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for tasks in tasks_done:
        print(f"\t {tasks}")
