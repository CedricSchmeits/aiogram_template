from aiogram import Dispatcher
from aiogram.utils import executor

from app.config import SKIP_UPDATES
from app.loader import dp

from app import utils, middlewares, filters


async def on_startup(dp: Dispatcher):
    await utils.setup_logger()
    await middlewares.setup(dp)
    await filters.setup(dp)
    from app import handlers
    await utils.setup_default_commands(dp)
    await utils.notify_admins(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=SKIP_UPDATES)
