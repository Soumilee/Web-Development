from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    if name and description and due != None:
        task['name'] = name
        task['due'] = str_to_datetime(due)
        task['description'] = description
        task['lastActivity'] = datetime.now()
        tasks.append(task)
        print("The task was added ")
    else:
        print("The task could not be added as it did not match the format please provide name of task description and due date in mentioned format")
    #sg342 implemented date 8th feb 2023 used append to add the new tasks at the end of the list
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """    
    if index>len(tasks):
        print("index cannot be greater than no. of items")
    if index<0:
        print("please enter index no. starting from 1")
    else:
        task_to_update = tasks[index]
        print("The task is",task_to_update["name"])
        print("Description: ",task_to_update["description"])
        print("Due date : ",task_to_update["due"])
        name = input(f"What's the name of this task? \n").strip()
        desc = input(f"What's a brief descriptions of this task? \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) \n").strip()
        update_task(index, name=name, description=desc, due=due)
    #sg342 8th feb 2023

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    if index>len(tasks):
        print("The index cannot be greater than the no. of items in list")
    elif index<0:
        print("Please enter index no. starting from 1")
    else:
        task_to_change = tasks[index]
        if task_to_change["name"] != name:
            task_to_change["name"] = name
            print("name of task was updated !!")
        if task_to_change["description"] != description:
            task_to_change["description"] = description
            print("the description of task was updated !!")
        if task_to_change["due"] != due:
            task_to_change["due"] = due
            print("the due date was updated..")
        else:
            print("Nothing was updated...")
        task_to_change["lastActivity"] = datetime.now() 
    tasks[index] = task_to_change 
    #sg342 8th feb 2023
    
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    if index>=len(tasks):
        print("The index cannot be greater than the no of items in list")
    elif index<0:
        print("Please give index no. starting from 1")
    else:
        finished_task = tasks[index]
        if finished_task["done"]:
            print("This task is already completed !!! ")
        else:
            finished_task["done"] = datetime.now()
            finished_task["lastActivity"] = datetime.now()
            print("Task marked done !!")
    tasks[index]=finished_task
    #sg342 8th feb 2023
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    if index>len(tasks):
        print("The index cannot be greater than the no of items in list")
    elif index<0:
        print("Please give index no. starting from 1")
    else:
        task = tasks[index]
        print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    #sg342 8th feb 2023


def delete_task(index):
    """ deletes a task from the tasks list by index """
    if index>len(tasks):
        print("The index cannot be greater than the no of items in list")
    elif index<0:
        print("Please give index no. starting from 1")
    else:
        tasks.pop(index)
        print("the task is successfully deleted from the tracker")
    #sg342 8th feb 2023 using pop(index) function to delete the task
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    _tasks = []
    for i in tasks:
        if i["done"] == False:
            _tasks.append(i)    
    list_tasks(_tasks)
    #sg342 8th feb 2023 

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    for i in tasks:
        if ("due">datetime.now()) and ("done"==False):
            _tasks = tasks[i]
    _tasks = []
    list_tasks(_tasks)
    #sg342 8th feb 2023

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    if index>len(tasks):
        print("The index cannot be greater than the no of items in list")
    elif index<0:
        print("Please give index no. starting from 1")
    else:
        task_left = tasks[index]
        due_time = str_to_datetime(task_left["due"])
        time_now = datetime.now()
        if due_time>time_now:
            time_diff = due_time-time_now
            print("time remaining to finish the task is %d/%m/%Y %H:%M:%S  ",time_diff)
        else:
            time_diff = time_now - due_time
            print("the task is over due by %d/%m/%Y %H:%M:%S ",time_diff)
    task = {}
    #sg342 8th feb 2023

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()