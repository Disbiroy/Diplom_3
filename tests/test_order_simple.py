import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from selenium.webdriver.common.by import By
from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.feature("Оформление заказа")
class TestOrderSimple:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order_authorized(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.go_to_login_page()
        login_page.wait_for_page_load()

        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        # Добавление ингредиентов (только первый, чтобы избежать перехвата клика)
        main_page.click_ingredient(0)

        # Закрыть модальное окно ингредиента если открыто
        if main_page.is_ingredient_modal_displayed():
            main_page.close_ingredient_modal()

        # Используем универсальный поиск кнопки заказа
        order_button = main_page.wait_for_element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        order_button.click()

        # Ожидание подтверждения заказа
        order_modal = main_page.wait_for_element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(text(), 'идентификатор')]"))

        assert order_modal.is_displayed(), "Модальное окно с номером заказа не отображается"

    @allure.title("Проверка наличия кнопки оформления заказа")
    def test_order_button_exists(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()

        # Авторизуем пользователя
        main_page.go_to_login_page()
        login_page.wait_for_page_load()
        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        # Добавляем ингредиент, чтобы появилась кнопка заказа
        main_page.click_ingredient(0)

        # Закрываем модальное окно ингредиента если открыто
        if main_page.is_ingredient_modal_displayed():
            main_page.close_ingredient_modal()

        # Ищем кнопку заказа - используем более гибкий поиск
        try:
            order_button = main_page.find_element(
                (By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        except:
            # Если не нашли по полному тексту, ищем по частичному
            order_button = main_page.find_element(
                (By.XPATH, "//button[contains(., 'заказ')]"))

        assert order_button.is_displayed(), "Кнопка оформления заказа не отображается"
        assert "оформить" in order_button.text.lower() or "заказ" in order_button.text.lower()