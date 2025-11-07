from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, 'feed')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")

    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")

    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__P3_V5')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")