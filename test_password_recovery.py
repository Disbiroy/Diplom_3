import pytest
import allure
import sys
import os

# Добавляем корневую директорию в Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from locators.forgot_password_locators import ForgotPasswordLocators


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля со страницы логина")
    def test_go_to_password_recovery_from_login(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        forgot_password_page = ForgotPasswordPage(browser)

        # Открываем главную страницу
        main_page.open()
        # Переходим на страницу логина
        main_page.go_to_login_page()
        # Кликаем на "Восстановить пароль"
        login_page.click_forgot_password_link()

        # Проверяем что перешли на страницу восстановления пароля
        current_url = forgot_password_page.current_url()
        assert current_url == TestData.PASSWORD_RECOVERY_URL, f"Expected {TestData.PASSWORD_RECOVERY_URL}, got {current_url}"
        assert forgot_password_page.is_email_input_visible(), "Email input field is not visible"

    @allure.title("Переход по ссылке 'Войти' со страницы восстановления пароля")
    def test_go_to_login_from_password_recovery(self, browser):
        forgot_password_page = ForgotPasswordPage(browser)

        # Открываем страницу восстановления пароля напрямую
        forgot_password_page.open(TestData.PASSWORD_RECOVERY_URL)
        # Кликаем на ссылку "Войти"
        forgot_password_page.click_login_link()

        # Проверяем что перешли на страницу логина
        current_url = forgot_password_page.current_url()
        assert current_url == TestData.LOGIN_URL, f"Expected {TestData.LOGIN_URL}, got {current_url}