import logging

from aiogram import executor
from aiogram.utils.exceptions import TelegramAPIError

import handlers
from bot_info import DP


if __name__ == "__main__":
    logging.basicConfig(
        format="%(name)s: [%(filename)s - %(lineno)d] #%(levelname)-8s (%(asctime)s) %(message)s",
        level=logging.INFO,
    )

    try:
        executor.start_polling(DP)
    except TelegramAPIError:
        pass
