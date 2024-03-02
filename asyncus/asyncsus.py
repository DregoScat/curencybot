from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from utils.db_api.postgres import Database
from classes.classes import sus as SUS
from config import data
###
# from keyboards.default import kyboard1
from states.state import *
import random
from bs4 import BeautifulSoup
import requests
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import time
import datetime

#~Imports~
#~start~
@dp.message_handler(commands=["start"])
async def start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await db.new_user(message.from_user.id, message.from_user.full_name)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(text="/convert"), KeyboardButton(text="/help")]
    keyboard.add(*buttons)
    await message.answer("Welcome to the ImposterLoL bot. Please choose a action below.\n If you don't understand something use '/Help'.\nThis bot is on the stage of the coding, so there could be errors.", reply_markup=keyboard)


#~Help~
@dp.message_handler(commands=["help"])
async def help(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # buttons = [KeyboardButton(text="/convert"), KeyboardButton(text="/chart"), KeyboardButton(text="/cancel")]
    # keyboard.add(*buttons)
    await message.answer(f"This bot is on the stage of the coding, so there could be errors.\nIn this bot you can use many functions. Main function is the function that convert currencies - /convert.")
    time.sleep(1)
    await message.answer(f"To create a chart of currencies, please use a command '/chart main_currency currencies'.")
    time.sleep(1)
    await message.answer(f"Main currency means the currency to which everything will be compared, and currencies means you can write from 1 to {len(cur)} of currencies we have.")
    time.sleep(1)
    await message.answer(f"Example - '/chart usd Eur Chf'.")
    time.sleep(1)
    await message.answer(f"Use /chart main_currency all', to create a chart of all currencies.")
    time.sleep(1)
    await message.answer(f"Example: '/chart Eur all'")
    time.sleep(1)
    await message.answer(f"Here's a list of currencies:")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons = [KeyboardButton(text="/help")]
    keyboard.add(*buttons)
    time.sleep(1)
    await message.answer(f"'Usd' = Dollar, 'Eur' = Euro, 'Pln' = zloty, 'Gbp' = Pound, 'Chf' = Swiss franc , 'Uah' = Ukrainian hryvnia'\nFor /chart, Uah is not working", reply_markup=keyboard)




    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#~Currencies and chart~
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import requests
from pycoingecko import CoinGeckoAPI
import pandas as pd
import io
#https://minfin.com.ua/ua/currency/

# cg = CoinGeckoAPI()
# ohlc = cg.get_coin_ohlc_by_id(id = "ethereum", vs_currency = "usd", days = "30")
# df = pd.DataFrame(ohlc)
# df.columns = ["date", "open", "high", "low", "close"]
# df["date"] = pd.to_datetime(df["date"], unit = "ms")
# df.set_index('date', inplace = True)
# print(df)

cur = ['USD', 'EUR', 'PLN', 'GBP', 'CHF', 'UAH']

first_cur = str()
second_cur = str()
value = str()




@dp.message_handler(commands=['convert'])
async def convert0(message:types.Message, state: FSMContext):
    await state.reset_state(with_data=True)

    await message.answer("I remind you: \n'Usd' = Dollar, 'Eur' = Euro, 'Pln' = zloty, 'Gbp' = Pound, 'Chf' = Swiss franc , 'Uah' = Ukrainian hryvnia'\nFor /chart, Uah is not working")
    time.sleep(0.5)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(text="Usd"), KeyboardButton(text="Eur"), KeyboardButton(text="Pln"), KeyboardButton(text="Gbp"), KeyboardButton(text="Chf"), KeyboardButton(text="Uah"), ]
    keyboard.add(*buttons)
    await message.answer("Choose first currency, it is a currency from what you want to convert.", reply_markup=keyboard)
    await Users.f_c.set()


@dp.message_handler(state=Users.f_c.state)
async def convert(message:types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(text="Usd"), KeyboardButton(text="Eur"), KeyboardButton(text="Pln"), KeyboardButton(text="Gbp"), KeyboardButton(text="Chf"), KeyboardButton(text="Uah"), ]
    keyboard.add(*buttons)
    global first_cur
    first_cur = message.text

    await message.answer("Choose second currency, it is a currency to what you want to convert.", reply_markup=keyboard)
    await Users.s_c.set()

@dp.message_handler(state=Users.s_c.state)
async def convert1(message:types.Message):
    global second_cur
    second_cur = message.text

    await message.answer("Choose value(s), it is a value(s) of currency that you want to convert. ValueS you must write through a space.")
    await Users.value.set()



