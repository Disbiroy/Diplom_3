from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/forgot-password"
        self.locators = ForgotPasswordLocators

    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввести email")
    def set_email(self, email):
        self.send_keys(self.locators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку восстановления")
    def click_restore_button(self):
        self.click_element(self.locators.RESTORE_BUTTON)

    @allure.step("Нажать ссылку Войти")
    def click_login_link(self):
        self.click_element(self.locators.LOGIN_LINK)

    @allure.step("Проверить видимость поля email")
    def is_email_input_visible(self):
        return self.is_element_visible(self.locators.EMAIL_INPUT)