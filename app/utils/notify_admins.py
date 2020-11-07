from app.config import ADMINS_ID
from app.utils import Broadcast
from loguru import logger


async def notify_admins():
    count = await (Broadcast(ADMINS_ID, 'The bot is running!')).start()
    logger.info(f"{count} admins received messages")
