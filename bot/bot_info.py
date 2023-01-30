from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN


BOT = Bot(BOT_TOKEN)
DP = Dispatcher(BOT, storage=MemoryStorage())
