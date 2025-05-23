import pytest
from selenium import webdriver
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

        # Ждем примерно 45 секунд для отображения результата
        time.sleep(45)

        # Проверка результата
        result = calculator.get_result()
        assert result == "15", f"Expected '15', but got '{result}'"

    finally:
        driver.quit()
