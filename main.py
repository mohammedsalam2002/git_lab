from todo import add , list_tasks , delete_task ,exit

status = True
while status :
    print('welcom to the program')
    
    print("1--> add task")
    print("2--> list task")
    print("3--> delete task")
    print("4--> exit")
    x = input("selected the op: ")
    if x == '1':
        task = input("Enter your task here")
        add(task)
    if  x =='2':
        list_tasks()
    elif x=='3':
        id = int(input("enter the id of the task you want to remove"))
        delete_task(id)
    elif x=='4':
        print("thank you for using our service")
        exit()

