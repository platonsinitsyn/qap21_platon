import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://practice-automation.com/click-events/"

# @pytest.mark.smoke
# def test_simple_click_cat(driver):
#     driver.get(url)
#     element = driver.find_element(By.XPATH, "//button[normalize-space()='Cat']")
#     element.click()
#     assert driver.find_element(By.ID, "demo").text.strip() == "Meow!"
#
#
# @pytest.mark.smoke
# def test_js_click_dog(driver):
#     driver.get(url)
#     element = driver.find_element(By.XPATH, "//button[normalize-space()='Dog']")
#     driver.execute_script("arguments[0].click();", element)
#     assert driver.find_element(By.ID, "demo").text.strip() == "Woof!"
#
#
# @pytest.mark.smoke
# def test_mouse_click_pig(driver):
#     driver.get(url)
#     element = driver.find_element(By.XPATH, "//button[normalize-space()='Pig']")
#     actions = ActionChains(driver)
#     actions.move_to_element(element).click().perform()
#     assert driver.find_element(By.ID, "demo").text.strip() == "Oink!"
#
#
# @pytest.mark.smoke
# def test_button_click_cow(driver):
#     driver.get(url)
#     button_click = driver.find_element(By.XPATH, "//button[normalize-space()='Cow']")
#     button_click.send_keys(Keys.ENTER)
#     assert driver.find_element(By.ID, "demo").text.strip() == "Moo!"


# -------- Pre-con: --------
def open_site(driver, url=URL):
    driver.get(url)


def wait(seconds=1):
    time.sleep(seconds)


def find_button(driver, text):
    return driver.find_element(By.XPATH, f"//button[normalize-space()='{text}']")


def click(driver, by, selector):
    driver.find_element(by, selector).click()


def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)


def mouse_click(driver, element):
    ActionChains(driver).move_to_element(element).click().perform()


def key_click_enter(element):
    element.send_keys(Keys.ENTER)


def assert_demo_text(driver, expected):
    actual = driver.find_element(By.ID, "demo").text.strip()
    assert actual == expected


# -------- tests --------
@pytest.mark.smoke
def test_simple_click_cat(driver):
    open_site(driver)
    click(driver, By.XPATH, "//button[normalize-space()='Cat']")
    wait(1)
    assert_demo_text(driver, "Meow!")


@pytest.mark.smoke
def test_js_click_dog(driver):
    open_site(driver)
    btn = find_button(driver, "Dog")
    js_click(driver, btn)
    wait(1)
    assert_demo_text(driver, "Woof!")


@pytest.mark.smoke
def test_mouse_click_pig(driver):
    open_site(driver)
    btn = find_button(driver, "Pig")
    mouse_click(driver, btn)
    wait(1)
    assert_demo_text(driver, "Oink!")


@pytest.mark.smoke
def test_keyboard_click_cow(driver):
    open_site(driver)
    btn = find_button(driver, "Cow")
    key_click_enter(btn)
    wait(1)
    assert_demo_text(driver, "Moo!")
