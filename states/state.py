from aiogram.dispatcher.filters.state import State, StatesGroup

class Admins(StatesGroup):
    mail = State()
    say = State()

class Users(StatesGroup):
    f_c =State()
    s_c =State()
    value =State()
