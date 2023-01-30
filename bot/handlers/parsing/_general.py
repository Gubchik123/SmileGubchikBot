import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def _get_request_by_(url: str) -> requests.Response:
    """For getting request GET Response"""
    return requests.get(
        url, headers={"user-agent": UserAgent().random.strip()}
    )


def get_soup_by_(url: str) -> BeautifulSoup:
    """For getting BeautifulSoup object by url"""
    return BeautifulSoup(_get_request_by_(url).text, "lxml")
