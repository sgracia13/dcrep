group =[0, 1 , 2]
def user_menu():
    print("Press 1 to add task")
    print("Press 2 to view tasks")
    print("Press 3 to delete tasks")
    print("Press q to quit")

def add_task():
    task = input("Type in your task")
    priority = input ("Type in priority")
    toDoList = {"title": task, "level": priority}
    group.append = {toDoList}

def view_task():
    for things in group:
        print(things[0])

        1. sleep - high
def delete_task():
    print("Which task would you like to delete?")
    view_task()
    key = int(input("Enter task you want to delete. "))



user_input = ""

while user_input != "q":
    user_menu()
    user_input = input("Enter your choice:")

    if user_input == "1":
        add_task()
    elif user_input == "2":
        view_task()
    elif user_input == "3":
        delete_task()

    