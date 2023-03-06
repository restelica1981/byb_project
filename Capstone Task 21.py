import datetime as date
import os
#====================Define Functions=======================#

def generate_report():

    current_date = date.datetime.today()
    total_task = 0
    uncompleted_task = 0
    completed_task = 0
    overdue_task = 0
    user_task = 0
    user_overdue_and_uncompleted = 0
    user_completed = 0
    user_uncompleted_task = 0
    input_file = open("tasks.txt", "r")
    for line in input_file:
        parts = line.strip().split(";")
        total_task += 1
        # reading text file and counting total taks
        if "No" in parts[-1]:
            uncompleted_task += 1
        elif "Yes" in parts[-1]:
            completed_task += 1
        elif str(current_date.strftime("%Y %m %d")) in parts[5]:
            overdue_task += 1
        # checking based on each line for completed tasks , uncompleted tasks and overdue tasks
        with open("task_overview.txt", "w") as out_file:
            print(f"There are a total of {total_task} tasks.", file=out_file)
            print(f"There are a total of {uncompleted_task} uncompleted tasks.", file=out_file)
            print(f"There are a total of {completed_task} completed tasks.", file=out_file)
            print(f"There are a total of {overdue_task} overdue tasks.", file=out_file)
            print(f"{(uncompleted_task / total_task * 100):.2f}% of tasks are uncompleted.", file=out_file)
            print(f"{(overdue_task / total_task * 100):.2f}% of tasks are overdue.", file=out_file)

        # writing results of various task totals and percentages to text file
        if user_name in parts[1]:
            user_task += 1
            if "No" in parts[-1]:
                user_uncompleted_task += 1
            elif "Yes" in parts[-1]:
                user_completed += 1
            if str(current_date.strftime("%Y %m %d")) in parts[5] and "No" in line:
                user_overdue_and_uncompleted += 1
        
            # checking if current user has any task if so checking working out information about there tasks
            with open("user_overview.txt", "w") as out_file:
                print(f"{user_name} has been assigned {user_task} tasks", file=out_file)
                print(f"{(user_task / total_task * 100):.2f}% of all tasks have been assigned {user_name}.", file=out_file)
                print(f"{(user_completed / user_task * 100):.2f}% of all tasks assigned {user_name} have been completed.",file=out_file)
                print(f"{(user_uncompleted_task / user_task * 100):.2f}% of all tasks assigned {user_name} still need "f"to be "f"completed.", file=out_file)
                print(f"{(user_overdue_and_uncompleted / user_task * 100):.2f}% of all tasks assigned {user_name} are "f"overdue and "f"need to be completed.", file=out_file)
                
#############################################################

#==================Login Section====================#

# This code reads usernames and password from the user.txt file to allow a user to login.
DATETIME_STRING_FORMAT = "%Y-%m-%d"
usernames = []
passwords = []

# Read in user_data
file =  open("user.txt", "r")

for lines in file:
#for each line in the file strip of spaces and split at the semi-colon
    temp = lines.strip().split(';')
    
    usernames.append(temp[0])
    passwords.append(temp[1])

file.close()
# If user not logged in
logged_in = False

while not logged_in:  #check the following when logging in  

    print("LOGIN")
    user_name = input("Username : ")
    pass_word = input("Password : ")

    if user_name not in usernames:
        print("You have entered an incorrect username......please try again")
        continue

    elif pass_word not in passwords:
        print("Password incorrect.......please try again")
        continue

    else:
        print(f"Welcome {user_name}, please choose an option:")
        logged_in = True

while logged_in:
    
    menu = input('''
r -  Register a user
a -  Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
ds - Display statistics
e -  Exit
: ''').lower()

    if menu == 'r':
# Request input of a new username
        new_username = input("New Username: ")

# Check if the new username already exists
        if new_username in usernames:
            print("This user already exists. Please try again.")
            continue
        
# Request input of a new password
        new_password = input("New Password: ")

# Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

# if passwords do not match ask user to try again   
        if confirm_password != new_password:
            print("The passwords do not match....please try again")
            continue

        print("New user added")

 # If they are the same, add them to the user.txt file,
        with open("user.txt", "a") as out_file:
            usernames.append(new_username)
            passwords.append(new_password)
            out_file.write(f"\n{new_username};{new_password}")

    if menu == 'a':
    
# Create tasks.txt if it doesn't exist
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as default_file:
                pass

# Read in existing task data
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]

# Datetime variable
        DATETIME_STRING_FORMAT = "%Y-%m-%d"
# Parse task data into a list of dictionaries
        task_list = []
        for id, t_str in enumerate(task_data):
            tasks = {}
            
# Split by semicolon and manually add each component
            task_components = t_str.split(";")
            tasks['ID'] = task_components [0]
            tasks['username'] = task_components[1]
            tasks['title'] = task_components[2]
            tasks['description'] = task_components[3]
            tasks['due_date'] = date.datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            tasks['assigned_date'] = date.datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
            tasks['completed'] = True if task_components[6] == "Yes" else False
            
            task_list.append(tasks)
        
# Request input for new task
        task_description = input("Task Description: ")
        task_title = input("Task Title: ")
        task_username = input("Username: ")
        task_due_date = input("Due Date (YYYY-MM-DD): ")
        task_assigned_date = input("Assigned Date (YYYY-MM-DD): ")
        task_completed = input("Completed (Yes/No): ").capitalize()

