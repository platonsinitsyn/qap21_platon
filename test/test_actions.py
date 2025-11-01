import pytest
from selenium.webdriver.common.by import By

url = "https://practice-automation.com/click-events/"


@pytest.mark.smoke
def test_form(driver):
    driver.get(url)
    element = driver.find_elements(By.ID, "Cat")
    element.click()
