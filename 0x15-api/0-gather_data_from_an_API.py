#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    resp = req.get(url).json()
    EMPLOYEE_NAME = resp.get("name")
    NUMBER_OF_DONE_TASKS = 0
    user_todos = req.get(user_todo_url).json()
    TOTAL_NUMBER_OF_TASKS = len(user_todos)
    for todo in user_todos:
        if todo.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")
    [print(
        f"\t {todos.get('title')}"
        ) for todos in user_todos if todos.get("completed")]
