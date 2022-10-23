import os
from os import system

print("\nWelcome to My TODO_list")
user = os.path.expanduser('~/TODO_list')

instructions = "\nOptions: \n-Enter a to add new task. \n-Enter c to mark item as completed. \n-Enter d to delete items. \n-Enter q to quit. "
todo_list = []

def open_list ():
    global todo_list
    try:
        with open(user + ".txt", mode='r') as f:
            b = f.readlines()
            todo_list = [x.replace('\n','') for x in b]
    except FileNotFoundError:
        open(user + ".txt", mode='w')

def view_list():
    open_list()
    for task in range(len(todo_list)):
        print("\nList:")
        print(task +1,end =". ")
        print(todo_list[task])

def list_mod ():
    with open(user + ".txt", newline='\n', mode='w') as f:
        f.write('\n'.join(str(e) for e in todo_list))
        f.close()

i = True   

while i:
    print(instructions)
    view_list()
    user_in = input("\nEnter your option: ").lower()

    if user_in == 'a':
        open_list()
        task = input("Type the new task: ")
        todo_list.append(task)
        list_mod()

    elif user_in == 'c':
       try: 
        int_list_item = int(input("Which index do you want to mark as completed? "))
        c = (" completed")
        todo_list[int_list_item-1] = todo_list[int_list_item-1] + c
        list_mod()
       except IndexError:
            print("\nIndex is out of range") 
       except ValueError:
           print("\nEnter an integer")
            
    elif user_in == 'd':
        try:
            del_task_index = int(input("Which index do you want to delete? "))
            todo_list.pop(del_task_index -1)
            list_mod()
        except IndexError:
            print("\nIndex is out of range")
        except ValueError:
            print("\nEnter an integer")
            
    elif user_in == 'q':
        exit_in = input("\nDo you want to exit? (y/n): ")
        if exit_in == 'y':
            print("Good Bye")
            quit()