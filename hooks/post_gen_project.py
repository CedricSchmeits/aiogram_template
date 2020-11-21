import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        remove_file('LICENSE')

    if '{{ cookiecutter.add_makefile }}' != 'y':
        remove_file('Makefile')

    print("\nYou can see guide at the https://github.com/0Kit/aiogram_template/blob/cookiecutter/README.md")
    print("Project {{ cookiecutter.project_name }} was successfully created\n")
