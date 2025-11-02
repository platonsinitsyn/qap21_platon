import time

import pytest
from selenium.webdriver.common.by import By

url = "https://practice-automation.com/iframes/"


@pytest.mark.smoke
def test_iframe(driver):
    driver.get("https://practice-automation.com/iframes/")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    element = driver.find_element(By.CSS_SELECTOR, "a.getStarted_Sjon")
    element.click()
    time.sleep(1)
    title = driver.find_element(By.CSS_SELECTOR, ".theme-doc-markdown.markdown h1")
    assert title.text.strip() == "Installation"
