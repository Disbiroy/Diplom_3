import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.locators.CONSTRUCTOR_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
        except Exception as e:
            print(f"Ошибка при клике на конструктор: {e}")
            # Пробуем обычный клик
            element = self.wait.until(EC.presence_of_element_located(self.locators.CONSTRUCTOR_BUTTON))
            element.click()
            time.sleep(2)

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        try:
            # Сначала проверяем, нет ли открытого модального окна
            if self.is_modal_displayed():
                self.close_modal()
                time.sleep(1)

            element = self.wait.until(EC.element_to_be_clickable(self.locators.ORDER_FEED_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        except Exception as e:
            print(f"Ошибка при клике на ленту заказов: {e}")
            # Пробуем обычный клик
            element = self.wait.until(EC.presence_of_element_located(self.locators.ORDER_FEED_BUTTON))
            element.click()
            time.sleep(3)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.driver.execute_script("arguments[0].scrollIntoView();", ingredients[index])
            ingredients[index].click()
            time.sleep(2)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            # Сначала пробуем найти и закрыть крестик
            close_btn = self.wait.until(EC.element_to_be_clickable(self.locators.MODAL_CLOSE_BUTTON))
            self.driver.execute_script("arguments[0].click();", close_btn)
            time.sleep(1)
        except:
            try:
                # Если крестик не нашли, пробуем кликнуть на overlay
                overlay = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
                self.driver.execute_script("arguments[0].click();", overlay)
                time.sleep(1)
            except:
                try:
                    # Пробуем ESC
                    body = self.driver.find_element(By.TAG_NAME, "body")
                    body.send_keys(Keys.ESCAPE)
                    time.sleep(1)
                except:
                    # Последняя попытка - клик по body
                    body = self.driver.find_element(By.TAG_NAME, "body")
                    body.click()
                    time.sleep(1)

        # Ждем пока модальное окно исчезнет
        try:
            self.wait_for_element_to_disappear(self.locators.INGREDIENT_MODAL)
        except:
            pass

    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_displayed(self):
        try:
            # Проверяем разные селекторы модальных окон
            selectors = [
                "//div[contains(@class, 'modal__container')]",
                "//div[contains(@class, 'Modal_modal__')]",
                "//div[contains(@class, 'Modal_overlay__')]"
            ]

            for selector in selectors:
                elements = self.driver.find_elements(By.XPATH, selector)
                for element in elements:
                    if element.is_displayed():
                        return True
            return False
        except:
            return False

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self, index=0):
        try:
            ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
            if ingredients and index < len(ingredients):
                counter_elements = ingredients[index].find_elements(*self.locators.INGREDIENT_COUNTER)
                if counter_elements and counter_elements[0].text:
                    return int(counter_elements[0].text)
        except:
            pass
        return 0

    @allure.step("Переключиться на раздел Соусы")
    def click_sauces_tab(self):
        try:
            # Сначала проверяем, нет ли открытого модального окна
            if self.is_modal_displayed():
                self.close_modal()
                time.sleep(1)

            element = self.find_element(self.locators.SAUCES_TAB)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except Exception as e:
            print(f"Ошибка при клике на вкладку соусов: {e}")
            element = self.find_element(self.locators.SAUCES_TAB)
            element.click()
            time.sleep(1)

    @allure.step("Переключиться на раздел Начинки")
    def click_fillings_tab(self):
        try:
            # Сначала проверяем, нет ли открытого модального окна
            if self.is_modal_displayed():
                self.close_modal()
                time.sleep(1)

            element = self.find_element(self.locators.FILLINGS_TAB)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except Exception as e:
            print(f"Ошибка при клике на вкладку начинок: {e}")
            element = self.find_element(self.locators.FILLINGS_TAB)
            element.click()
            time.sleep(1)

    @allure.step("Проверить, что конструктор загружен")
    def is_constructor_loaded(self):
        return self.is_element_visible(self.locators.BUNS_SECTION)

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        """Ждем пока страница полностью загрузится"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except:
            pass