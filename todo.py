tasks = ["1"]

def add(task):
    tasks.append(task)

def list_tasks():
    print(tasks)


def delete_task(index):
    del tasks[index]


def exit():
    quit()
