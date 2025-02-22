import asyncio
from aiogram import Dispatcher, Bot

from checker import TOKEN, OWNER
from .routers import start, checker
from .middlewares.middlewares import Middleware


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN)
    dp.include_routers(
        start.start_router,
        checker.checker_router)

    start.start_router.message.middleware(Middleware())
    checker.checker_router.message.middleware(Middleware())
        
    async with bot:
        await bot.send_message(
            chat_id=OWNER,
            text=f"😘 | <b>Здарова заебал, я воркаю.</b>",
            parse_mode='HTML'
            )

    await dp.start_polling(bot)
    

    

asyncio.run(main())