from aiogram import types
from aiogram.dispatcher.filters import Text

from bot_info import DP
from keyboard import make_keyboard, make_button


@DP.message_handler(commands="goodbye")
@DP.message_handler(Text(equals="Закончить веселье", ignore_case=True))
async def command_goodbye(message: types.Message) -> None:
    """The handler for the 'goodbye' command"""
    markup = make_keyboard(width=1)
    markup.add(make_button("/start"))

    await message.answer_sticker(
        "CAACAgIAAxkBAAM2Y9f-XkmJ9621NUhr2ZvdTqvqwn0AAnYAAycUSQt2HTA3ZpGg6S0E"
    )
    await message.answer(
        f"Пока, {message.from_user.first_name}, возвращайся еще\
        \nВ следующий раз просто введи или нажми /start :)",
        reply_markup=markup,
    )
