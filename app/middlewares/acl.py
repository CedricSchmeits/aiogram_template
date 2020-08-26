from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from app.db_api.models import User


class ACLMiddleware(BaseMiddleware):
    @staticmethod
    async def setup_chat(data: dict, user: types.User):
        user_id = user.id

        user = await User.get(user_id)
        if user is None:
            user = await User.create(id=user_id)

        data["user"] = user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user)
