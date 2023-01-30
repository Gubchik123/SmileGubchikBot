from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot_info import DP
from ..menu import menu


@DP.message_handler(CommandStart())
async def command_start(message: types.Message) -> None:
    """For sending the greeting message after 'start' command"""
    await message.answer_sticker(
        "CAACAgIAAxkBAAIB72PYDxSG8qFpelSN8wNyAsdnTXqzAAJjAAMnFEkLmmtkjto32lstBA"
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}\nДавай повеселимся!!!"
    )
    await menu(message)
