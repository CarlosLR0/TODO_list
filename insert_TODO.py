# Ask user for their name
TODO_list = []
list_length = 100
for i in range(list_length):
	todo = input("Add to the list: ")
	TODO_list.append(todo)

# After done the asking, the program opens the file
# 'usernames.txt' in write mode, there are some more other
# modes, but in this example, I will only use the write mode with
with open("TODO_list.txt", "w") as fl:
    # Now, 'fl' is the reference of the command 'open("TODO_list.txt", "w")'
    # The file will write the username that it got
    # at the first part
	fl.write(TODO_list)

    
    # Now, the program done the adding, you should close them
	fl.close()

# That's it!
