import task_manager_functions as tmf

task_file = "task_file.txt"
completed_task_file = "completed_tasks.txt"

version_number = 1.0
tmf.display_title(version_number)
session_active = True

options = [(1, 'Enter a new task'),
           (2, 'Mark a task complete'),
           (3, 'Display pending tasks'),
           (4, 'Display completed tasks'),
           (5, 'Exit program')]

while session_active:
    tmf.display_options(options)
    option = int(tmf.select_option())
    match option:
        case 1:
            new_task = input("Enter a new task: ")
            tmf.add_task(task_file, f"\n{new_task}")
            input('Press Enter to continue...')
        case 2:
            print("\nCURRENT TASK | DATE ENTERED")
            tmf.display_all_tasks(task_file)
            completed_task = int(input("Which task have you completed: "))
            tmf.remove_task(task_file, completed_task, completed_task_file)
            input('Press Enter to continue...')
        case 3:
            print("\nCURRENT TASK | DATE ENTERED")
            tmf.display_all_tasks(task_file)
            input('Press Enter to continue...')
        case 4:
            print("\nCOMPLETED TASK | DATE ENTERED | DATE COMPLETED")
            tmf.display_all_tasks(completed_task_file)
            input('Press Enter to continue...')
        case 5:
            print("Goodbye\n")
            session_active = False
        case _:
            print("That's not a valid option")
