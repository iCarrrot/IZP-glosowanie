"""
Employers list
In new file for clear code.
"""


class Employers:
    __list = None

    @classmethod
    def get_list(cls):
        if cls.__list is None:
            data = []
            try:
                with open("polls/static/data/employers") as f:
                    data = f.read().split('\n')

            except FileNotFoundError:
                print('\033[93m'
                      + "WARNING: File: polls/static/data/employers not found!"
                      + '\n' + '\033[0m')

            cls.__list = data

        return cls.__list
