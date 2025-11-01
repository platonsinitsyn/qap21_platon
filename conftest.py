import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = True
    opts.add_argument("--window-size=640,900")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
