import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from data import TestData
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Отображение счетчиков заказов")
    def test_order_counters_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        order_feed_page.wait_for_page_load()

        assert order_feed_page.is_order_count_displayed()

    @allure.title("Отображение заказов в работе")
    def test_orders_in_progress_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        order_feed_page.wait_for_page_load()

        assert order_feed_page.is_orders_in_progress_displayed()

    @allure.title("Элементы ленты заказов")
    def test_order_feed_elements(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open()
        order_feed_page.wait_for_page_load()

        assert order_feed_page.is_order_list_displayed()