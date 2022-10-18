print("\nMy TODO_list")
instructions = "\nOptions: \n-Enter a to add new task. \n-Enter c to mark item as completed. \n-Enter d to delete items. \n-Enter v to view list. \n-Enter e to exit "
print(instructions)

todo_list = []

i = True

while i:
    user_in = input("Enter your option: ").lower()

    if user_in == 'a':
        task = input("Type the new task: ").lower()
        todo_list.append([task])
        print("Added new task: ", task)

    elif user_in == 'c':
        #for idx, task in enumerate(todo_list)
        int_list_item = int(input("Which index do you want to mark as completed? "))
        #modify
        c = ("completed")
        todo_list[int_list_item] = todo_list[int_list_item], c
        print(todo_list[int_list_item])

    elif user_in == 'd':
        print("Current list")
        for task in range(len(todo_list)):
            print(task,end = ". ")
            print(todo_list[task])
        del_task_index = int(input("Which index do you want to delete? "))
        print("You have deleted",todo_list.pop(del_task_index))
        
    elif user_in == 'v':
        print("Current list")
        for task in range(len(todo_list)):
           print(task,end =". ")
           print(todo_list[task])
            
    elif user_in == 'e':
        exit_in = input("\nDo you want to exit? (Y/N): ").lower()
        if exit_in == 'y':
            print("Good Bye")
            i = False

    elif user_in == 's':
        save_in = input("Are you sure you want to save? (Y/N: ")
        if save_in == 'y':
            with open("TODO_list.txt", newline='\n', mode='w') as fl:
                fl.write('\n'.join(str(e) for e in todo_list))
                fl.close()
                print("Current list has been saved")
