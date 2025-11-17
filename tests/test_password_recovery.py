import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        # Открываем главную страницу и переходим к логину
        main_page.open()
        main_page.go_to_login_page()

        # Кликаем на "Восстановить пароль"
        login_page.click_forgot_password_link()

        # Проверяем что перешли на страницу восстановления пароля
        current_url = forgot_password_page.current_url()
        assert current_url == TestData.PASSWORD_RECOVERY_URL
        assert forgot_password_page.is_email_input_visible()

    @allure.title("Переход по ссылке 'Войти' со страницы восстановления пароля")
    def test_go_to_login_from_password_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)

        # Открываем страницу восстановления пароля напрямую
        forgot_password_page.open(TestData.PASSWORD_RECOVERY_URL)

        # Кликаем на ссылку "Войти"
        forgot_password_page.click_login_link()

        # Проверяем что перешли на страницу логина
        current_url = login_page.current_url()
        assert current_url == TestData.LOGIN_URL
        assert login_page.is_login_button_visible()