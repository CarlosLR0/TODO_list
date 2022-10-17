# Ask user for their task to add
TODO_list = input("Add to the list: ")

# After done the asking, the program opens the file
# 'TODO_list.txt' in write mode
with open("TODO_list.txt", "a") as fl:
    # Now, 'fl' is the reference of the command 'open("TODO_list.txt", "w")'
    # The file will write the task that it got
    # at the first part
	fl.write('\n')
	fl.write(TODO_list)
    
    # Now, the programs done the adding, and should close them
	fl.close()

