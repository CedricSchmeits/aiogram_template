import argparse
import asyncio
from app import config
from app.db_api.database import connect
from app.db_api.models import User
from app.loader import db
from loguru import logger


def create_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-a', '--add-admins', action='store_const', const=True, default=False,
                            help='Delete the created table')
    arg_parser.add_argument('-d', '--drop-tables', action='store_const', const=True, default=False,
                            help="Add the admin_id's from environment variable")
    return arg_parser


async def cli():
    parser = create_parser()
    namespace = parser.parse_args()

    await connect()
    if namespace.drop_tables:
        logger.warning('Dropping tables')
        await db.gino.drop_all()

    logger.info('Creating tables')
    await db.gino.create_all()

    if namespace.add_admins:
        logger.info('Adding administrators')
        for admin_id in config.ADMINS_ID:
            await User.create(id=int(admin_id), is_superuser=True)
            logger.debug(f'Administrator {admin_id} was added to the table')

    await db.pop_bind().close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cli())
