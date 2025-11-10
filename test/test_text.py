import pytest
from selenium.webdriver.common.by import By

url = "https://practice-automation.com/form-fields/"


@pytest.mark.smoke
def test_enter_and_clear_text(driver):
    driver.get(url)
    element = driver.find_element(By.ID, "name-input")
    element.send_keys("Platon")
    assert element.get_attribute("value") == "Platon"
    element.clear()
    assert element.get_attribute("value") == ""
