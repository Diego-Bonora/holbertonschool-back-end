#!/usr/bin/python3
"""
requests TODO from jsonplaceholder and
creates a csv with the info
"""
import json
import requests

if __name__ == "__main__":
    USER_INFO = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    TODO = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    dict_to_json = {}
    for USERS in USER_INFO:
        list_to_json = []
        for values in TODO:
            if str(USERS["id"]) == str(values["userId"]):
                new_dict = {"username": "{}".format(str(USERS["username"])),
                            "task": "{}".format(str(values["title"])),
                            "completed": values["completed"]}
                list_to_json.append(new_dict)
        dict_to_json["{}".format(str(USERS["id"]))] = list_to_json

    with open("todo_all_employees.json", mode="w", encoding="UTF8") as file:
        json.dump(dict_to_json, file)
