from datetime import date


def display_options(options):
    for option in options:
        print(f"{option[0]}.  {option[1]}")


def select_option() -> int:
    selection = input("Enter a number: ")
    return selection


def add_task(file, task):
    # task = input("Enter a new task: ")
    with open(file, 'a') as f:
        f.write(f"{task} | {date.today()}")
    f.close()


def remove_task(file, selection):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                if lines.index(line) + 1 != selection:
                    f.write(line)
                else:
                    add_task('completed_tasks.txt', line)
                    print(f"You have completed the task: {line}")
        f.close()
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_all_tasks(file):
    try:
        with open(file, 'r') as f:
            i = 1
            for line in f:
                print(f"{i}. {line.strip()}")
                i += 1
        f.close()
    except FileNotFoundError:
        print(f"The file {file} was not found")
