#!/usr/bin/python3
"""
requests TODO from jsonplaceholder and
creates a csv with the info
"""
import requests
import sys
import csv

if __name__ == "__main__":
    USER = sys.argv[1]
    USER_INFO = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            USER)).json()
    TODO = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER)).json()

    list_to_csv = []
    for values in TODO:
        new_list = [USER_INFO["id"], USER_INFO["username"],
                    values["completed"], values["title"]]
        list_to_csv.append(new_list)

    with open("{}.csv".format(USER), mode="w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerows(list_to_csv)
