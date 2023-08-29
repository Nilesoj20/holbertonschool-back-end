#!/usr/bin/python3
"""returns information about his/her TODO list progress"""

import requests
from requests import get
from sys import argv

if __name__ == '__main__':
    source = 'https://jsonplaceholder.typicode.com'
    todoall = source + "/user/{}/todos".format(argv[1])
    names = source + "/users/{}".format(argv[1])
    todores = get(todoall).json()
    nameres = get(names).json()

    todonum = len(todores)
    todocomp = len([todo for todo in todores
                    if todo.get("completed")])
    name = nameres.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todocomp, todonum))
    for todo in todores:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
