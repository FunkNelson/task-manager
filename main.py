# display options
# enter a task
# display all tasks
# complete a task
# grab a random task


version_number = 1.0

options = [(1, 'Enter a new task'),
           (2, 'Mark a task complete'),
           (3, 'Display all tasks'),
           (4, 'Display a random task')]


# To-do list file
task_file = "task_file.txt"


# Display options
def display_options(options):
    for option in options:
        print(f"{option[0]}.  {option[1]}")

# Add task


def add_task(file, task):
    with open(file, 'a') as f:
        f.write(f"{task}\n")
    f.close()

# Display all tasks


def display_all_tasks(file):
    try:
        with open(file, 'r') as f:
            i = 1
            print("Here are your current tasks")
            for line in f:
                print(f"{i}. {line.strip()}")
                i += 1
    except FileNotFoundError:
        print(f"The file {file} was not found")


# Program execution
print(f"Welcome to Task Manager v{version_number}")

display_options(options)

# add_task(task_file, "Drop off ballot")

display_all_tasks(task_file)
