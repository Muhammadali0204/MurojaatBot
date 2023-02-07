from loader import dp, temp
from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.inline_keyboard import keyboard


@dp.message_handler(commands="create_video")
async def photo(msg : types.Message, state : FSMContext):
    await msg.answer('<b>Video yuboring : </b>')
    await state.set_state("video")
    
    
@dp.message_handler(state="video", content_types = types.ContentType.VIDEO)
async def photo_handler(msg : types.Message, state : FSMContext):
    temp[1] = ["", [], [], msg.video.file_id, msg.video.thumb.file_id]
    await msg.answer("<b>Matnini yuboring : </b>")
    await state.set_state("matn_video")
    
@dp.message_handler(state="matn_video")
async def matn(msg : types.Message, state : FSMContext):
    temp[1][0] = msg.html_text
    await msg.answer("<b>Matn qabul qilindi!</b>\n\n<b>Inline keybord uchun linklarni yuboring : </b>")
    await state.set_state("link_video")
    
@dp.message_handler(state='link_video') 
async def link(msg : types.Message, state : FSMContext):
    temp[1][1].append(msg.text)
    await msg.answer(f"<b>Endi esa <i>{msg.text}</i> uchun nom yuboring : </b>")
    await state.set_state("nom_video")
    
@dp.message_handler(state="nom_video")
async def nom(msg : types.Message, state : FSMContext):
    temp[1][2].append(msg.text)
    await msg.answer(temp[1][0], reply_markup=keyboard(temp[1][1], temp[1][2], True))
    await state.set_state("tasdiq_video")
    
@dp.callback_query_handler(state="tasdiq_video", text="ok")
async def tasdiq(call : types.CallbackQuery, state : FSMContext):
    await call.message.delete()
    print(call.message.chat.id)
    await call.message.answer_video(video=temp[1][3], thumb= temp[1][4],caption=temp[1][0],reply_markup=keyboard(temp[1][1], temp[1][2], False))
    await call.answer("Tuzildi✅")
    await state.finish()
    
@dp.callback_query_handler(text="davom", state="tasdiq_video")
async def qayta(call : types.CallbackQuery, state : FSMContext):
    await call.message.delete()
    await call.answer(f"Linklar soni {len(temp[1][1])} ta")
    await call.message.answer("<b>Keyingi linkni yuboring : </b>")
    await state.set_state("link_video")
    
@dp.callback_query_handler(text="atmen", state="tasdiq_video")
async def qayta(call : types.CallbackQuery, state : FSMContext):
    await call.answer("<b>Bekor qilindi</b>", show_alert=True)
    await call.message.delete()
    await state.finish()