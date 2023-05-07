from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_cust = InlineKeyboardButton('Заказчик', callback_data='button_customer_sign')
inline_btn_cont = InlineKeyboardButton('Подрядчик', callback_data='button_contractor_sign')
inline_kb_roles = InlineKeyboardMarkup().add(inline_btn_cust).add(inline_btn_cont)

inline_btn_add_order_views = InlineKeyboardButton('Просмотры', callback_data='button_add_order_views')
inline_btn_add_order_subs = InlineKeyboardButton('Подписки', callback_data='button_add_order_subs')
inline_btn_add_order_bots = InlineKeyboardButton('Боты', callback_data='button_add_order_bots')
inline_btn_add_order_groups = InlineKeyboardButton('Группы', callback_data='button_add_order_groups')
inline_btn_add_order_exten = InlineKeyboardButton('Расширенные', callback_data='button_add_order_exten')
inline_kb_add_orders = InlineKeyboardMarkup().row(inline_btn_add_order_views, inline_btn_add_order_subs).row(inline_btn_add_order_bots, inline_btn_add_order_groups).add(inline_btn_add_order_exten)



