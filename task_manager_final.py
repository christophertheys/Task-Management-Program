print("\t \t \t Welcome to the task manager program !\n \t \t All your administrative tasks sorted in one place"
      .upper())
print("\n")
print(" You need to enter a valid username and password in order to access the task manager program \n")

# Starting point was opening up the user.txt in order for the program to read over the info from the file to validate
# any inputted information

with open("user_for_manager.txt", "r") as master_file:
    validity_check = master_file.read()
    user_name_input = str(input("Enter your username : "))
    user_password = str(input("Enter your password : "))
    print("\n")
    # The inputted data will be validated against the valid usernames and passwords in the text file
    if user_password and user_password in validity_check:
        print("\t \t \t Valid username and password \n" "\t \t \t \t Access Granted \n".upper())
    elif user_name_input and user_password not in master_file:
        raise Exception("This user is invalid \n")
master_file.close()
# If the user does not enter a valid input, the program will prompt the user to try again until a valid username
# and password have been entered
while True:
    selection_menu = input("Select one of the following options below  \n"
                           "r - Register a new user \n"
                           "a - Adding a task \n"
                           "va - View all tasks \n"
                           "vm - view my task \n"
                           "gr - Generate reports \n"
                           "ds - Display statistics \n"
                           "e - Exit \n"
                           "Type in desired option :  \n").lower()
    print("\n")
    if selection_menu == 'r':
        if user_name_input != "admin":
            print("Invalid authorisation to register users".upper())
        else:
            print(" \t \t \t You have selected to add a new user to the system \n ")
            admin_path_decision = int(input("Enter '1' to view the statistic menu or "
                                            "Enter '2' to register a new user : \n"))
            if admin_path_decision == 1:
                with open("statistic_menu_for_admin", "r") as admin_file, open("tasks_for manager.txt", "r") \
                        as overview_of_tasks:
                    for line in admin_file:
                        file_split = line.replace(", ", "\n")
                        print("\n", file_split)
                admin_file.close()
                break
            # The user.txt file will be opened once more in order to add a new user to the file of approved usernames
            # and passwords
            else:
                with open("user_for_manager.txt", "r") as new_user_file_read:
                    new_user_name = input("Enter the new username : ")
                    new_user_password = input("Enter the new user password : ")
                    validity_check_for_existing_user = new_user_file_read.read()
                    if new_user_name and new_user_password in validity_check_for_existing_user:
                        print("\n \t \t Username and Password already exists on file".upper())
                    else:
                        with open("user_for_manager.txt", "a") as new_user_file_addition:
                            print(new_user_name + "\n" + new_user_password + "\n")
                            confirmation_of_user = int(input("Type in '1' to confirm the above username and "
                                                             "password : "))
                            if confirmation_of_user != 1:
                                print("The username and password has not been confirmed... Try again...")
                            # Where the desired username or password is not what the user desires, the program will
                            # prompt the user to try again
                            else:
                                print("\n \t \t \t Username and password is confirmed \n \n \t \t"
                                      "A new user has been successfully created !".upper())
                            new_user_file_addition.write("\n" + new_user_name + "," + " " + new_user_password)
        break
    # The open file is closed to ensure that the text file is no longer referred to after the conditional statement

    elif selection_menu == 'a':
        print("\n \t \t \t You have selected to add a task for an employee".upper(),
              "\n \n \t You will need to enter the "
              "username of the team member for which"
              " the task will be assigned to \n")
        with open("tasks_for manager.txt", "a") as task_file:
            # The task file is referred to because this is where all allocated tasks can be found
            user_name_input = input("Enter the username : ")
            task_number = input("Enter the task number to be assigned : ")
            task_title = input('Enter the title of the task : ')
            task_description = input("Enter a description of the task : ")
            current_date = input("Enter the current date (so that the assignment date of the task is declared) : ")
            task_due_date = input("Enter the due data of the task : ")
            print("\n \t \t All the information relevant for this task has been included ! \n")
            task_file.write("\n \n" + user_name_input + ", " + " " + task_number + "," + " " + task_title + "," + " "
                            + task_description + "," + " " + current_date + "," + " " + task_due_date + "," + " "
                            + "No (Task not yet complete) \n ")
        task_file.close()
        break
    # The assigned tasks will be compiled and added to the task text file  using all information inputted

    elif selection_menu == 'va':
        print("\t \t \t You have selected to view all the task \n".upper())
        with open("tasks_for manager.txt", "r") as file_view:
            for line in file_view:
                file_split = line.replace(", ", "\n")
                print(file_split)
            break
    # This task viewer code has split up all the data in the text file in an easy-to-read format
    elif selection_menu == 'vm':
        print("\n User currently logged in : " + user_name_input + "\n")
        print("\n You have selected to view all the tasks assigned to your user login credentials \n".upper())

        with open("tasks_for manager.txt", "r") as user_task_viewer:
            for user_name_input in user_task_viewer:
                file_view = user_name_input.replace(",", "\n")
                print(file_view)
            escape: Exception("Enter a valid username who has been allocated a task")
            further_selection = int(input("Further Selection \n \n Select a task by entering the 'task number' \n "
                                          "Or \n select '-1' to return to the main menu : ".upper()))
            if further_selection == -1:
                print(selection_menu)
            else:
                print("\n You have selected a specific task \n \n")
                with open("/Users/molemotheys/Desktop/tasks_for manager.txt", "a") as amendment_of_tasks:
                    task_amend_choice = input(" \t \t \t The amendments to the task consist of  \n "
                                              "Mark the task as complete \n or; \n Edit the task \n "
                                              "\t \t Type in task selection : \n")
                    if len(task_amend_choice) > 14:
                        print("You have selected to mark the task as complete")
                        user_name_input = input("Enter the username : ")
                        task_number = input("Enter the task number to be assigned : ")
                        task_title = input('Enter the title of the task : ')
                        task_description = input("Enter a description of the task : ")
                        current_date = input(
                            "Enter the current date (so that the assignment date of the task is declared) : ")
                        task_due_date = input("Enter the due data of the task : ")
                        print("\n \t \t All the information relevant for this task has been included ! \n")
                        amendment_of_tasks.write("\n \n" + user_name_input + ", " + " " + task_number + "," + " " +
                                                 task_title + "," + " " + task_description + "," + " " + current_date
                                                 + "," + " " + task_due_date + "," + " "
                                                 + "Yes (Task is complete) \n ")
                    else:
                        print("You have selected to edit the task")
                        user_name_input = input("Enter the username : ")
                        task_number = input("Enter the task number to be assigned : ")
                        task_title = input('Enter the title of the task : ')
                        task_description = input("Enter a description of the task : ")
                        current_date = input(
                            "Enter the current date (so that the assignment date of the task is declared) : ")
                        task_due_date = input("Enter the due data of the task : ")
                        print("\n \t \t All the information relevant for this task has been included ! \n")
                        amendment_of_tasks.write("\n \n" + user_name_input + ", " + " " + task_number + "," + " " +
                                                 task_title + "," + " " + task_description + "," + " " + current_date
                                                 + "," + " " + task_due_date + "," + " " +
                                                 "No (Task not yet complete) \n ")
                break
        user_task_viewer.close()
    elif selection_menu == 'gr':
        with open("tasks_for manager.txt", "r+") as task_reader, open("task_overview.txt", "a+") as task_overview:
            for line in task_overview:
                task_overview.write(line)
                print(task_overview)
            break
    elif selection_menu == 'ds':
        with open("user_for_manager.txt", "r") as user_read_file, open("user_overview.txt", "a+") as user_overview:
            for line in user_overview:
                user_overview.write(line)
                print(user_overview)
            break

    elif selection_menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have entered an invalid option. Please Try again... \n")
