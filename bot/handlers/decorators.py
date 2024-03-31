import logging
from typing import Callable

from aiogram.types import Message

from .menu import menu


def process_searching(action: str) -> Callable:
    def wrapper(handler: Callable) -> None:
        async def decorator(message: Message) -> None:
            try:
                search_message = await message.answer("Поиск...")

                await handler(message)

                await search_message.delete()
            except Exception as e:
                await message.answer(
                    "Упс, возникла ошибка, повторите попытку :)"
                )
                logging.error(f"Exception in {action} handler: {str(e)}")
            await menu(message)

        return decorator

    return wrapper
