import logging

from aiogram import types
from aiogram.dispatcher.filters import Text

from bot_info import DP

from .menu import menu
from .parsing import get_joke_text, get_mem_image


logger = logging.getLogger()


@DP.message_handler(Text("Анекдот", ignore_case=True))
async def joke_handler(message: types.Message) -> None:
    """The handler for sending a joke"""
    try:
        await _send_searching_message(message)
        await message.answer(get_joke_text())
    except Exception as e:
        await _send_error_message(message)
        logger.error(f"Exception in joke handler: {str(e)}")
    await menu(message)


@DP.message_handler(Text("Мемчик", ignore_case=True))
async def mem_handler(message: types.Message) -> None:
    """The handler for sending a mem image"""
    try:
        await _send_searching_message(message)
        await message.answer_photo(get_mem_image())
    except Exception as e:
        await _send_error_message(message)
        logger.error(f"Exception in mem handler: {str(e)}")
    await menu(message)


async def _send_searching_message(message: types.Message) -> None:
    """For sending to user the searching message"""
    await message.answer("Поиск...")


async def _send_error_message(message: types.Message) -> None:
    """For sending to user the error message"""
    await message.answer("Упс, возникла ошибка, повторите попытку :)")
