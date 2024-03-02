from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("tab1", "For users"),
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("help", "Recive a help"),
            types.BotCommand("chart","Recive a chart of 5 most"),
            types.BotCommand("convert","Recive a chart of 5 most"),
            types.BotCommand("tab2", "For ADMINS"),
            types.BotCommand("mail", "Mail Information to all the users"),
            types.BotCommand("phone_book", "Recive a phone book"),
            types.BotCommand("say","Mail Information to users, /say id Message"),



        ]
    )
