print("Welcome\nPLease enter your name:")
name = input()


print("\nMy TODO_list")
instructions = "\nOptions: \n-Enter a to add new task. \n-Enter c to mark item as completed. \n-Enter d to delete items. \n-Enter e to exit. \n-Enter l to load saved list. \n-Enter s to save current list. \n-Enter v to view list. "
print(instructions)

todo_list = []

i = True

while i:
    user_in = input("\nEnter your option: ").lower()

    if user_in == 'a':
        task = input("\nType the new task: ")
        todo_list.append(task)
        print("\nAdded new task: ", task)

    elif user_in == 'c':
       try:
           int_list_item = int(input("\nWhich index do you want to mark as completed? "))
           c = (" completed")
           todo_list[int_list_item] = todo_list[int_list_item] + c
           print(todo_list[int_list_item])

       except IndexError:
            print("\nIndex is out of range") 
       except ValueError:
           print("\nEnter an integer")
            
    elif user_in == 'd':
        print("\nCurrent list")
        try:
            for task in range(len(todo_list)):
                print(task,end = ". ")
                print(todo_list[task])
            del_task_index = int(input("Which index do you want to delete? "))
            print("\nYou have deleted",todo_list.pop(del_task_index))

        except IndexError:
            print("\nIndex is out of range")
        except ValueError:
            print("\nEnter an integer")
            
    elif user_in == 'v':
        print("\nCurrent list")
        for task in range(len(todo_list)):
           print(task,end =". ")
           print(todo_list[task])
            
    elif user_in == 'e':
        exit_in = input("\nUnsaved tasks will not be recoverable\nDo you want to exit? (y/n): ")
        if exit_in == 'y':
            print("Good Bye")
            quit()

    elif user_in == 's':
        save_in = input("\nAre you sure you want to save? (y/n): ")
        if save_in == 'y':
            with open(name + ".txt", newline='\n', mode='w') as fl:
                fl.write('\n'.join(str(e) for e in todo_list))
                fl.close()
                print("Current list has been saved")

    elif user_in == 'l':
        read = input("\n\nWARNING\nLoading a saved list will overwrite your current list\nPress enter after reading the warning")
        load_in = input('Do you want to load your saved list? (y/n): ')
        if load_in == 'y':
            
            a = open(name + ".txt", mode='r')
            b = a.readlines()
            todo_list = [x.replace('\n','') for x in b]
            print("Loaded saved list:")
            for task in range(len(todo_list)):
                print(task, end =". ")
                print(todo_list[task])
            

