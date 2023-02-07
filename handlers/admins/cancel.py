from loader import dp
from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.inline_keyboard import keyboard

@dp.message_handler(commands=["cancel"], state='*', chat_id = ADMINS)
async def atmen(msg : types.Message,state : FSMContext):
    await msg.answer("<i>Cancel</i>")
    await state.finish()