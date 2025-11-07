import sys
import os
import pytest
import allure
import time
from selenium.webdriver.common.by import By

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Проверка отображения счетчиков заказов")
    def test_order_counters_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            time.sleep(3)

            # Проверяем что перешли на страницу заказов
            current_url = driver.current_url
            assert '/feed' in current_url, f"Ожидался переход на /feed, текущий URL: {current_url}"

        with allure.step("Проверить наличие счетчиков"):
            all_time_count = order_feed_page.get_orders_done_all_time()
            today_count = order_feed_page.get_orders_done_today()

            # Проверяем что счетчики возвращают числа (могут быть 0 если нет заказов)
            assert isinstance(all_time_count, int)
            assert isinstance(today_count, int)

            print(f"Заказов за все время: {all_time_count}")
            print(f"Заказов за сегодня: {today_count}")

    @allure.title("Проверка отображения заказов в работе")
    def test_orders_in_progress_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            time.sleep(3)

            current_url = driver.current_url
            assert '/feed' in current_url, f"Ожидался переход на /feed, текущий URL: {current_url}"

        with allure.step("Проверить, что раздел 'В работе' отображается"):
            # Проверяем наличие раздела "В работе"
            assert order_feed_page.is_orders_in_progress_section_visible()

    @allure.title("Проверка основных элементов ленты заказов")
    def test_order_feed_elements(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            time.sleep(3)

            current_url = driver.current_url
            assert '/feed' in current_url, f"Ожидался переход на /feed, текущий URL: {current_url}"

        with allure.step("Проверить наличие основных элементов"):
            assert order_feed_page.is_order_feed_loaded()

            # Проверяем что есть заказы (или пустой список)
            order_cards = driver.find_elements(By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__')]")
            print(f"Найдено заказов: {len(order_cards)}")