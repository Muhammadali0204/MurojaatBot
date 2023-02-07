from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard(links, nomlar, a):
    inline_keyboard = InlineKeyboardMarkup(
        row_width=1
    )
    for i in range(0, len(links)):
        inline_keyboard.insert(InlineKeyboardButton(text=nomlar[i], url=links[i]))
    
    
    if a:
        inline_keyboard.insert(InlineKeyboardButton(text="➡️", callback_data="davom"))
        inline_keyboard.insert(InlineKeyboardButton(text="❌", callback_data="atmen"))
        inline_keyboard.insert(InlineKeyboardButton(text="✅", callback_data="ok"))
        
    return inline_keyboard