import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://practice-automation.com/click-events/"


@pytest.mark.smoke
def test_simple_click_cat(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Cat']")
    element.click()
    assert driver.find_element(By.ID, "demo").text.strip() == "Meow!"


@pytest.mark.smoke
def test_js_click_dog(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Dog']")
    driver.execute_script("arguments[0].click();", element)
    assert driver.find_element(By.ID, "demo").text.strip() == "Woof!"


@pytest.mark.smoke
def test_mouse_click_pig(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Pig']")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    assert driver.find_element(By.ID, "demo").text.strip() == "Oink!"


@pytest.mark.smoke
def test_button_click_cow(driver):
    driver.get(url)
    button_click = driver.find_element(By.XPATH, "//button[normalize-space()='Cow']")
    button_click.send_keys(Keys.ENTER)
    assert driver.find_element(By.ID, "demo").text.strip() == "Moo!"
