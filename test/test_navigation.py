import time

import pytest
from selenium.webdriver.common.by import By

url = "https://practice-automation.com/form-fields/"


@pytest.mark.smoke
def test_navigation(driver):
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[href='https://linktr.ee/automateNow']").click()
    window_handles = driver.window_handles
    assert len(window_handles) == 2

    driver.switch_to.window(window_handles[1])
    current_url = driver.current_url
    assert current_url != url


@pytest.mark.smoke
def test_back_forward_button(driver):
    driver.get(url)
    driver.find_element(By.LINK_TEXT, "Home").click()
    current_url = driver.current_url
    assert url != current_url
    driver.back()
    assert url == driver.current_url
    assert current_url != driver.current_url
    driver.forward()
    assert url != driver.current_url
