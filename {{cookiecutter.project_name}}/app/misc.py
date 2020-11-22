from aiogram import Bot, Dispatcher, types

{%- if cookiecutter.use_redis == "y" %}
from aiogram.contrib.fsm_storage.redis import RedisStorage2
{%- else %}
from aiogram.contrib.fsm_storage.memory import MemoryStorage
{%- endif %}

from gino import Gino

from app import config

db = Gino()

bot = Bot(
    token=config.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)
{% if cookiecutter.use_redis == "y" %}
storage = RedisStorage2(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
)
{% else %}
storage = MemoryStorage()
{% endif %}
dp = Dispatcher(
    bot=bot,
    storage=storage,
)

__all__ = (
    "bot",
    "storage",
    "dp",
    "db",
)
