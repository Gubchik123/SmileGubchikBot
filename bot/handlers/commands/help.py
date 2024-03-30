from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot_info import DP
from ..menu import menu


@DP.message_handler(CommandHelp())
async def command_help(message: types.Message) -> None:
    """The handler for the 'help' command for the general rules of using"""
    await message.answer(
        """
        Команды бота:
        /start - Начало работы с ботом
        /help - Отображение основных правил использования
        /goodbye - Завершение работы с ботом

        Советую использовать кнопки для задуманного результата

        Приятного использования!!!

        Контакты автора бота:
        CV site: https://hubariev.com
        LinkedIn: https://www.linkedin.com/in/nikita-hubariev
        Instagram: https://www.instagram.com/notwhale.1746

        Другие проекты автора доступны на:
        Project board: https://gubchik123-project-board.netlify.app
        GitHub: https://github.com/Gubchik123

        Другой бот автора: @WeatherGubchikBot
        """.replace("        ", "")
    )
    await menu(message)
