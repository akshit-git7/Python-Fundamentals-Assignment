tasks=[]

def view_task():
    if not tasks:
        print("There are no tasks")
    else:
        print("_____To-Do List____")
        i=0
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' was added")

    
def del_task(i):
    view_task()
    try:
        task = tasks.pop(i - 1)
        print(f"Task '{task}' deleted")
    except IndexError:
        print("Invalid index")

