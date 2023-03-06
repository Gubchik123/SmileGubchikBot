import logging

from aiogram.utils.exceptions import TelegramAPIError

import handlers
from bot_info import DP


if __name__ == "__main__":
    logging.basicConfig(
        format="%(name)s: [%(filename)s - %(lineno)d] #%(levelname)-8s (%(asctime)s) %(message)s",
        level=logging.INFO,
    )
    
    try:
        DP.start_polling()
    except TelegramAPIError as e:
        pass
