from contextlib import suppress

from aiogram import Dispatcher
from aiogram.utils import executor
from gino import UninitializedError

from app import utils, middlewares, filters, config
from app.loader import dp
from app.db_api.database import connect, db


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_logger()
    await connect()
    await middlewares.setup(dispatcher)
    await filters.setup(dispatcher)
    from app import handlers
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins()


async def on_shutdown(dispatcher: Dispatcher):
    with suppress(UninitializedError):
        await db.pop_bind().close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=config.SKIP_UPDATES)
