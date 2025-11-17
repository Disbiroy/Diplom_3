import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import time
import allure
from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfileWorking:

    @pytest.fixture(scope="function")
    def login(self, driver):
        """Фикстура для логина и перехода в профиль"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        # Логинимся
        main_page.open()
        main_page.go_to_login_page()
        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)

        # Переходим в личный кабинет
        time.sleep(2)
        profile_page.go_to_profile()

        # Ждем загрузки профиля
        time.sleep(2)

        yield

        # Выход после каждого теста
        try:
            if "account" in driver.current_url:
                profile_page.logout()
                time.sleep(2)
        except:
            pass

    @allure.title("Переход в личный кабинет после логина")
    def test_go_to_profile_after_login(self, driver, login):
        profile_page = ProfilePage(driver)

        # Проверяем что мы в личном кабинете
        assert "account" in driver.current_url
        print("Успешно перешли в личный кабинет")

    @allure.title("Выход из аккаунта")
    def test_logout_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)

        # Выходим из аккаунта
        profile_page.logout()
        time.sleep(2)

        # Проверяем что вернулись на страницу логина
        assert "login" in driver.current_url
        print("Успешно вышли из аккаунта")

    @allure.title("Переход в конструктор из личного кабинета")
    def test_go_to_constructor_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)

        # Переходим в конструктор
        profile_page.go_to_constructor()
        time.sleep(2)

        # Проверяем что мы на главной странице
        assert driver.current_url == TestData.MAIN_URL
        print("Успешно перешли в конструктор")

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)

        # Переходим в историю заказов
        profile_page.go_to_order_history()
        time.sleep(2)

        # Проверяем что мы на странице истории заказов
        assert "order-history" in driver.current_url
        print("Успешно перешли в историю заказов")