from random import choice, randint

from bs4 import BeautifulSoup

from ._general import get_soup_by_


def get_joke_text() -> str:
    """For getting joke text from random url"""
    soup = get_soup_by_(
        f"https://anekdotov.net/anekdot/index-page-{randint(1, 24)}.html"
    )
    return _get_rand_joke_text_by_(soup)


def _get_rand_joke_text_by_(soup: BeautifulSoup) -> str:
    """For getting random joke on the page"""
    all_jokes = soup.find_all("div", class_="anekdot")
    rand_joke: BeautifulSoup = choice(all_jokes)
    return rand_joke.text
