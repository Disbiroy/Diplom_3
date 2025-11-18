from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/forgot-password"

    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self.driver.get(self.url)  # ДОБАВИЛИ МЕТОД open()

    @allure.step("Ввести email")
    def set_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку восстановления")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Нажать ссылку Войти")
    def click_login_link(self):
        self.click_element(ForgotPasswordLocators.LOGIN_LINK)

    @allure.step("Проверить видимость поля email")
    def is_email_input_visible(self):
        return self.is_element_visible(ForgotPasswordLocators.EMAIL_INPUT)