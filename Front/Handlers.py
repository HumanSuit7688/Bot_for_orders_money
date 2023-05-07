from aiogram import Dispatcher, types
from Front.Buttons import  inline_kb_roles, inline_kb_add_orders
from backend.work_db import User

async def start(msg: types.Message):
    await msg.answer('Привет, Я бот который поможет тебе заработать деньги на легких заданиях, а также продвинуть свои задания за оплату.\nВся инфа тут - /info')

async def info(msg: types.Message):
    await msg.answer('Этот бот помогает заработать деньги выполняя различные легкие задания или продвинуть свои задания, заплатив за их выполнение. '
                     'Чтобы всё работало нужно зарегистрироваться (/sign_up) и выбрать роль, заказчик или подрядчик.'
                     '')
async def help(msg: types.Message):
    await msg.answer('Если у вас возникла проблема или вопрос пишите администраторам.')

async def sign_up(msg: types.Message):
    await msg.answer('Привет, Кто ты заказчик или Подрядчик?', reply_markup=inline_kb_roles)


async def sign_customer(callback_query: types.CallbackQuery):
    id = callback_query.from_user.id
    user_name = callback_query.from_user.username
    user = User(id)
    check = user.check_log()
    if check == True:
        print('уже занято')
        await callback_query.answer('Уже есть такой акккаунт')
    else:
        print('все ок')
        user.sign_up(user_name, 'Z')
        await callback_query.answer('Авторизация прошла успешно!')


async def sign_contractor(callback_query: types.CallbackQuery):
    id = callback_query.from_user.id
    user_name = callback_query.from_user.username
    user = User(id)
    check = user.check_log()
    if check == True:
        print('уже занято')
        await callback_query.answer('Уже есть такой акккаунт')
    else:
        print('все ок')
        user.sign_up(user_name, 'P')
        await callback_query.answer('Авторизация прошла успешно!')

async def add_order(msg: types.Message):
    tele_id = msg.chat.id
    user = User(tele_id)
    role = user.return_role()
    if role == 'Z' or role == 'A':
        await msg.answer('Хотите добавить задание, выбирайте категорию:', reply_markup=inline_kb_add_orders)
    else:
        await msg.answer('Отказ в доступе')




def register_handlers(dp: Dispatcher):

    dp.register_message_handler(sign_up, commands='sign_up')
    dp.register_message_handler(start, commands= 'start')
    dp.register_callback_query_handler(sign_customer, lambda c: c.data == 'button_customer_sign')
    dp.register_callback_query_handler(sign_contractor, lambda c: c.data == 'button_contractor_sign')
    dp.register_message_handler(add_order, commands='add_order')