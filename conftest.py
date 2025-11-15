import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--br", action="store", default="chrome", help="the name of the browser")


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = False
    opts.add_argument("--window-size=1920,1080")
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
