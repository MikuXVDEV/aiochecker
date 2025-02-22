from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Dict, Awaitable, Any

from ..entities import User
from checker import CHANNEL_ID
from ..utils.utils import formatted_from_mention, check_user_in_channel


class Middleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ):

        is_channel =  await check_user_in_channel(event, data['bot'])
        mention = await formatted_from_mention(event)
        channel_link = await data['bot'].get_chat(CHANNEL_ID)

        data["user"] = User(
            mention=mention,
            is_channel=is_channel,
            channel_link=channel_link
            )
            
        await handler(event, data)