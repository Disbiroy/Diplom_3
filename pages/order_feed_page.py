import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step("Проверить, что страница ленты заказов загружена")
    def is_order_feed_loaded(self):
        try:
            return self.is_element_visible(self.locators.ORDER_FEED_TITLE)
        except:
            # Проверяем по URL
            return '/feed' in self.driver.current_url

    @allure.step("Получить количество выполненных заказов за все время")
    def get_orders_done_all_time(self):
        try:
            text = self.get_text(self.locators.ORDERS_DONE_ALL_TIME)
            return int(text) if text and text.isdigit() else 0
        except:
            return 0

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_orders_done_today(self):
        try:
            text = self.get_text(self.locators.ORDERS_DONE_TODAY)
            return int(text) if text and text.isdigit() else 0
        except:
            return 0

    @allure.step("Проверить наличие раздела 'В работе'")
    def is_orders_in_progress_section_visible(self):
        return self.is_element_visible(self.locators.ORDERS_IN_PROGRESS_SECTION)