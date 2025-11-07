import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None

    try:
        if browser_name == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.implicitly_wait(10)
        driver.maximize_window()

        # Открываем главную страницу
        driver.get("https://stellarburgers.education-services.ru/")

        # Ждем загрузки страницы
        driver.execute_script("return document.readyState") == "complete"

        yield driver

    except Exception as e:
        print(f"Error initializing driver: {e}")
        if driver:
            driver.quit()
        raise

    finally:
        if driver:
            # Скриншот при падении
            if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
                try:
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=f"{request.node.name}_failure",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as screenshot_error:
                    print(f"Failed to take screenshot: {screenshot_error}")

            driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)