import re
import sys
from pathlib import Path


# REGEXES
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
VERSION_REGEX = r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$'

# COLORS
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m[WARNING]: "
INFO = "\x1b[1;33m[INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m[SUCCESS]: "
ERROR = "\033[31m[ERROR]: "


def validate_module_name(module_name: str):
    if not re.match(MODULE_REGEX, module_name):
        print(
            ERROR,
            f'The project name "{module_name}" is not a valid Python module name. '
            'Please do not use a - and use _ instead',
            TERMINATOR
        )
        exit(1)


def validate_version(version: str):
    if not re.match(VERSION_REGEX, version):
        print(
            ERROR,
            f'The version "{version}" is not a valid Python version. '
            'Read PEP440 for more information',
            TERMINATOR
        )
        exit(1)


if __name__ == '__main__':
    validate_module_name('{{ cookiecutter.project_name}}')
    validate_version('{{ cookiecutter.version }}')
