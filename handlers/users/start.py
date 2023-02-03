from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalomu alaykum {message.from_user.get_mention(message.from_user.full_name)}.</b>")
    await message.answer(f"<b>Savolingiz yoki taklifingiz bo`lsa yozib qoldiring</b>\n\n<i>Tez orada javob beriladi!</i>")
    for admin in ADMINS:
        await bot.send_message(admin, f"<b>Foydalanuvchi : {message.from_user.full_name} xabar yubordi</b>")