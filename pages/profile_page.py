from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/account/profile"
        self.locators = ProfilePageLocators

    @allure.step("Перейти в личный кабинет")
    def go_to_profile(self):
        self.click_element(self.locators.PROFILE_LINK)

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        self.click_element(self.locators.ORDER_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click_element(self.locators.LOGOUT_BUTTON)

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_element(self.locators.CONSTRUCTOR_LINK)

    @allure.step("Проверить что мы на странице истории заказов")
    def is_order_history_visible(self):
        return "order-history" in self.current_url()

    @allure.step("Проверить что загрузилась страница профиля")
    def is_profile_page_loaded(self):
        try:
            current_url = self.current_url()
            # Более надежная проверка - проверяем URL и наличие элементов профиля
            is_correct_url = "/account" in current_url
            has_profile_elements = (
                self.is_element_visible(self.locators.PROFILE_LINK, timeout=5) or
                self.is_element_visible(self.locators.NAME_INPUT, timeout=5) or
                self.is_element_visible(self.locators.EMAIL_INPUT, timeout=5) or
                self.is_element_visible(self.locators.LOGOUT_BUTTON, timeout=5)
            )
            return is_correct_url and has_profile_elements
        except Exception as e:
            print(f"Error checking profile page: {e}")
            return False