import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля со страницы логина")
    def test_go_to_password_recovery_from_login(self, driver):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            login_page = LoginPage(driver)
            forgot_password_page = ForgotPasswordPage(driver)

        with allure.step("Открываем главную страницу и переходим к логину"):
            main_page.open()
            main_page.go_to_login_page()

        with allure.step("Кликаем на 'Восстановить пароль'"):
            login_page.click_forgot_password_link()

        with allure.step("Проверяем что перешли на страницу восстановления пароля"):
            # ИСПРАВЛЕНО: используем wait_for_url
            forgot_password_page.wait_for_url(TestData.PASSWORD_RECOVERY_URL)
            current_url = forgot_password_page.current_url()
            assert current_url == TestData.PASSWORD_RECOVERY_URL, f"Expected {TestData.PASSWORD_RECOVERY_URL}, got {current_url}"
            assert forgot_password_page.is_email_input_visible()

    @allure.title("Переход по ссылке 'Войти' со страницы восстановления пароля")
    def test_go_to_login_from_password_recovery(self, driver):
        with allure.step("Инициализация страниц"):
            forgot_password_page = ForgotPasswordPage(driver)
            login_page = LoginPage(driver)

        with allure.step("Открываем страницу восстановления пароля напрямую"):
            forgot_password_page.open()

        with allure.step("Кликаем на ссылку 'Войти'"):
            forgot_password_page.click_login_link()

        with allure.step("Проверяем что перешли на страницу логина"):
            # ИСПРАВЛЕНО: используем wait_for_url
            login_page.wait_for_url(TestData.LOGIN_URL)
            current_url = login_page.current_url()
            assert current_url == TestData.LOGIN_URL, f"Expected {TestData.LOGIN_URL}, got {current_url}"
            assert login_page.is_login_button_visible()