import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage

def test_slow_calculator():
    driver = webdriver.Chrome()  # или другой драйвер
    calculator = CalculatorPage(driver)

    try:
        # Открываем страницу
        calculator.open()

        # Вводим задержку 45 секунд
        calculator.set_delay("45")

        # Выполняем вычисление 7 + 8 =
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

        # Используем явное ожидание появления результата "15"
        wait = WebDriverWait(driver, 46)
        wait.until(
            EC.text_to_be_present_in_element(calculator.result_locator, "15")
        )

        # Получаем и проверяем результат
        result = calculator.get_result()
        assert result == "15", f"Expected '15', but got '{result}'"

    finally:
        driver.quit()
