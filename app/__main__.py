from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, middlewares, filters, config
from app.loader import dp
from app.db_api.database import connect


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_logger()
    await connect()
    await middlewares.setup(dispatcher)
    await filters.setup(dispatcher)
    from app import handlers
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=config.SKIP_UPDATES)
