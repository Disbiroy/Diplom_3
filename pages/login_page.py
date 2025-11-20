from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/login"
        self.locators = LoginPageLocators

    @allure.step("Ввести email")
    def set_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.send_keys(self.locators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку Войти")
    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step("Нажать ссылку Восстановить пароль")
    def click_forgot_password_link(self):
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)

    @allure.step("Нажать ссылку Зарегистрироваться")
    def click_register_link(self):
        self.click_element(self.locators.REGISTER_LINK)

    @allure.step("Выполнить логин")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step("Проверить видимость кнопки Войти")
    def is_login_button_visible(self):
        return self.is_element_visible(self.locators.LOGIN_BUTTON)