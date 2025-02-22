from aiogram import Bot
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest 

from checker import CHANNEL_ID


async def formatted_from_mention(message: Message) -> str:
    return f"<a href='tg://user?id=6506201559'>‌{message.from_user.first_name}</a>"


async def check_user_in_channel(message: Message, bot: Bot) -> bool:
    status_user = None
    try:
        status_user = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        return status_user.status not in ('left', 'kicked', 'banned')

    except TelegramBadRequest:
        return False

    except Exception as e:
        await message.answer(
            f"🤨 | <b>Ну нихуя себе, у нас ошибка:</b> \n{e}",
            parse_mode='HTML')
        return False
