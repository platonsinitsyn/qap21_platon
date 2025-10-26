import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")  # включить и выключить окно браузера
    opts.add_argument("--window-size=640,900")  # размер окна
    driver = webdriver.Chrome(options=opts)  #
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_pytest(driver):
    url = "https://docs.pytest.org/en/stable/"
    driver.get(url)
    assert driver.title == "pytest documentation"
    assert driver.current_url == url


def test_python_web(driver):
    url = "https://www.python.org/"
    driver.get(url)
    assert driver.title == "Welcome to Python.org"
    assert driver.current_url == url
