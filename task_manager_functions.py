from datetime import date


def display_options(options):
    print('\n')
    for option in options:
        print(f"{option[0]}. {option[1]}")


def select_option() -> int:
    selection = input("\nEnter a number: ")
    return selection


def add_task(file, task):
    with open(file, 'a') as f:
        f.write(f"{task} | {date.today()}")


def remove_task(file, selection, done_file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for index, line in enumerate(lines):
                if index + 1 != selection:
                    f.write(line)
                else:
                    add_task(done_file, f"\n{line.strip()}")
                    print(f"You have completed the task: {line}")
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_all_tasks(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                print(f"{index + 1}. {line.strip()}")
        print("\n")
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_title(version):
    print('\n')
    print('___________              __        _____                                             ')
    print('\\__    ___/____    _____|  | __   /     \\ _____    ____ _____     ____   ___________ ')
    print('  |    |  \\__  \\  /  ___/  |/ /  /  \\ /  \\\\__  \\  /    \\\\__  \\   / ___\\_/ __ \\_  __ \\')
    print('  |    |   / __ \\_\\___ \\|    <  /    Y    \\/ __ \\|   |  \\/ __ \\_/ /_/  >  ___/|  | \\/')
    print('  |____|  (____  /____  >__|_ \\ \\____|__  (____  /___|  (____  /\\___  / \\___  >__|   ')
    print('               \\/     \\/     \\/         \\/     \\/     \\/     \\//_____/      \\/     ')
    print(f'                                               version {version} ')
