from aiogram import types


def make_keyboard(width: int, one_time: bool = False) -> types.ReplyKeyboardMarkup:
    """For getting aiogram reply keyboard markup"""
    return types.ReplyKeyboardMarkup(
        row_width=width, resize_keyboard=True, one_time_keyboard=one_time
    )


def make_button(title: str) -> types.KeyboardButton:
    """For getting aiogram keyboard button"""
    return types.KeyboardButton(title)
