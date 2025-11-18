import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderFeedPageLocators:
    # УНИВЕРСАЛЬНЫЕ ЛОКАТОРЫ
    ORDER_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено')]/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list') or contains(@class, 'order-list')]")
    ORDER_STATISTICS = (By.XPATH, "//section[contains(@class, 'OrderFeed_board') or contains(@class, 'order-board') or contains(@class, 'OrderHistory')]")


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/feed"
        self.locators = OrderFeedPageLocators

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.driver.get(self.url)  # ВЕРНУЛИ КАК БЫЛО!

    @allure.step("Проверить отображение счетчика заказов")
    def is_order_count_displayed(self):
        return self.is_element_visible(self.locators.ORDER_COUNT)

    @allure.step("Проверить отображение заказов в работе")
    def is_orders_in_progress_displayed(self):
        return self.is_element_visible(self.locators.ORDERS_IN_PROGRESS)

    @allure.step("Проверить отображение списка заказов")
    def is_order_list_displayed(self):
        return self.is_element_visible(self.locators.ORDER_LIST)

    @allure.step("Проверить отображение статистики заказов")
    def is_order_statistics_displayed(self):
        return self.is_element_visible(self.locators.ORDER_STATISTICS)