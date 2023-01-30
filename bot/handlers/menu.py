from aiogram import types

from keyboard import make_asking_keyboard


async def menu(message: types.Message) -> None:
    """For getting the bot menu"""
    await message.answer("Что дальше?", reply_markup=make_asking_keyboard())
