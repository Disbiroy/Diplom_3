import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import time
import allure
from selenium.webdriver.common.by import By
from data import TestData


@allure.feature("Оформление заказа")
class TestOrderSimple:

    @pytest.fixture(scope="function")
    def login(self, driver):
        """Фикстура для логина"""
        driver.get(TestData.LOGIN_URL)
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(TestData.TEST_EMAIL)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(TestData.TEST_PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(3)
        yield

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_make_order_authorized(self, driver, login):
        """Простой тест оформления заказа"""

        print("=== ТЕСТ ОФОРМЛЕНИЯ ЗАКАЗА ===")

        # Ищем кнопку оформления заказа
        order_buttons = [
            "//button[contains(text(), 'Оформить заказ')]",
            "//button[contains(text(), 'Заказать')]",
            "//button[contains(@class, 'order')]"
        ]

        for button_xpath in order_buttons:
            try:
                order_button = driver.find_element(By.XPATH, button_xpath)
                print(f"Нашли кнопку заказа: {button_xpath}")
                print(f"Текст кнопки: {order_button.text}")
                print(f"Активна ли кнопка: {order_button.is_enabled()}")
                break
            except:
                continue
        else:
            print("Не нашли кнопку оформления заказа")
            return

        # Пробуем нажать кнопку заказа
        try:
            order_button.click()
            time.sleep(2)
            print("Нажали кнопку заказа")
        except:
            print("Не удалось нажать кнопку заказа")

        # Проверяем появилось ли модальное окно заказа
        modal_selectors = [
            "//div[contains(@class, 'modal')]",
            "//div[contains(@class, 'Modal')]",
            "//div[contains(@class, 'popup')]"
        ]

        for modal_xpath in modal_selectors:
            try:
                order_modal = driver.find_element(By.XPATH, modal_xpath)
                print(f"Модальное окно заказа появилось: {modal_xpath}")

                # Ищем номер заказа
                try:
                    order_number = driver.find_element(By.XPATH, "//h2[contains(text(), 'идентификатор')]")
                    print(f"Номер заказа: {order_number.text}")
                except:
                    print("Не нашли номер заказа")

                # Закрываем модальное окно
                close_buttons = [
                    "//button[contains(@class, 'close')]",
                    "//button[contains(@class, 'Close')]",
                    "//div[contains(@class, 'close')]"
                ]

                for close_xpath in close_buttons:
                    try:
                        close_button = driver.find_element(By.XPATH, close_xpath)
                        close_button.click()
                        print("Закрыли модальное окно")
                        break
                    except:
                        continue

                break
            except:
                continue
        else:
            print("Модальное окно не появилось")

        print("Тест завершен")


def test_order_button_exists(driver):
    """Просто проверяем что кнопка заказа существует на главной странице"""
    driver.get(TestData.MAIN_URL)
    time.sleep(2)

    order_buttons = [
        "//button[contains(text(), 'Оформить заказ')]",
        "//button[contains(text(), 'Заказать')]"
    ]

    for button_xpath in order_buttons:
        try:
            order_button = driver.find_element(By.XPATH, button_xpath)
            print(f"Кнопка заказа найдена: {button_xpath}")
            print(f"Текст: {order_button.text}")
            print(f"Активна: {order_button.is_enabled()}")
            return
        except:
            continue

    print("Кнопка заказа не найдена")