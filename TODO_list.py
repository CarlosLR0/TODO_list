#TODO Application
#
#Main goals:
#-TUI, REPL.
#-Add, list tasks, able to delete completed task.
#-Persist across runs? stores previous data?
#-Every user gets their own list.
#-Editable storage format?
#-All tasks will be entered by the user.
#-User friendly, no memorization (no complicated commands to work with?).
#-Auto recall or prompt recall.
#-Report total # of tasks.
#Printing the list is default behaviour
# No more than 15 items in default printing
#save completed tasks
#show completed tasks
#Completed tasks @ the beginning of the list shall be deleted

from rich import print
from rich.console import Console
from rich.text import Text
import os
from os import system

print('Welcome to My TODO_list')
user = os.path.expanduser('~/TODO_list')

instructions = "\nOptions: \n1) Add new task. 2) Mark as completed. 3) Delete task. 4) Change page. 5) Quit. "
print(instructions)
todo_list = []

def open_list ():
    global todo_list
    try:
        with open(user + ".txt", mode='r') as f:
            b = f.readlines()
            todo_list = [x.replace('\n','') for x in b]
    except FileNotFoundError:
        open(user + ".txt", mode='w')

def clr_completed():
    for task in range(len(todo_list)):
        if todo_list[0].endswith('*') :
            del todo_list[0]
def page_num():
    while True:
        try:
            L = int(input("which page do you wanna see? "))
            L = L*15
            return L
        
        except ValueError:
            print ("Please enter a valid integer")
            continue
        else:
            break
def first15():
    open_list()
    clr_completed()
    L = 15
    print("\nList:")
    if (L - 14) <= len(todo_list):
        for j  in range(len(todo_list[L-15:L:])):
            print(j + (L-14),end =". ")
            print(todo_list[j + (L-15)])
first15()

def countTasks():
    open_list()
    print(f"\nThere are {len(todo_list)} tasks.")
countTasks()
    
def view_list():
    while True:
        open_list()
        clr_completed()
        L = page_num()
        print("\nList:")
        if (L - 14) <= len(todo_list):
            for j  in range(len(todo_list[L-15:L:])):
                print(j + (L-14),end =". ")
                print(todo_list[j + (L-15)])
            break
        elif (L - 15) > len(todo_list):
            print("Not available")
            
def list_mod ():
    with open(user + ".txt", newline='\n', mode='w') as f:
        f.write('\n'.join(str(e) for e in todo_list))
        f.close()

i = True   

while i:
    view_list()
    print(instructions)
    while True:
        try:
            user_in = int(input("\nEnter your option: "))
            if user_in == 1:
                try:
                    open_list()
                    task = input("Type the new task: ")
                    todo_list.append(task)
                    list_mod()
                    break
                except IndexError:
                    print("\nIndex is out of range") 
                except ValueError:
                    print("\nEnter an integer")

            elif user_in == 2:
                try: 
                    int_list_item = int(input("Which index do you want to mark as completed? "))
                    c = ("[italic green]*")
                    todo_list[int_list_item-1] = (c + todo_list[int_list_item - 1] + c)
                    list_mod()
                    break
                except IndexError:
                    print("\nIndex is out of range") 
                except ValueError:
                    print("\nEnter a task number")
            
            elif user_in == 3:
                try:
                    del_task_index = int(input("Which index do you want to delete? "))
                    todo_list.pop(del_task_index -1)
                    list_mod()
                    break
                except IndexError:
                    print("\nIndex is out of range")
                except ValueError:
                    print("\nEnter an integer")
            elif user_in == 4:
                break
            
            elif user_in == 5:
                exit_in = input("\nDo you want to exit? (y/n): ")
                if exit_in == 'y':
                    print("Good Bye")
                    quit()
        except IndexError:
            print("\nIndex is out of range")
            continue
        except ValueError:
            print("\nEnter an option")
            continue
