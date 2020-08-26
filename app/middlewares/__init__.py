from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from .throttling import ThrottlingMiddleware
from .acl import ACLMiddleware


async def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(ACLMiddleware())
    logger.info('Middlewares are successfully configured')
