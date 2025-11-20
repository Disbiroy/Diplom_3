from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Основные элементы
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/account/profile')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # История заказов
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'OrderHistory_text')]")
    ORDER_DATE = (By.XPATH, ".//span[contains(@class, 'OrderHistory_time')]")
    ORDER_STATUS = (By.XPATH, ".//span[contains(@class, 'OrderHistory_status')]")
    ORDER_TOTAL = (By.XPATH, ".//p[contains(@class, 'OrderHistory_total')]")

    # Конструктор и логотип - ИСПРАВЛЕННЫЕ ЛОКАТОРЫ ДЛЯ ХЕДЕРА
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Дополнительные локаторы для проверки загрузки страницы профиля
    PROFILE_SECTION = (By.XPATH, "//a[contains(@href, '/account/profile')]")
    PROFILE_FORM = (By.XPATH, "//form[contains(@class, 'Account_form')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")