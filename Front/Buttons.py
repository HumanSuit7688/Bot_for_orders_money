from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_cust = InlineKeyboardButton('Заказчик', callback_data='button_customer_sign')
inline_btn_cont = InlineKeyboardButton('Подрядчик', callback_data='button_contractor_sign')
inline_kb_roles = InlineKeyboardMarkup().add(inline_btn_cust).add(inline_btn_cont)

