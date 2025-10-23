# display options
# enter a task
# display all tasks
# complete a task
# grab a random task


version_number = 1.0

task_list = [(1, 'Enter a new task'),
             (2, 'Mark a task complete'),
             (3, 'Display all tasks'),
             (4, 'Display a random task')]


def display_tasks(task_list):
    for task in task_list:
        print(f"{task[0]}.  {task[1]}")


# Program execution
print(f"Welcome to Task Manager v{version_number}")

display_tasks(task_list)
