from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import allure

class AuthorizationPage:
    """
    Класс страницы авторизации.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver

        # Локаторы элементов страницы
        self.username_input_locator = (By.ID, "user-name")
        self.password_input_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Войти с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход пользователя.

        :param username: логин пользователя.
        :param password: пароль пользователя.
        :return: None
        """
        self.driver.find_element(*self.username_input_locator).send_keys(username)
        self.driver.find_element(*self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.login_button_locator).click()
