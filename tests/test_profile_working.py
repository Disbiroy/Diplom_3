import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Работа с профилем")
class TestProfileWorking:

    @allure.title("Переход в профиль после авторизации")
    def test_go_to_profile_after_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.go_to_login_page()
        login_page.wait_for_page_load()

        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        main_page.go_to_profile()
        profile_page.wait_for_page_load()

        assert profile_page.is_profile_page_loaded()

    @allure.title("Выход из профиля")
    def test_logout_from_profile(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.go_to_login_page()
        login_page.wait_for_page_load()

        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        main_page.go_to_profile()
        profile_page.wait_for_page_load()

        profile_page.logout()
        login_page.wait_for_page_load()

        assert login_page.is_login_button_visible()

    @allure.title("Переход в конструктор из профиля")
    def test_go_to_constructor_from_profile(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.go_to_login_page()
        login_page.wait_for_page_load()

        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        main_page.go_to_profile()
        profile_page.wait_for_page_load()

        profile_page.go_to_constructor()
        main_page.wait_for_page_load()

        assert main_page.is_constructor_section_visible()

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.go_to_login_page()
        login_page.wait_for_page_load()

        login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        main_page.wait_for_page_load()

        main_page.go_to_profile()
        profile_page.wait_for_page_load()

        profile_page.go_to_order_history()
        profile_page.wait_for_page_load()

        assert profile_page.is_order_history_visible()