from contextlib import suppress

from aiogram.utils.exceptions import TelegramAPIError
from loguru import logger

from aiogram import Dispatcher
from asyncio import sleep

from app.config import ADMINS_ID


async def notify_admins(dp: Dispatcher):
    for admin_id in ADMINS_ID:
        with suppress(TelegramAPIError):
            await dp.bot.send_message(admin_id, "Bot is started", disable_notification=True)
        logger.debug("Notified superuser {user} about bot is started.", user=admin_id)

        await sleep(0.3)
