def test_pytest(driver):
    url = "https://docs.pytest.org/en/stable/"
    driver.get(url)
    assert driver.title == "pytest documentation"
    assert driver.current_url == url
