from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure

class ProductsPage:
    """
    Класс страницы товаров.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы товаров.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver

        # Локаторы элементов страницы
        self.product_name_locator_template = "//div[@class='inventory_item_name' and text()='{product_name}']"
        self.add_to_cart_button_locator_template = "//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        self.cart_icon_locator = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию.

        :param product_name: название товара.
        :return: None
        """
        add_button_xpath = self.add_to_cart_button_locator_template.format(product_name=product_name)
        
        # Можно добавить проверку наличия элемента перед кликом (опционально)
        
        self.driver.find_element(By.XPATH, add_button_xpath).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.driver.find_element(*self.cart_icon_locator).click()
