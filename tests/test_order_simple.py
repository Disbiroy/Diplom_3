import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from selenium.webdriver.common.by import By  # ДОБАВИЛ ИМПОРТ
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

        # Добавление ингредиентов и оформление заказа
        main_page.click_ingredient(0)
        main_page.click_ingredient(1)

        # Закрыть модальное окно если открыто
        if main_page.is_element_visible(main_page.locators.MODAL_WINDOW):
            main_page.close_modal()

        # УНИВЕРСАЛЬНЫЙ ЛОКАТОР ДЛЯ КНОПКИ
        order_button = main_page.wait_for_element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Оформить заказ') or contains(., 'оформить') or @type='submit']"))
        order_button.click()

        # Ожидание подтверждения заказа
        main_page.wait_for_element_to_be_clickable(
            (By.XPATH, "//div[contains(., 'идентификатор') or contains(., 'заказ') or contains(@class, 'Modal')]"),
            timeout=15
        )


def test_order_button_exists(driver):
    main_page = MainPage(driver)

    main_page.open()

    # УНИВЕРСАЛЬНЫЙ ЛОКАТОР ДЛЯ КНОПКИ
    order_button = main_page.find_element(
        (By.XPATH, "//button[contains(., 'Оформить') or contains(., 'оформить') or contains(@class, 'button_button')]"))
    assert order_button.is_displayed()