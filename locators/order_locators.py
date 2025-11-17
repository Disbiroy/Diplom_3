from selenium.webdriver.common.by import By


class OrderLocators:
    # Кнопки оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'OrderModal')]//h2")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")

    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    BUN_SECTION = (By.XPATH, "//h2[text()='Булки']/..")
    SAUCE_SECTION = (By.XPATH, "//h2[text()='Соусы']/..")
    FILLING_SECTION = (By.XPATH, "//h2[text()='Начинки']/..")

    # Конструктор бургера
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    BUN_IN_CONSTRUCTOR = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_bun')]")
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_ingredient')]")

    # Счетчик заказов
    ORDER_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]")