@dp.message_handler(state=Users.value.state)
async def convert2(message:types.Message, state: FSMContext):
    global value

    value = message.text.strip().split(" ")
    converted_value = list()
    for i in range(len(value)):
        sus = 1
        print(i)
        print(f"https://minfin.com.ua/currency/converter/{value[i-1]}-{first_cur}-to-{second_cur}")
        r = requests.get(f"https://minfin.com.ua/currency/converter/{value[i-1]}-{first_cur}-to-{second_cur}")
        print(r)
        soup = BeautifulSoup(r.content, "html.parser")
        # print(soup)
        print(soup.select(".DFlfde SwHCTb"))
        # j = soup.select_one(f"div > div > div > div > div > span")
        for j in soup.find_all('input', class_='zlkj5-1 cNCStF'):
            if sus == 2:
                print(j)
                print("---------------------------------------------")



                j = str(j.get("value"))
                print(j)
                j = j.replace("\xa0", "")
                print(j)
                j = j.replace(" ", "")
                print(j)
                j = "".join(j.split(" "))
                print(j)
                j = float(j)
                converted_value.append(j)
                print(j)
                print("good")


            sus+=1
        print(converted_value)
    print("TEST")
    print(value)
    print(converted_value)
    df = pd.DataFrame(
        {
            first_cur: value,
            second_cur: converted_value
        }
    )
    print(df)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    buttons = [KeyboardButton(text="/help")]
    keyboard.add(*buttons)
    await message.answer(f"Here's your converted value(s):\n{df.to_string(index=False)}", reply_markup=keyboard)
    await state.reset_state()












# import random
# import time
#
# symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
#
#
# while True:
#     stringus = "https://discord.gg/"
#     code = ""
#     for i in range(8):
#         a = random.choice(symbols)
#         code = code + a
#
#     print(stringus+code)
#     time.sleep(3)


# Replace 'YOUR_API_KEY' with your actual API key from Alpha Vantage
# API_KEY = 'YOUR_API_KEY'
# #{CURRENCY_SYMBOL}&to_currency={c[1].lower()}&apikey={API_KEY}
# # Function to get historical currency exchange rates
# def get_currency_exchange_rates(base_currency, target_currency, api_key):
#     # Calculate dates for one month period
#     end_date = datetime.datetime.now().strftime('%Y-%m-%d')
#     start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
#
#     # Construct the API request URL
#     url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={base_currency}&to_symbol={target_currency}&apikey={api_key}&outputsize=full&datatype=json'
#
#     # Make the API request
#     response = requests.get(url)
#     data = response.json()
#
#     # Extract exchange rates from the response
#     exchange_rates = {}
#     for date, info in data['Time Series FX (Daily)'].items():
#         if date >= start_date and date <= end_date:
#             exchange_rates[date] = float(info['4. close'])
#
#     return exchange_rates
#
# # Example usage
# base_currency = 'USD'  # Base currency
# target_currency = 'EUR'  # Target currency
# exchange_rates = get_currency_exchange_rates(base_currency, target_currency, API_KEY)
#
# # Print exchange rates
# for date, rate in exchange_rates.items():
#     print(f'{date}: {rate}')




# index = 0
# cg = CoinGeckoAPI()
# for i in cur:
#     parameters = {
#         'vs_currency': i[index].lower(),
#         'order': 'market_cap_desc',
#         'per_page': 100,
#         'page': 1,
#         'sparkline': False,
#         'locale': 'en'
#     }
#     coin_market_data = cg.get_coins_markets(**parameters)
#     print(coin_market_data)
#     index += 1

# @dp.message_handler(commands=["chart"])
# async def currency_chart():
#     pass

