"""
Employers list
In new file for clear code.
"""


employers = []
try:
    with open("polls/static/data/employers") as f:
        for line in f:
            employers.append(line)
except FileNotFoundError:

    print ('\033[93m'
           + "WARNING: File: polls/static/data/employers not found!\n"
           + '\033[0m')
