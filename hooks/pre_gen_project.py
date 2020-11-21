import re
import sys
from pathlib import Path


# TODO Create module for hooks regexes
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
VERSION_REGEX = r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$'


# TODO Create module for hooks exceptions
class ProjectNameError(Exception):
    ...


class ProjectVersionError(Exception):
    ...


def validate_module_name(module_name: str):
    if not re.match(MODULE_REGEX, module_name):
        raise ProjectNameError(
            f'ERROR: The project name ({module_name}) is not a valid Python module name. '
            'Please do not use a - and use _ instead'
        )


def validate_version(version: str):
    if not re.match(VERSION_REGEX, version):
        raise ProjectVersionError(
            f'ERROR: The verison ({version}) is not a valid Python version. '
            'Read PEP440 for more information'
        )


if __name__ == '__main__':
    validate_module_name('{{ cookiecutter.project_name}}')
    validate_version('{{ cookiecutter.version }}')
