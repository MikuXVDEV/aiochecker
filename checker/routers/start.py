from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import BaseMiddleware, Bot
from checker import CHANNEL_ID

start_router = Router()


@start_router.message(Command("start"))
async def checker(
    message: Message,
    user: dict
    ) -> None:
    await message.answer(
        f"👋 {user.mention} |<b>\n\nПривет, я -> Бот, чекер подписок. Что бы начать работать -> просто, добавьте меня в группу.</b>", 
        parse_mode="HTML")