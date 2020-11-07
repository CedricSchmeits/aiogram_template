import asyncio
import typing
from aiogram.utils import exceptions
from loguru import logger
from asyncio import sleep

from app.misc import bot


class Broadcast:
    __started = False

    def __init__(self, users: typing.List[int], text: str, disable_notification: bool = False, timeout: int = 0.02):
        self.users = users
        self.text = text
        self.disable_notification = disable_notification
        self.count = 0
        self.timeout = timeout

    async def send_message(self, user_id: int) -> bool:
        try:
            await bot.send_message(user_id, self.text, disable_notification=self.disable_notification)
        except exceptions.BotBlocked:
            logger.debug(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            logger.debug(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            logger.debug(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await sleep(e.timeout)
            return await self.send_message(user_id)  # Recursive call
        except exceptions.UserDeactivated:
            logger.debug(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            logger.exception(f"Target [ID:{user_id}]: failed")
        else:
            logger.debug(f"Target [ID:{user_id}]: success")
            return True
        return False

    async def start(self) -> int:
        for user_id in self.users:
            if await self.send_message(user_id):
                self.count += 1
            await asyncio.sleep(self.timeout)
        return self.count
