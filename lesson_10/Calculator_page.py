from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Локатор поля задержки
        self.delay_input_locator = (By.CSS_SELECTOR, "#delay")
        # Локатор результата
        self.result_locator = (By.CSS_SELECTOR, ".screen")
        # Обновленный шаблон XPath для кнопок <span>
        self.button_xpath_template = "//span[text()='{}']"

    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: str):
        """
        Устанавливает задержку перед выполнением вычислений.

        :param seconds: строковое значение задержки в секундах.
        """
        delay_field = self.driver.find_element(*self.delay_input_locator)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, label: str):
        """
        Нажимает кнопку с указанной меткой.

        :param label: текст кнопки (например, "7", "+", "=").
        """
        button = self.driver.find_element(By.XPATH, self.button_xpath_template.format(label))
        button.click()

    def get_result(self) -> str:
        """
        Получает текст результата вычисления.

        :return: результат в виде строки.
        """
        result_element = self.driver.find_element(*self.result_locator)
        return result_element.text.strip()