# Create new task dictionary
        new_task = {}
        new_task['ID'] = len(task_list)
        new_task['username'] = task_username
        new_task['title'] = task_title
        new_task['description'] = task_description
        new_task['due_date'] = date.datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
        new_task['assigned_date'] = date.datetime.strptime(task_assigned_date, DATETIME_STRING_FORMAT)
        new_task['completed'] = True if task_completed == "Yes" else False

# Append new task to task list
        task_list.append(new_task)

# Rewrite tasks.txt with updated task list
        with open("tasks.txt", 'w') as task_file:
            for task in task_list:
                task_file.write(f"{task['ID']};{task['username']};{task['title']};{task['description']};{task_due_date};{task_assigned_date};{task_completed}\n")

    if menu == 'va':
# Reads the task from task.txt file and prints to the console     
        with open ("tasks.txt", "r") as task_file:
            for lines in task_file:
                temp = lines.strip().split(';')
                disp_str = f"ID: \t\t {temp[0]}\n"
                disp_str += f"Task: \t\t {temp[2]}\n"
                disp_str += f"Assigned to: \t {temp[1]}\n"
                disp_str += f"Date Assigned: \t {temp[4]}\n"
                disp_str += f"Due Date: \t {temp[5]}\n"
                disp_str += f"Task Description: \n\t {temp[3]}\n"
                print("--------------------------")
                print(disp_str)
                print("--------------------------")

    if menu == 'vm':
# Retrieve task list
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]

        task_list = []
        for id, t_str in enumerate(task_data):
            tasks = {}
            
            # Split by semicolon and manually add each component
            task_components = t_str.split(";")
            tasks['ID'] = task_components [0]
            tasks['username'] = task_components[1]
            tasks['title'] = task_components[2]
            tasks['description'] = task_components[3]
            tasks['due_date'] = date.datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            tasks['assigned_date'] = date.datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
            tasks['completed'] = True if task_components[6] == "Yes" else False

            task_list.append(tasks)

        # Display tasks assigned to current user
        print("My Tasks:")
        for task in task_list:
            if task['username'] == user_name:
                disp_str = f"ID: \t\t {task['ID']}\n"
                disp_str += f"Task: \t\t {task['title']}\n"
                disp_str += f"Date Assigned: \t {task_components[5]}\n"
                disp_str += f"Due Date: \t {task_components[4]}\n"
                disp_str += f"Task Description: \n\t {task['description']}\n"
                disp_str += f"Completed: \t {'Yes' if task['completed'] else 'No'}\n"
                print("--------------------------")
                print(disp_str)
                print("--------------------------")

        # Allow user to select a task or return to the main menu
        task_selection = int(input("Enter the number of the task you want to edit/mark as complete, or enter -1 to return to the main menu: "))
        if task_selection == -1:
            continue
        
        # elif task_selection not in range(0,len(task_list)):
        #     print("Invalid task selection. Please try again.")
        
        elif task_selection > len(task_list):
            print("Invalid task selection. Please try again.")
            continue
        
        # Get selected task
        selected_task = task_list[task_selection]
        #print(task_selection)

        # Allow user to mark task as complete or edit the task
        task_action = input("Enter 'c' to mark the task as complete or 'e' to edit the task: ").lower()
        if task_action == 'c':

        # Mark task as complete
            task_data[task_selection] = f"{selected_task['ID']};{selected_task['username']};{selected_task['title']};{selected_task['description']};{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};Yes"
            with open('tasks.txt', 'w')as task_file:
                for line in task_data:
                    task_file.write(line + "\n")

            print("marked as complete")

        elif task_action == 'e':
    # Get selected task
            selected_task = task_list[task_selection]

            # Allow user to edit task
            if selected_task['completed']:
                print("Task is already complete and cannot be edited.")
                continue
            else:
                task_field = input("Enter 'u' to edit the user or 'd' to edit the due date: ").lower()
                if task_field == 'u':
                    # Edit task user
                    new_user = input("Enter the new user for the task: ")
                    selected_task['username'] = new_user
                    task_data[task_selection] = f"{selected_task['ID']};{selected_task['username']};{selected_task['title']};{selected_task['description']};{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};No"
                    with open('tasks.txt', 'w')as task_file:
                        for line in task_data:
                            task_file.write(line + "\n")
                    print("Task user updated.")
            
                elif task_field == 'd':
                    # Edit task due date
                    new_due_date = input("Enter the new due date for the task (yyyy-mm-dd): ")
                    selected_task['due_date'] = date.datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                    task_data[task_selection] = f"{selected_task['ID']};{selected_task['username']};{selected_task['title']};{selected_task['description']};{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};No"
                    with open('tasks.txt', 'w')as task_file:
                        for line in task_data:
                            task_file.write(line + "\n")

                    print("Task due date updated.")
                else:
                    print("Invalid input. Task not edited.")
            
    if menu == 'gr':

# Create task_overview.txt if it doesn't exist
        if not os.path.exists("task_overview.txt"):
            with open("task_overview.txt", "w") as input_file:
                generate_report()
                pass

# Read in existing task data
        with open("task_overview.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]
            generate_report()

# Create user_overview.txt if it doesn't exist
        if not os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "w") as input_file:
                generate_report()
                pass
# Read in existing task data
        with open("user_overview.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]
            generate_report()
        
    if menu == 'ds' and user_name == 'admin':

# If the user is logged in as admin they can retrieve stats on the other users
# Run function to generate the reports
        generate_report()

# Retrieve task list
        with open("task_overview.txt", 'r') as task_file:
            print("\n***Task Overview***\n")
            for line in task_file: 
                print(line, end = "")

        with open("user_overview.txt", 'r') as task_file:
            print("\n***User Overview***\n")
            for line in task_file:
                print(line, end = "")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()