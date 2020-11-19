from typing import List, Option

from loguru import logger

from app.utils import Broadcast


async def notify_admins(admins: Option[List[int], List[str], int, str]):
    count = await (Broadcast(admins, 'The bot is running!')).start()
    logger.info(f"{count} admins received messages")
