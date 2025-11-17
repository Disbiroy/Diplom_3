from .base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/forgot-password"

    def set_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)

    def click_login_link(self):
        self.click_element(ForgotPasswordLocators.LOGIN_LINK)

    def is_email_input_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.EMAIL_INPUT)