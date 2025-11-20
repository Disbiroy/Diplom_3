import allure
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/feed"
        self.locators = OrderFeedLocators

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Проверить отображение счетчика заказов")
    def is_order_count_displayed(self):
        return self.is_element_visible(self.locators.ORDERS_DONE_ALL_TIME)

    @allure.step("Проверить отображение заказов в работе")
    def is_orders_in_progress_displayed(self):
        return self.is_element_visible(self.locators.ORDERS_IN_PROGRESS_SECTION)

    @allure.step("Проверить отображение списка заказов")
    def is_order_list_displayed(self):
        return self.is_element_visible(self.locators.ORDER_CARDS)

    @allure.step("Проверить отображение статистики заказов")
    def is_order_statistics_displayed(self):
        return self.is_element_visible(self.locators.ORDERS_DONE_ALL_TIME)