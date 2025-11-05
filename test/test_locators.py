import pytest
from selenium.webdriver.common.by import By

# url = "https://letcode.in/test"
url = "https://www.wildberries.by/"


@pytest.mark.smoke
def test_locators(driver):
    driver.get(url)

    # 1 - By.NAME
    el = driver.find_elements(By.NAME, "banner_cb306469-2db8-47e7-af99-e3954463b0ea")
    print(el)

    # 2 - By.ID
    el = driver.find_elements(By.ID, "searchInput")
    print(el)

    # 3 - By.CLASS_NAME
    el = driver.find_elements(By.CLASS_NAME, "j-item-basket")[0]
    print(el)

    # 4 - By.CLASS_NAME
    el = driver.find_elements(By.CLASS_NAME, "simple-menu__item--geo")[0]
    print(el)

    # 5 - By.CLASS_NAME
    el = driver.find_elements(By.CLASS_NAME, "nav-element__logo")[0]
    print(el)
