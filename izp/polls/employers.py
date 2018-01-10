"""
Employers list
In new file for clear code.
"""


def get_employers_list():

    employers = []
    try:
        with open("polls/static/data/employers") as f:
            employers = f.read().split('\n')

    except FileNotFoundError:
        print('\033[93m'
              + "WARNING: File: polls/static/data/employers not found!\n"
              + '\033[0m')

    return employers
