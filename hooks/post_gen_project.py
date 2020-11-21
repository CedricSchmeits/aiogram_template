import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m[WARNING]: "
INFO = "\x1b[1;33m[INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m[SUCCESS]: "
ERROR = "\033[31m[ERROR]: "


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        remove_file('LICENSE')

    if '{{ cookiecutter.add_makefile }}' != 'y':
        remove_file('Makefile')

    print(HINT, "\nYou can see guide at the https://github.com/0Kit/aiogram_template/blob/cookiecutter/README.md",
          TERMINATOR)
    print(SUCCESS + "Project {{ cookiecutter.project_name }} was successfully created\n",
          TERMINATOR)
