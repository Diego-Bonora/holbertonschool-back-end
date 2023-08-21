#!/usr/bin/python3
"""
requests TODO from jsonplaceholder and
creates a csv with the info
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

    with open("{}.csv".format(USER), mode="w", encoding="UTF8") as file:
        for values in TODO:
            file.write(f"{USER_INFO['id']}, {USER_INFO['username']},\
{values['completed']}, {values['title']}\n")
