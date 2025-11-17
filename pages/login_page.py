from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/login"

    def set_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def is_login_button_visible(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)