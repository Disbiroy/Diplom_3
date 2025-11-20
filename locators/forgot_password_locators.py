from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    # Страница восстановления пароля
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # Страница с полем для кода
    CODE_INPUT = (By.XPATH, "//input[@placeholder='Введите код из письма']")

    # Страница смены пароля
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

    # Ссылка "Войти" на странице восстановления
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Глазок для показа/скрытия пароля
    PASSWORD_VISIBILITY_TOGGLE = (By.XPATH, "//div[contains(@class, 'input__icon')]")