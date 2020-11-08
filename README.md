# Bot written using [Forzend's](https://t.me/Forzend) template

## Setting up

### Poetry

**_Make sure you have installed [poetry](https://python-poetry.org/docs/)._**

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