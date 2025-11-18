import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, 'account')]")
    CONSTRUCTOR_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")

    # УНИВЕРСАЛЬНЫЕ ЛОКАТОРЫ ДЛЯ МОДАЛЬНОГО ОКНА
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal') or contains(@class, 'modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH,
                          "//button[contains(@class, 'Modal_modal__close') or contains(@class, 'modal__close')]")

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://stellarburgers.education-services.ru/"
        self.locators = MainPageLocators

    @allure.step("Перейти на страницу логина")
    def go_to_login_page(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        self.click_element(self.locators.PROFILE_BUTTON)

    @allure.step("Проверить видимость конструктора")
    def is_constructor_section_visible(self):
        return self.is_element_visible(self.locators.CONSTRUCTOR_SECTION)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.url)  # ВЕРНУЛИ КАК БЫЛО!

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click_element(self.locators.ORDER_FEED_LINK)

    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click_element(self.locators.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.scroll_to_element(self.locators.INGREDIENT_ITEM)
            self.click_element(self.locators.INGREDIENT_ITEM)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click_element(self.locators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_to_disappear(self.locators.MODAL_WINDOW)
        except:
            self.send_escape_key()

    @allure.step("Переключиться на вкладку булок")
    def click_buns_tab(self):
        self.click_element(self.locators.BUNS_TAB)

    @allure.step("Переключиться на вкладку соусов")
    def click_sauces_tab(self):
        self.click_element(self.locators.SAUCES_TAB)

    @allure.step("Переключиться на вкладку начинок")
    def click_fillings_tab(self):
        self.click_element(self.locators.FILLINGS_TAB)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self, index=0):
        try:
            ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
            if ingredients and index < len(ingredients):
                counter_elements = ingredients[index].find_elements(*self.locators.INGREDIENT_COUNTER)
                if counter_elements and counter_elements[0].text:
                    return int(counter_elements[0].text)
        except:
            pass
        return 0