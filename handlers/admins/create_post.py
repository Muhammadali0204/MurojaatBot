from loader import dp, temp
from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.inline_keyboard import keyboard

@dp.message_handler(commands="create",chat_id = ADMINS)
async def post(msg : types.Message, state : FSMContext):
    temp[1] = ["", [], []]
    await msg.answer("<b>Matnini yuboring : </b>")
    await state.set_state("matn")
    
    
@dp.message_handler(state="matn")
async def matn(msg : types.Message, state : FSMContext):
    temp[1][0] = msg.html_text
    await msg.answer("<b>Matn qabul qilindi!</b>\n\n<b>Inline keybord uchun linklarni yuboring : </b>")
    await state.set_state("link")
    
@dp.message_handler(state='link')
async def link(msg : types.Message, state : FSMContext):
    temp[1][1].append(msg.text)
    await msg.answer(f"<b>Endi esa <i>{msg.text}</i> uchun nom yuboring : </b>")
    await state.set_state("nom")
    
@dp.message_handler(state="nom")
async def nom(msg : types.Message, state : FSMContext):
    temp[1][2].append(msg.text)
    await msg.answer(temp[1][0], reply_markup=keyboard(temp[1][1], temp[1][2], True))
    await state.set_state("tasdiq")
    
    
@dp.callback_query_handler(state="tasdiq", text="ok")
async def tasdiq(call : types.CallbackQuery, state : FSMContext):
    await call.message.delete()
    await call.message.answer(temp[1][0], reply_markup=keyboard(temp[1][1], temp[1][2], False))
    await call.answer("Tuzildi✅")
    await state.finish()
    
@dp.callback_query_handler(text="davom", state="tasdiq")
async def qayta(call : types.CallbackQuery, state : FSMContext):
    await call.message.delete()
    await call.answer(f"Linklar soni {len(temp[1][1])} ta")
    await call.message.answer("<b>Keyingi linkni yuboring : </b>")
    await state.set_state("link")
    
@dp.callback_query_handler(text="atmen", state="tasdiq")
async def qayta(call : types.CallbackQuery, state : FSMContext):
    await call.answer("<b>Bekor qilindi</b>", show_alert=True)
    await call.message.delete()
    await state.finish()
    
