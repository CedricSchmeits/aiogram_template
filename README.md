# Aiogram bot template by [Forzend](https://t.me/Forzend)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-5.0-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![Aiogram](https://img.shields.io/badge/aiogram-2.11.2-blue)](https://pypi.org/project/aiogram/)
[![Docker](https://img.shields.io/badge/Docker-Yes-success)](https://www.docker.com/get-started)

Template based on [Forden's template](https://github.com/Forden/aiogram-bot-template) for creating scalable bots with aiogram


## Setting up

1. **_Make sure you have installed [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)._**

2. Generate project
    ```commandline
    cookiecutter https://github.com/0Kit/aiogram_template.git
    ```

3. Make changes to the project

4. Make migrations _(Choose one of the options)_

    **Using make**

    ```commandline
    make makemigrations
    ```

    **Using poetry**
    
    _Make sure you have installed [poetry](https://python-poetry.org/docs/#installation)_
    ```commandline
    poetry run alembic revision --autogenerate -m init 
    ```
5. Run project _(Choose one of the options)_
    
    **In docker container(using make)**
    
    _Make sure you have installed [poetry](https://python-poetry.org/docs/#installation) and Make_
    
    ```commandline
    make app-create
    ```
   
   **In Docker(without extraneous tools)**
   ```commandline
    docker-compose up -d
    ```
   
   **In your system**
   
   _Make sure you have installed [poetry](https://python-poetry.org/docs/#installation)_
   
   ```commandline
   python3 -m app
   ```

## Development

### dependencies
<details>
    <summary>Click here to see some system dependencies</summary>

* [Python](https://www.python.org/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://www.docker.com/get-started)
* [docker-compose](https://github.com/docker/compose#where-to-get-docker-compose)
* [make](https://en.wikipedia.org/wiki/Make_(software)) _[required]_
</details>

### Structure

* app —  the source of the application
    * filters — module with custom
    * handlers — module with all project handlers
    * keyboards — module with telegram keyboards
        * inline
        * reply
    * middlewares — module with aiogram middlewares
    * models — module with batabase models
    * states — module aiogram state groups 
    * utils — module with any project utils
    * __main__.py — Entrypoint
        * config.py — project constants loaded from the. env file
        * misc.py — project global varibles there
* migrations — database migration module [automatically generated by alembic]
* scripts — bash scripts
        * docker-entrypoint.sh — bash script for launching the application in a Docker container
* .env.dist — example for .env file
* .flake8 — flake8 config

### Make commands

All commands are in the `Makefile` and are used by `make [options] [command] [variables]`

`app-create` — build and run start application

`app-logs` — check application log

`app-strart` — start the application

`app-stop` — stop the application

`app-down` — down the application

`app-destroy` — down the application with removing containers for services not defined in the
 Compose file and named volumes declared in the `volumes` section of the Compose file and anonymous
 volumes attached to containers.

<details>
    <summary>Click here to see all make commands</summary>


#### Linters

`isort` — format code using isort

`black` — format code using black

`flake8` — lint code using flake8

`lint` — use all code formatters and linters


#### Migrations

`alembic ${args}` — run alembic with some args

`makemigrations` — create new migrations based on the changes you have made to your models.

`migrate` — apply all migrations

`downgrade` — go back to the previous version of migrations

#### Docker

`docker-config` — is the same as `docker-compose config`

`docker-ps` — is the same as `docker-compose ps`

`docker-build` — is the same as `docker-compose build`

`docker-up-dependencies` — up dependencies in docker-compose

`docker-up` — up the app with its dependencies

`docker-stop` — is the same as `docker-compose stop`

`docker-down` — is the same as `docker-compose down`

`docker-destroy` — destroy application

`docker-logs` — show application log
</details>