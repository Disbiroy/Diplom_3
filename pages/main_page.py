from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, 'account')]")
    CONSTRUCTOR_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")

    # ИСПРАВЛЕННЫЕ ЛОКАТОРЫ:
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")

    # Модальное окно (ИСПРАВЛЕННЫЕ)
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    # Табы конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/"

    def go_to_login_page(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def go_to_profile(self):
        self.click_element(MainPageLocators.PROFILE_BUTTON)

    def is_constructor_section_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_SECTION)

    def open(self):
        self.driver.get(self.url)

    # ОСНОВНЫЕ МЕТОДЫ:
    def click_order_feed(self):
        """Кликает на раздел 'Лента заказов'"""
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    def click_constructor(self):
        """Кликает на раздел 'Конструктор'"""
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_ingredient(self, index=0):
        """Кликает на ингредиент по индексу"""
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            ingredients[index].click()

    def close_modal(self):
        """Закрывает модальное окно"""
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_modal_visible(self):
        """Проверяет видимость модального окна"""
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW)

    def click_sauces_tab(self):
        """Кликает на таб 'Соусы'"""
        self.click_element(MainPageLocators.SAUCES_TAB)

    def click_fillings_tab(self):
        """Кликает на таб 'Начинки'"""
        self.click_element(MainPageLocators.FILLINGS_TAB)

    def get_ingredient_counter(self, index=0):
        """Получает значение счетчика ингредиента"""
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            try:
                counter = ingredients[index].find_element(*MainPageLocators.INGREDIENT_COUNTER)
                return counter.text
            except:
                return "0"
        return "0"

    def is_constructor_loaded(self):
        """Проверяет загрузился ли конструктор"""
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_SECTION)