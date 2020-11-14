# Aiogram bot template by [Forzend](https://t.me/Forzend)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-5.0-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![Aiogram](https://img.shields.io/badge/aiogram-2.11.2-blue)](https://pypi.org/project/aiogram/)
[![Docker](https://img.shields.io/badge/Docker-Yes-success)](https://www.docker.com/get-started)

Template based on [Forden's template](https://github.com/Forden/aiogram-bot-template) for creating scalable bots with aiogram

## Structure
<details>
  <summary>first button</summary>  
  <details>
    <summary>second button</summary>    
  </details>
</details>



## Setting up

### Poetry

**_Make sure you have installed [poetry](https://python-poetry.org/docs/#installation)._**

1. Rename `.env.dist` to `.env` and fill in your Redis, Postgres credentials and a bot token.

2. Install requirements
   ```cmd
   $ poetry update && poetry install
   ```
3. Apply alembic migrations
   ```cmd
   $ poetry run alembic upgrade head
   ```
4. Run the script with poetry
   ```cmd
   $ poetry run python app
   ```

### Docker

**_Make sure you have installed [docker](https://docs.docker.com/) & [docker-compose](https://docs.docker.com/compose/)_**

1. Rename `.env.dist` to `.env` and fill in your Redis, Postgres credentials and a bot token.

2. Run the project
    ```cmd
    sudo docker-compose up -d
    ```