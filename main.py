import task_manager_functions as tmf

version_number = 1.0

options = [(1, 'Enter a new task'),
           (2, 'Mark a task complete'),
           (3, 'Display pending tasks'),
           (4, 'Display completed tasks')]


task_file = "task_file.txt"
completed_task_file = "completed_tasks.txt"

# print(f"Welcome to Task Manager v{version_number}")
tmf.display_title(version_number)
tmf.display_options(options)

option = int(tmf.select_option())
match option:
    case 1:
        new_task = input("Enter a new task: ")
        tmf.add_task(task_file, f"\n{new_task}")
    case 2:
        tmf.display_all_tasks(task_file)
        completed_task = int(input("Which task have you completed: "))
        tmf.remove_task(task_file, completed_task, completed_task_file)
    case 3:
        print("\nCURRENT TASK | DATE ENTERED")
        tmf.display_all_tasks(task_file)
    case 4:
        print("\nCOMPLETED TASK | DATE ENTERED | DATE COMPLETED")
        tmf.display_all_tasks(completed_task_file)
    case _:
        print("That's not a valid option")
