tasks = []

def add(task):
    tasks.append(task)

def list_tasks():
    return tasks


def delete_task(index):
    del tasks[index]


def exit():
    quit()
