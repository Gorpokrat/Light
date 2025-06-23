from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure


class CheckoutPage:
    """
    Класс страницы оформления заказа.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов формы и итоговой суммы
        self.first_name_input_locator = (By.ID, "first-name")
        self.last_name_input_locator = (By.ID, "last-name")
        self.postal_code_input_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")
        self.total_price_locator = (By.CLASS_NAME, "summary_total_label")

    @allure.step(
        "Заполнить форму заказа именем '{first_name}', "
        "фамилией '{last_name}', индексом '{postal_code}'"
    )
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму данных покупателя.

        :param first_name: имя.
        :param last_name: фамилия.
        :param postal_code: индекс.
        :return: None
        """
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.first_name_input_locator)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.last_name_input_locator)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.element_to_be_clickable(self.postal_code_input_locator)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    @allure.step("Нажать кнопку Continue для продолжения оформления заказа")
    def continue_checkout(self) -> None:
        """
        Продолжает оформление заказа.

        :return: None
        """
        
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button_locator)
        )
        
        continue_button.click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
       """
       Получает текст итоговой суммы заказа.

       :return: строка с итоговой суммой.
       """
       total_element = self.wait.until(
           EC.visibility_of_element_located(self.total_price_locator)
       )
       return total_element.text.strip()
