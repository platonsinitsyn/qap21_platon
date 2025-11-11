# import pytest
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from files import IMG_1

# from selenium.webdriver.common.keys import Keys


URL = "https://learn.javascript.ru/task/simple-page"


def test_alert_click(driver):
    element = driver.find_element(By.CSS_SELECTOR, 'a[onclick="event.preventDefault(); runDemo(this)"]')
    element.click()
    alert = driver.switch_to.alert
    alert.send_keys("Platon")
    alert.accept()
    assert alert.text == "Platon"
    alert.accept()


URL = "http://the-internet.herokuapp.com/windows"


def test_window_handle(driver):
    driver.get(URL)
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    text = driver.find_element(By.TAG_NAME, "h3").text
    assert text == "New Window"


URL = "/"


def test_file_upload(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    driver.send_keys(str(IMG_1))
