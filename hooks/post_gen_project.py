import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m[WARNING]: "
INFO = "\x1b[1;33m[INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m[SUCCESS]: "
ERROR = "\033[31m[ERROR]: "


def remove(name: str):
    target = os.path.join(PROJECT_DIRECTORY, name)
    if os.path.isfile(target):
        os.remove(target)
    else:
        shutil.rmtree(target)


if __name__ == '__main__':
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        print(WARNING + 'open_source_license=Not open source')
        remove('LICENSE')

    if '{{ cookiecutter.use_make }}' != 'y':
        print(WARNING + 'add_makefile=False')
        remove('Makefile')

    if '{{ cookiecutter.use_docker }}' != 'y':
        print(WARNING + 'use_docker=False')
        remove('Dockerfile')
        remove('docker-compose.yml')
        remove('scripts')

    print(HINT, "\nYou can see guide at the https://github.com/0Kit/aiogram_template/blob/cookiecutter/README.md",
          TERMINATOR)
    print(SUCCESS + "Project {{ cookiecutter.project_name }} was successfully created\n",
          TERMINATOR)
