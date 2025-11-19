from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Кнопка личного кабинета в хедере
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, 'account')]")

    # В личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, 'order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'logo')]")

    # Добавим локаторы для проверки загрузки страницы профиля
    PROFILE_SECTION = (By.XPATH, "//a[contains(@href, '/account/profile')]")
    PROFILE_FORM = (By.XPATH, "//form[contains(@class, 'Account_form')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/account/profile"

    def go_to_profile(self):
        """Переходит в личный кабинет после логина"""
        self.click_element(ProfilePageLocators.PROFILE_BUTTON)

    def go_to_order_history(self):
        """Переходит в историю заказов"""
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    def logout(self):
        """Выходит из аккаунта"""
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def go_to_constructor(self):
        """Переходит в конструктор"""
        self.click_element(ProfilePageLocators.CONSTRUCTOR_LINK)

    def is_order_history_visible(self):
        """Проверяет что мы на странице истории заказов"""
        return "order-history" in self.current_url()

    def is_profile_page_loaded(self):
        """Проверяет что загрузилась страница профиля"""
        try:
            current_url = self.current_url()
            # Простая проверка - если URL содержит /account, считаем что это профиль
            return "/account" in current_url
        except:
            return False