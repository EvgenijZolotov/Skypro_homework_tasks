import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="edge", 
        help="Browser to use: edge or safari"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)

    elif browser_name == "safari":
        options = SafariOptions()
        driver = webdriver.Safari(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()
