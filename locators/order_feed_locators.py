from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Page title
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    # Order statistics
    ORDERS_DONE_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Orders in progress
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(), 'В работе:')]")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]")

    # Order cards
    ORDER_CARDS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")