from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, config
from app.loader import dp

# The configuration of the modules using import
from app import middlewares, filters, handlers

from app.db_api import database


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_logger()
    await database.connect()
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins()


async def on_shutdown(dispatcher: Dispatcher):
    await database.close_connection()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=config.SKIP_UPDATES)
