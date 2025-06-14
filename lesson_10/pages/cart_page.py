from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure

class CartPage:
    """
    Класс страницы корзины.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver

        # Локаторы элементов страницы
        self.checkout_button_locator = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def checkout(self) -> None:
        """
        Переходит к оформлению заказа.

       :return: None
       """
       self.driver.find_element(*self.checkout_button_locator).click()
