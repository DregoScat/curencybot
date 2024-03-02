from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp , db, bot
from utils.db_api.postgres import Database
from classes.classes import sus as SUS
from config import data
###
# from keyboards.default import kyboard1
from states.state import Admins
import random
from bs4 import BeautifulSoup
import requests
from aiogram.dispatcher.filters.builtin import CommandStart



@dp.message_handler(commands=["mail"])
async def mailing_check(message: types.Message):
    sus = SUS()

    if not sus.check_if_admin(data.ADMINS, message.from_user.id):
        await bot.send_message(message.from_user.id, "You're not admin!")
    else:
        await message.answer("Write your mail to all users, using this bot")
        await Admins.mail.set()

@dp.message_handler(state=Admins.mail.state)
async def mailing(message: types.Message, state: FSMContext):

    users = await db.get_users()
    await bot.send_message(message.from_user.id, "Here's how it's looking like:")
    for i in users:
        await bot.send_message(i['user_id'], message.text)
    await state.reset_state(with_data=True)


@dp.message_handler(commands=["phone_book"])
async def tel_book(message: types.Message):
    a = await db.get_tel_book()
    await message.answer("""Here is a phone book:
            Name, - phone""")
    for i in a:
        await message.answer(f"{i['user_name']}, - {i['user_id']}")

@dp.message_handler()
async def saying_check(message: types.Message):
    c = str(message.text).split(" ")
    a = str(message.text).split(" ")



    try:
        print(c[0])
        print(c[1])
        print(c[2])

    except:
        pass

    if c[0] == "/say":
        a.pop(0)
        print(a)
        a.pop(0)
        print(a)
        a = " ".join(a)
        print(a)
        sus = SUS()

        if not sus.check_if_admin(data.ADMINS, message.from_user.id):
            await bot.send_message(message.from_user.id, "You're not admin!")
        else:



            await bot.send_message(c[1], a)
            await bot.send_message(message.from_user.id, f"""Here's how it's looking like
{a}""")