@dp.message_handler()
async def currency_chart(message:types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    c = str(message.text).strip().split(" ")
    a = str(message.text).strip().split(" ")
    b = str(message.text).strip()
    u = list()

    date = datetime.datetime.now()
    print(date)

    date = str(date).split("-")



    day = str(date[2]).split(" ")
    day = day[0]
    print(date)
    print(day)

    days31 = ["01", "03", "05", "07", "09", "11"]
    days30 = ["04", "06", "08", "10", "12"]
    days29 = ["02"]

    if date[1] in days30:
        month = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        print(month)
    elif date[1] in days31:
        month = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
        print(month)
    elif date[1] in days29:
        month = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28, 29]
        print(month)

    print(month)
    y = list()
    y2 = list()
    y3 = list()
    y4 = list()
    y5 = list()
    y6 = list()




    # try:
    #     print(c[0])
    #     print(c[1])
    #     print(c[2])
    #
    # except:
    #     pass

    if c[0] == "/chart":
        for i in range(len(c)-1):
            i += 1
            # print(len(c))
            # print(c[i])
            if c[i].upper() in cur:
                idk = True
                print("Yes")
                u.append(c[i])
            else:
                idk = False
                print("NOOOOOO")
                break
        print(u)


        if idk == True:
            print(a)
            a.pop(0)
            print(a)
            a.pop(0)
            print(a)
            # a = " ".join(a)
            # print(a)

            for i in range(len(c)-2):



                j = i
                i += 2

                # cg = CoinGeckoAPI()
                # test = cg.get_coins_list()
                #
                # parameters = {
                #     'vs_currency' : c[i].lower(),
                #     'order': 'market_cap_desc',
                #     'per_page': 100,
                #     'page': 1,
                #     'sparkline': False,
                #     'locale': 'en'
                # }
                # coin_market_data = cg.get_coins_markets(**parameters)
                # print(coin_market_data)


                API_KEY = '5WSVNLW4V0DVMA2K'


                CURRENCY_SYMBOL = c[i].lower()


                end_date = datetime.datetime.now().strftime('%Y-%m-%d')
                start_date = (datetime.datetime.now() - datetime.timedelta(days=len(month))).strftime('%Y-%m-%d')

                # Construct the API request URL
                url = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={CURRENCY_SYMBOL}&to_symbol={c[1].lower()}&outputsize=full&apikey={API_KEY}'
                # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo'


                # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
                # url1 = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&interval=5min&apikey={API_KEY}'

                #--------------------
                # r = requests.get(url)
                # data = r.json()
                #
                # print(data)
                #
                # # Make the API request
                # response = requests.get(url)
                # data = response.json()
                #
                # # Extract exchange rates from the response
                # exchange_rates = {}
                # print(data)
                # for date, info in data['Time Series FX (Monthly)'].items():
                #     if date >= start_date and date <= end_date:
                #         exchange_rates[date] = float(info['4. close'])
                #
                # print(exchange_rates)
                # # print(f'Текущий курс {CURRENCY_SYMBOL}: {exchange_rate}')
                # print(c[i])
                #
                # for date, rate in exchange_rates.items():
                #     print(f'{date}: {rate}')
                #---------
                from datetime import timedelta
                date = str(datetime.datetime.now()).split("-")
                print(date)
                aaa = date[2].split(" ")
                date.pop(2)
                date.append(aaa[0])
                print(date)
                date_from = list()
                for i in range(31, 1, -1):
                    print(i)
                    dt = datetime.datetime.now()-timedelta(days=i)
                    date_from.append(dt.strftime("%Y-%m-%d"))
                print(date_from)
                # aaa = date_from[2].split(" ")
                # date_from.pop(2)
                # date_from.append(aaa[0])
                # date_from = "-".join(date_from)
                print(f"date_from: {date_from}")

                # date_to = "-".join(date)

                #url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/month/{date_from}/{date_to}?adjusted=true&sort=asc&limit=120&apiKey=PIUOuUMmX5FCzS4c6j6i3ecltMomxoCR"

                url = f"https://api.frankfurter.app/{date_from[0]}..{date_from[len(date_from)-1]}?base={c[1]}"
                print(url)
                r = requests.get(url)
                print(r)
                data = r.json()
                print(data)
                for j in range(len(c)-2):
                    for i in range(len(date_from)):
                        try:
                            rate = data['rates'][date_from[i]][c[j+2].upper()]
                            print("good")

                            #         if j == 0:
                            if j == 0:
                                y.append(rate)
                                print("x: " + str(rate))
                            if j == 1:
                                y2.append(rate)
                                print("y: " + str(rate))
                            if j == 2:
                                y3.append(rate)
                                print("z: " + str(rate))
                            if j == 3:
                                y4.append(rate)
                                print("o: " + str(rate))
                            if j == 4:
                                y5.append(rate)
                                print("p: " + str(rate))
                            if j == 5:
                                y6.append(rate)
                                print("r: " + str(rate))

                        except:
                            print("excepted")

                # for j in range(len(c)):
                #     for i in range(len(date_from)):
                #
                #         print("c : ", c)
                #         url = f"https://api.frankfurter.app/{date_from[i-1]}?amount=1&from={c[i+2]}&to={c[1]}"
                #         print(url)
                #         r = requests.get(url)
                #         print(r)
                #         data = r.json()
                #         print(data)
                #
                #         rate = data['']
                #
                #






                # ohlc = cg.get_coin_ohlc_by_id(id = c[1].lower(), vs_currency = c[i].lower(), days = "30")
                # df = pd.DataFrame(ohlc)
                # df.columns = ["date", "open", "high", "low", "close"]
                # df["date"] = pd.to_datetime(df["date"], unit = "ms")
                # df.set_index('date', inplace = True)
                # print(df)

                # r = requests.get(f"https://www.google.com/finance/quote/{c[1]}-{c[i]}?sa=X&ved=2ahUKEwisz5yD2sOEAxVTSvEDHQ4yBgAQmY0JegQIBxAv&window=1M")
                # soup = BeautifulSoup(r.content, "html.parser")





            try:
                print("lol ",  len(y))
                plt.plot([i for i in range(1, len(y)+1)], y)
                plt.text("Month", "Main currecy")
            except:
                pass
            try:
                plt.plot([i for i in range(1, len(y2)+1)], y2)
                plt.text("Month", "Main currecy")
            except:
                pass
            try:
                plt.plot([i for i in range(1, len(y3)+1)], y3)
                plt.text("Month", "Main currecy")
            except:
                pass
            try:
                plt.plot([i for i in range(1, len(y4)+1)], y4)
                plt.text("Month", "Main currecy")
            except:
                pass
            try:
                plt.plot([i for i in range(1, len(y5)+1)], y5)
                plt.text("Month", "Main currecy")
            except:
                pass
            try:
                plt.plot([i for i in range(1, len(y6)+1)], y6)
                plt.text("Month", "Main currecy")
            except:
                pass

            save = io.BytesIO()
            plt.xlabel("Day")
            plt.ylabel(f"Main Currency - {c[1].lower()}")
            plt.savefig(save, format = 'png')
            save.seek(0)
            await message.answer_photo(save)

