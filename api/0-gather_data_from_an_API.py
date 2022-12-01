#!/usr/bin/python3
"""
  Script that, using this REST API, for a given employee ID,
  returns information about his/her TODO list progress.
"""

import requests
from sys import argv


def counter(completed=None):
    """
      Just to count completed task
    """

    count = 0
    for any in todo:
        if any.get('completed') is True:
            count += 1
    return count


if __name__ == "__main__":

    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users'.format,
                        params=payload).json()

    payload2 = {'userId': argv[1]}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos'.format,
                        params=payload2).json()

    print('Employee {} is done with tasks({}/{}):'.format(
     user[0].get('name'),
     counter(todo),
     len(todo)))

    for any in todo:
        if any.get('completed') is True:
            print("\t {}".format(any.get('title')))
