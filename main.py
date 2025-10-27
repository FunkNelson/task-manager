import task_manager_functions as tmf

task_file_pending = "tasks_pending.txt"
task_file_recurring = "tasks_recurring.txt"
task_file_completed = "tasks_completed.txt"

version_number = 1.10
tmf.display_title(version_number)
session_active = True

options = [(1, 'Enter a new one-time task'),
           (2, 'Enter a new recurring task'),
           (3, 'Mark a one-time task complete'),
           (4, 'Mark a recurring task complete'),
           (5, 'Display pending one-time tasks'),
           (6, 'Display pending recurring tasks'),
           (7, 'Display completed tasks'),
           (8, 'Exit program')]

while session_active:
    tmf.display_options(options)
    option = int(tmf.select_option())
    match option:
        case 1:
            new_task = input("Enter a new task: ")
            tmf.add_task(task_file_pending, f"\n{new_task}")
            input('Press Enter to continue...')
        case 2:
            print("Feature in development")
        case 3:
            print("\nCURRENT TASK | DATE ENTERED")
            tmf.display_all_tasks(task_file_pending)
            completed_task = int(input("Which task have you completed: "))
            tmf.remove_task(task_file_pending, completed_task,
                            task_file_completed)
            input('Press Enter to continue...')
        case 4:
            print("Feature in development")
        case 5:
            print("\nCURRENT TASK | DATE ENTERED")
            tmf.display_all_tasks(task_file_pending)
            input('Press Enter to continue...')
        case 6:
            print("Feature in development")
        case 7:
            print("\nCOMPLETED TASK | DATE ENTERED | DATE COMPLETED")
            tmf.display_all_tasks(task_file_completed)
            input('Press Enter to continue...')
        case 8:
            print("Goodbye\n")
            session_active = False
        case _:
            print("That's not a valid option")
