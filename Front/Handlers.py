from aiogram import Dispatcher, types
from Front.Buttons import  inline_kb_roles

async def start(msg: types.Message):
    await msg.answer('Привет, Я бот который поможет тебе заработать деньги на легких заданиях, а также продвинуть свои задания за оплату.\nВся инфа тут - /info')

async def info(msg: types.Message):
    await msg.answer('Много всякого')

async def help(msg: types.Message):
    await msg.answer('Если у вас возникла проблема или вопрос пишите адмиимтраторам.')

async def sign_up(msg: types.Message):
    await msg.answer('Привет, Кто ты заказчик или Подрядчик?', reply_markup=inline_kb_roles)



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(sign_up, commands='sign_up')
    dp.register_message_handler(start, commands= 'start')