import pytest
import allure
from selenium import webdriver

from pages.authorization_page import AuthorizationPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Покупка товаров на сайте Saucedemo")
@allure.description("Тестовая сценарий покупки нескольких товаров и проверки итоговой суммы.")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_flow():
    with allure.step("Запуск браузера и открытие сайта"):
         driver = webdriver.Chrome()
         driver.maximize_window()

         auth_page = AuthorizationPage(driver)
         products_page = ProductsPage(driver)
         cart_page = CartPage(driver)
         checkout_page = CheckoutPage(driver)

         try:
             with allure.step("Авторизация пользователя"):
                 auth_page.open()
                 auth_page.login("standard_user", "secret_sauce")

             with allure.step("Добавление товаров в корзину"):
                 products_to_add = [
                     "Sauce Labs Backpack",
                     "Sauce Labs Bolt T-Shirt",
                     "Sauce Labs Onesie"
                 ]
                 for product in products_to_add:
                     products_page.add_product_to_cart(product)

             with allure.step("Переход в корзину"):
                 products_page.go_to_cart()

             with allure.step("Оформление заказа"):
                 cart_page.checkout()

             with allure.step("Заполнение формы данных покупателя"):
                 checkout_page.fill_form("Иван", "Иванов", "12345")

             with allure.step("Продолжение оформления заказа"):
                 checkout_page.continue_checkout()

             with allure.step("Получение итоговой суммы заказа"):
                 total_text = checkout_page.get_total()
                 print(f"Итоговая сумма: {total_text}")

             with allure.step("Проверка правильности суммы"):
                 assert total_text == "Total: $58.29"

         finally:
             driver.quit()
