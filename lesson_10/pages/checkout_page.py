from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

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

       # Локаторы элементов формы и итоговой суммы
       self.first_name_input_locator = (By.ID, "first-name")
       self.last_name_input_locator = (By.ID, "last-name")
       self.postal_code_input_locator = (By.ID, "postal-code")
       self.continue_button_locator = (By.ID, "continue")
       self.total_price_locator = (By.CLASS_NAME, "summary_total_label")

   @allure.step("Заполнить форму заказа именем '{first_name}', фамилией '{last_name}', индексом '{postal_code}'")
   def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
       """
       Заполняет форму данных покупателя.

       :param first_name: имя.
       :param last_name: фамилия.
       :param postal_code: индекс.
       :return: None
       """
       self.driver.find_element(*self.first_name_input_locator).send_keys(first_name)
       self.driver.find_element(*self.last_name_input_locator).send_keys(last_name)
       self.driver.find_element(*self.postal_code_input_locator).send_keys(postal_code)

   @allure.step("Нажать кнопку Continue для продолжения оформления заказа")
   def continue_checkout(self) -> None:
      """
      Продолжает оформление заказа.

      :return: None
      """
      self.driver.find_element(*self.continue_button_locator).click()

   @allure.step("Получить итоговую сумму заказа")
   def get_total(self) -> str:
      """
      Получает текст итоговой суммы заказа.

      :return: строка с итоговой суммой.
      """
      return self.driver.find_element(*self.total_price_locator).text.strip()
