import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable: {locator}"
        )

    def click_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def js_click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_visible(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ) is not None
        except:
            return False

    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def send_escape_key(self):
        body = self.find_element((By.TAG_NAME, "body"))
        body.send_keys(Keys.ESCAPE)

    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def get_element_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, text, timeout=10):
        """Ввод текста в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # ДОБАВИЛ ЭТОТ МЕТОД ↓
    def wait_for_url(self, expected_url, timeout=10):
        """Ждать пока URL станет ожидаемым"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )