import random

import pytest

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def lst():
    lst_temp = []
    for i in range(9):
        lst_temp.append(random.randint(0, 10))
    return lst_temp


def test_1(lst):
    assert lst


def test_2(lst):
    assert lst
