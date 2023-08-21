#!/usr/bin/python3
"""
requests TODO from jsonplaceholder and
prints the employee with all the tasks done
"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    user_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user}')
    user_info_json = user_info.json()
    todo = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user}')
    todo_json = todo.json()
    total_tasks = 0
    total_tasks_done = 0
    tasks_done = []
    for tasks in todo_json:
        if tasks["completed"]:
            tasks_done.append(tasks["title"])
            total_tasks_done += 1
            total_tasks += 1
        else:
            total_tasks += 1

    print(
        f"Employee {user_info_json['name']} is done with\
tasks({total_tasks_done}/{total_tasks}):")
    for tasks in tasks_done:
        print(f"\t {tasks}")
