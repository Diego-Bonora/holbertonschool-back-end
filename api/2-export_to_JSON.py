#!/usr/bin/python3
"""
requests TODO from jsonplaceholder and
creates a csv with the info
"""
import json
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

    list_to_json = []
    for values in TODO:
        new_list = {"task": "{}".format(str(values["title"])), "completed":
                    values["completed"], "username": "{}".format(str(USER_INFO["username"]))}
        list_to_json.append(new_list)
    dict_to_json = {"{}".format(str(USER_INFO["id"])): list_to_json}

    with open("{}.json".format(USER), mode="w", encoding="UTF8") as file:
        json.dump(dict_to_json, file)
