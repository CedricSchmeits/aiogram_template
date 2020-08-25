import asyncclick as click

from app import config
from app.db_api.database import init_engine
from app.db_api.models import User
from app.loader import db
from loguru import logger


@click.command()
@click.option('-d', '--drop', is_flag=True, help='Delete the created table')
@click.option('-a', '--add-admins', is_flag=True, help="Add the admin_id's from environment variable")
async def cli(drop: bool = False, add_admins: bool = False):
    await init_engine()

    if drop:
        logger.warning('Dropping tables')
        await db.gino.drop_all()

    logger.info('Creating tables')
    await db.gino.create_all()

    if not add_admins:
        return

    logger.info('Adding administrators')
    for admin_id in config.ADMINS_ID:
        await User(id=int(admin_id), is_superuser=True).create()
        logger.debug(f'Administrator {admin_id} was added to the table')


if __name__ == "__main__":
    cli(_anyio_backend='asyncio')
