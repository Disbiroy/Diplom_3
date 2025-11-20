import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Главная страница")
class TestMain:

    @allure.title("Навигация: клик на 'Конструктор'")
    def test_click_constructor_navigation(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_page_load()

        main_page.click_constructor()
        main_page.wait_for_page_load()

        assert main_page.is_constructor_section_visible()

    @allure.title("Навигация: клик на 'Лента заказов'")
    def test_click_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_page_load()

        current_url = order_feed_page.current_url()
        assert "/feed" in current_url

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opening(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient(0)

        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_ingredient_modal_closing(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_ingredient(0)
        main_page.wait_for_element_to_be_clickable(main_page.locators.INGREDIENT_MODAL_CLOSE_BUTTON)

        main_page.close_ingredient_modal()
        main_page.wait_for_element_to_disappear(main_page.locators.INGREDIENT_MODAL_WINDOW)

        assert not main_page.is_ingredient_modal_displayed()

    @allure.title("Навигация по табам конструктора")
    def test_constructor_tabs_navigation(self, driver):
        main_page = MainPage(driver)

        main_page.open()

        # Кликаем на соусы и проверяем что секция соусов отображается
        main_page.click_sauces_tab()
        assert main_page.is_element_visible(main_page.locators.SAUCES_TAB)

        # Кликаем на начинки и проверяем что секция начинок отображается
        main_page.click_fillings_tab()
        assert main_page.is_element_visible(main_page.locators.FILLINGS_TAB)

        # Возвращаемся к булкам и проверяем что секция булок отображается
        main_page.click_buns_tab()
        assert main_page.is_element_visible(main_page.locators.BUNS_TAB)

    @allure.title("Проверка счетчиков ингредиентов")
    def test_ingredient_counters(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        counter = main_page.get_ingredient_counter(0)
        assert counter == 0


@allure.feature("Лента заказов на главной")
class TestOrderFeedMain:

    @allure.title("Отображение счетчиков заказов")
    def test_order_counters_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_page_load()

        assert order_feed_page.is_order_count_displayed()

    @allure.title("Отображение заказов в работе")
    def test_orders_in_progress_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_page_load()

        assert order_feed_page.is_orders_in_progress_displayed()