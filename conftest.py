import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    ),
    parser.addoption(
        "--url", default="http://localhost:8081", help="URL to run tests"
    ),
    parser.addoption(
        "--driver", default="./drivers/", help="Path to driver directory"
    )
    parser.addoption(
        "--wait"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers_storage = request.config.getoption("--driver")
    _driver = None
    if browser_name == "chrome":
        S = Service(f'{drivers_storage}/chromedriver')
        _driver = webdriver.Chrome(service=S)

    elif browser_name == "firefox":
        S = Service(f'{drivers_storage}/geckodriver')
        _driver = webdriver.Firefox(service=S)

    elif browser_name == "edge":
        S = Service(f'{drivers_storage}/msedgedriver')
        _driver = webdriver.ChromiumEdge(service=S)

    yield _driver, url
    _driver.close()
