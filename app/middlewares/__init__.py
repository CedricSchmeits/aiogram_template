from aiogram import Dispatcher
from loguru import logger

from .throttling import ThrottlingMiddleware


async def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    logger.info('Middlewares are successfully configured')
