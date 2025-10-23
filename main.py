import task_manager_functions as tmf

version_number = 1.0

options = [(1, 'Enter a new task'),
           (2, 'Mark a task complete'),
           (3, 'Display all tasks'),
           (4, 'Display a random task')]


task_file = "task_file.txt"  # file that is written and read from


print(f"Welcome to Task Manager v{version_number}")

tmf.display_options(options)

option = int(tmf.select_option())
match option:
    case 1:
        new_task = input("Enter a new task: ")
        tmf.add_task(task_file, new_task)
    case 2:
        tmf.display_all_tasks(task_file)
        completed_task = int(input("Which task have you completed: "))
        tmf.remove_task(task_file, completed_task)
    case 3:
        print("Here are your current tasks:")
        tmf.display_all_tasks(task_file)
    case 4:
        print("This isn't ready yet")
    case _:
        print("That's not a valid option")
