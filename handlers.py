import requests
from aiogram import Router, html, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

main_commands = [
    'Menu',
    'lang',
    'Orders history',
    'Тех под'
]


# @router.message(CommandStart())
# async def start_handler(message: Message):
#     kb = ReplyKeyboardMarkup(keyboard=[
#         [KeyboardButton(text='Menu'), KeyboardButton(text='lang')],
#         [KeyboardButton(text='Orders history')],
#         [KeyboardButton(text='Тех под')],
#     ])
#
#     await message.answer(f'''
# Hello, {html.italic(message.from_user.username)}
# Id: {message.from_user.id}
# ''', reply_markup=kb)


@router.message(Command('do', 'work'))
async def do_handler(message: Message):
    await message.answer(message.text)


# @router.message(F.text == 'Menu')
# async def menu_handler(message: Message):
#     await message.answer("This is your menu: ")

@router.message(F.text.in_(main_commands))
async def main_commands_handler(message: Message):
    if message.text == 'Menu':
        await message.answer("This is your menu: ")
    elif message.text == 'lang':
        await message.answer("ru")
        await message.answer("en")
    else:
        await message.answer("Idi von")


@router.message(Command('users'))
async def message_handler(message: Message):
    data = requests.get('https://reqres.in/api/users?per_page=12').json()
    txt = ''
    for i in data['data']:
        txt += f"User {i['id']}:\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
    await message.answer(txt)


# limits_commands = ['2', '5', '6', '10', 'all']
limits_commands = ['limit_2', 'limit_5', 'limit_6', 'limit_10', 'all']


# @router.message(CommandStart())
# async def limits_kb_handler(message: Message):
#     kb = ReplyKeyboardMarkup(keyboard=[
#         [KeyboardButton(text='2'), KeyboardButton(text='5')],
#         [KeyboardButton(text='6'), KeyboardButton(text='10')],
#         [KeyboardButton(text='all')],
#     ])
#     await message.answer('Select a limit', reply_markup=kb)


@router.message(CommandStart())
async def limits_kb_handler(message: Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='limit_2'), KeyboardButton(text='limit_5')],
        [KeyboardButton(text='limit_6'), KeyboardButton(text='limit_10')],
        [KeyboardButton(text='all')],
    ])
    await message.answer('Select a limit', reply_markup=kb)


# @router.message(F.text.in_(limits_commands))
# async def limits_handler(message: Message):
#     if message.text == 'all':
#         limit = None
#     else:
#         limit = int(message.text)
#     if message.text == 'all':
#         data = requests.get('https://reqres.in/api/users?per_page=12').json()
#         txt = ''
#         for i in data['data']:
#             txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email \n\n
#         await message.answer(txt)
#     else:
#         data = requests.get(f'https://reqres.in/api/users?per_page={limit}').json()
#         txt = ''
#         for i in data['data']:
#             txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email \n\n
#         await message.answer(txt)


@router.message(F.text.in_(limits_commands))
async def limits_handler(message: Message):
    txt = ''
    if message.text == 'all':
        data = requests.get('https://reqres.in/api/users?per_page=12').json()
        for i in data['data']:
            txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    elif message.text == 'limit_2':
        data = requests.get('https://reqres.in/api/users?per_page=2').json()
        for i in data['data']:
            txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    elif message.text == 'limit_5':
        data = requests.get('https://reqres.in/api/users?per_page=5').json()
        for i in data['data']:
            txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    elif message.text == 'limit_6':
        data = requests.get('https://reqres.in/api/users?per_page=6').json()
        for i in data['data']:
            txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    elif message.text == 'limit_10':
        data = requests.get('https://reqres.in/api/users?per_page=10').json()
        for i in data['data']:
            txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    else:
        await message.answer('Limit not found')


@router.message(F.text.isdigit())
async def user_id_handler(message: Message):
    user_id = int(message.text)
    data = requests.get(f'https://reqres.in/api/users/{user_id}').json()
    txt = ''
    if 'data' in data:
        i = data['data']
        txt += f"User {i['id']}\nName: {i['first_name']}\nLast name: {i['last_name']}\nEmail: {i['email']}\n\n"
        await message.answer(txt)
    else:
        await message.answer("User not found")
