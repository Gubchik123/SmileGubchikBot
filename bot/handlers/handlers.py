from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from bot_info import DP

from .decorators import process_searching
from .parsing import get_joke_text, get_mem_image


@DP.message_handler(Text("Анекдот", ignore_case=True))
@process_searching("joke")
async def joke_handler(message: Message) -> None:
    """The handler for sending a joke"""
    await message.answer(get_joke_text())


@DP.message_handler(Text("Мемчик", ignore_case=True))
@process_searching("mem")
async def mem_handler(message: Message) -> None:
    """The handler for sending a mem image"""
    await message.answer_photo(get_mem_image())
