from random import choice, randint

from bs4 import BeautifulSoup

from ._general import get_soup_by_, _get_request_by_


def get_mem_image() -> str:
    """For getting mem image from random url"""
    soup = get_soup_by_(f"https://pikabu.ru/tag/Мемы?page={randint(1, 125)}")
    return _get_rand_mem_image_by_(soup)


def _get_rand_mem_image_by_(soup: BeautifulSoup) -> str:
    """For getting random link on the page"""
    all_links = soup.find_all("img", class_="story-image__image")
    rand_img: BeautifulSoup = choice(all_links)
    return _get_image_from_(_get_src_from_(rand_img))


def _get_src_from_(img: BeautifulSoup) -> str:
    """For getting image url from 'img' html tag"""
    src = img.get("data-src")
    if not src:
        src = img.get("data-large-image")
    return src


def _get_image_from_(url: str) -> bytes:
    """For getting image content"""
    response = _get_request_by_(url)
    return response.content
