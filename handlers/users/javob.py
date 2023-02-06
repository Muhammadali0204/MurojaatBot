from aiogram import types
from data.config import ADMINS


from loader import dp, bot

@dp.message_handler()
async def javob(message : types.message):
    await message.answer("<b>Xabaringiz qabul qilindi</b>✅\n\n<i>Tez orada javob beriladi!</i>")
    for admin in ADMINS:
        await bot.send_message(admin, f"<b>Foydalanuvchi : {message.from_user.full_name} xabar yubordi</b>")