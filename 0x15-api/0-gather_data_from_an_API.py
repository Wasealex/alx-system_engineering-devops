#!/usr/bin/python3
"""script that, use employee ID as an arg and
returns information about his/her TODO list progress. in the following output
First line: Employee EMPLOYEE_NAME is done with tasks
            (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
Second and N next lines display the title of completed tasks:
            TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
from sys import argv, exit
import requests
if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        exit(1)

    url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])

    employee_url = f"{url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    todos_url = f"{url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")
