# TASK 2
# https://candymapper.com/ - prod
# https://candymapperr2.com/ - test
#
# --env=test
# на странице заголовок и урл
#
# def pytest_session_start(session):
#   pytest.env = ''

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="test", choices=["test", "prod"], help="Select environment: test or prod"
    )


def pytest_session_start(session):
    pytest.env = session.config.getoption("--env")


@pytest.fixture(scope="session")
def base_url():
    urls = {
        "prod": "https://candymapper.com/",
        "test": "https://candymapperr2.com/",
    }
    return urls.get(pytest.env, urls["test"])
