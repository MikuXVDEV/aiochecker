from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


checker_router = Router()


@checker_router.message(F.chat.type == ChatType.SUPERGROUP or ChatType.GROUP)
async def checker_subscription(
    message: Message,
    user: dict
    ) -> None:

    keyboard = InlineKeyboardBuilder([
        [
            InlineKeyboardButton(text="👋 | ВОТ КАНАЛ", url=user.channel_link.invite_link)
        ]
    ]).as_markup()

    if not user.is_channel:
        await message.delete()
        await message.answer(
            f"🧏‍♀️ | {user.mention}\nГандон ебучий, в канал сначала зайди.",
            parse_mode='HTML',
            reply_markup=keyboard
            )
        return

    await message.answer(
        f"❤️ | Пасиба что подписался",
        parse_mode='HTML'
        )
