import logging

from aiogram import executor

import handlers
from bot_info import DP


if __name__ == "__main__":
    logging.basicConfig(
        format="%(name)s: [%(filename)s - %(lineno)d] #%(levelname)-8s (%(asctime)s) %(message)s",
        level=logging.INFO,
    )
    executor.start_polling(DP)
