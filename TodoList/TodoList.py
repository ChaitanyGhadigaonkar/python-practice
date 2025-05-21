# create a CLI based Todo List application
# all the todos will be updated in the todos.txt file

# user should able to perform CRUD todos tasks
# use text file to store, read, delete and update all the tasks
# use that text file as a database

import os
import uuid


def getUniqueId():
    return uuid.uuid4().int


scriptDir = os.path.dirname(__file__)
databaseFilePath = os.path.join(scriptDir, "todo.txt")


def getAllTodos():
    with open(databaseFilePath, "r") as readFile:
        todos = list()
        record = dict()

        for line in readFile:
            line = line.strip()
            if not line:
                if record:
                    todos.append(record.copy())
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value

        for todo in todos:
            print(todo)


def getTodoById():
    todoId = input("Enter Todo Id:\n")
    with open(databaseFilePath, "r") as readFile:
        todos = list()
        record = dict()

        for line in readFile:
            line = line.strip()
            if not line:
                if record:
                    todos.append(record.copy())
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value

        for todo in todos:
            if todo["id"] == todoId:
                print(todo)
                return
    print(f"no todo found for id : {todoId}")


def createTodo():
    title = input("Enter title \n")
    description = input("Enter description \n")
    status = input(
        "Enter current status of the task, in progress completed incomplete \n")

    statusList = list()
    statusList.append("completed")
    statusList.append("incomplete")
    statusList.append("in progress")

    if (status not in statusList):
        print("invalid status")
        return

    todoDictionary = dict()
    todoDictionary["id"] = getUniqueId()
    todoDictionary["title"] = title
    todoDictionary["description"] = description
    todoDictionary["status"] = status

    with open(databaseFilePath, "a+") as file:
        file.write("\n")

        for key in todoDictionary.keys():
            file.write(f"{key}: {todoDictionary[key]} \n")
        file.write("\n")
    print("Todo Added Successfully.")


def main():
    print("Welcome to cli based TODO list app", end="\n")

    print("THESE ARE ALL THE CHOICES YOU HAVE \n")

    print("1. Get all the TODOS \n")
    print("2. Get particular TODO using its ID \n")
    print("3. Add TODO \n")
    print("4. Update TODO using its ID \n")
    print("5. DELETE TODO using its ID \n")
    print("6. TO Exit code\n")
    while True:
        userInput = input("Enter Choice\n")
        match int(userInput):
            case 1:
                getAllTodos()
            case 2:
                getTodoById()
            case 3:
                createTodo()
            case 4:
                print("update particular todo")
            case 5:
                print("delete particular todo")
            case 6:
                break
            case _:
                print("invalid input\n")


main()
