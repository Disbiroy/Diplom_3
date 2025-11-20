from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки навигации в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']//p[text()='Лента Заказов']")

    # Основные элементы страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, 'account')]//p[text()='Личный Кабинет']")
    CONSTRUCTOR_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']//p[text()='Лента Заказов']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")

    # Вкладки конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")

    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter')]")

    # Модальные окна
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    INGREDIENT_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_')]")

    # Конструктор бургера
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")

    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")