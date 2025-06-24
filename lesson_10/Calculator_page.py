from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Локатор поля задержки
    delay_input_locator = (By.CSS_SELECTOR, "#delay")
    # Локатор результата
    result_locator = (By.ID, "result")
    # Локаторы кнопок цифр и операторов (используем XPath по тексту)
    button_xpath_template = "//button[text()='{}']"

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self.delay_input_locator)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, label: str):
        button = self.driver.find_element(By.XPATH, self.button_xpath_template.format(label))
        button.click()

    def get_result(self) -> str:
        result_element = self.driver.find_element(*self.result_locator)
        return result_element.text.strip()