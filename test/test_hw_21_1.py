# TASK 1
# 1, https://practicetestautomation.com/practice-test-login/
# покрыть форму авторизации в соответствии с тест кейсами которые там указаны
# + проверь открытие страницы (отображение всех элементов)
# + с expected condition

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# --------- Preconditions ---------

url = "https://practicetestautomation.com/practice-test-login/"


def open_site(driver, url=url):
    driver.get(url)


def get_element(driver, selector, timeout=5):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(selector))
    return element


def element_check_visible(driver, selector):
    element = driver.find_element(*selector)
    assert element.is_displayed()


def click(driver, selector, timeout=10):
    element = get_element(driver, selector, timeout)
    element.click()


def element_check(driver, selector, expected):
    element = get_element(driver, selector)
    actual = element.text.strip()
    assert actual == expected


def enter_text(driver, selector, text):
    element = get_element(driver, selector)
    element.send_keys(text)


def check_success_url(driver):
    current_url = driver.current_url
    assert "practicetestautomation.com/logged-in-successfully/" in current_url


# --------- Check all elements on the page ---------


@pytest.mark.smoke
def test_check_all_elements(driver):
    open_site(driver)
    element_check_visible(driver, (By.CSS_SELECTOR, ".custom-logo-link"))
    element_check_visible(driver, (By.LINK_TEXT, "HOME"))
    element_check_visible(driver, (By.LINK_TEXT, "PRACTICE"))
    element_check_visible(driver, (By.LINK_TEXT, "COURSES"))
    element_check_visible(driver, (By.LINK_TEXT, "BLOG"))
    element_check_visible(driver, (By.LINK_TEXT, "CONTACT"))
    element_check(driver, (By.CSS_SELECTOR, "#login > h2"), "Test login")
    element_check(
        driver,
        (By.XPATH, '//*[@id="login"]/ul/li[1]'),
        "This is a simple Login page. Students can use this page to practice "
        "writing simple positive and negative LogIn tests. Login functionality "
        "is something that most of the test automation engineers need to automate.",
    )
    element_check(
        driver,
        (By.CSS_SELECTOR, "#login > ul > li:nth-child(2)"),
        "Use next credentials to execute Login:\n" "Username: student\n" "Password: Password123",
    )
    element_check_visible(driver, (By.XPATH, '//*[@id="username"]'))
    element_check_visible(driver, (By.XPATH, '//*[@id="password"]'))
    element_check_visible(driver, (By.XPATH, '//*[@id="submit"]'))


# --------- Test case 1: Positive LogIn test ---------


@pytest.mark.smoke
def test_positive_login(driver):
    open_site(driver)
    enter_text(driver, (By.XPATH, '//*[@id="username"]'), "student")
    enter_text(driver, (By.XPATH, '//*[@id="password"]'), "Password123")
    click(driver, (By.XPATH, '//*[@id="submit"]'))
    check_success_url(driver)
    element_check(driver, (By.XPATH, '//*[@id="loop-container"]/div/article/div[1]/h1'), "Logged In Successfully")
    element_check_visible(driver, (By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a'))


@pytest.mark.smoke
def test_negative_username(driver):
    open_site(driver)
    enter_text(driver, (By.XPATH, '//*[@id="username"]'), "incorrectUser")
    enter_text(driver, (By.XPATH, '//*[@id="password"]'), "Password123")
    click(driver, (By.XPATH, '//*[@id="submit"]'))
    element_check(driver, (By.XPATH, '//*[@id="error"]'), "Your username is invalid!")


@pytest.mark.smoke
def test_negative_password(driver):
    open_site(driver)
    enter_text(driver, (By.XPATH, '//*[@id="username"]'), "student")
    enter_text(driver, (By.XPATH, '//*[@id="password"]'), "incorrectPassword")
    click(driver, (By.XPATH, '//*[@id="submit"]'))
    element_check(driver, (By.XPATH, '//*[@id="error"]'), "Your password is invalid!")
