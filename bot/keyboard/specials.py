from aiogram import types
from .default import make_keyboard, make_button


def make_asking_keyboard() -> types.ReplyKeyboardMarkup:
    """For getting asking keyboard"""
    markup = make_keyboard(width=2)
    markup.add(make_button("Анекдот"), make_button("Мемчик"))
    return markup
