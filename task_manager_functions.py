def display_options(options):
    for option in options:
        print(f"{option[0]}.  {option[1]}")


def select_option() -> int:
    selection = input("Enter a number: ")
    return selection


def add_task(file, task):
    with open(file, 'a') as f:
        f.write(f"{task}\n")
    f.close()


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
