import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage


@allure.title("Тест медленной работы калькулятора")
@allure.description("Проверка работы калькулятора с задержкой 45 секунд и вычислением 7 + 8.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    """
    Тест проверяет работу калькулятора с установленной задержкой,
    выполнение операции 7 + 8 и проверку результата.
    """

    with allure.step("Инициализация драйвера Chrome"):
        driver = webdriver.Chrome()

    calculator = CalculatorPage(driver)

    try:
        with allure.step("Открытие страницы калькулятора"):
            calculator.open()

        with allure.step("Установка задержки 45 секунд"):
            calculator.set_delay("45")

        with allure.step("Ввод числа '7'"):
            calculator.click_button("7")

        with allure.step("Ввод знака '+'"):
            calculator.click_button("+")

        with allure.step("Ввод числа '8'"):
            calculator.click_button("8")

        with allure.step("Нажатие '=' для вычисления"):
            calculator.click_button("=")

        with allure.step("Ожидание появления результата '15'"):
            wait = WebDriverWait(driver, 46)
            wait.until(
                EC.text_to_be_present_in_element(calculator.result_locator, "15")
            )

        with allure.step("Получение результата вычисления"):
            result = calculator.get_result()

        with allure.step(f"Проверка результата ('15') против полученного ('{result}')"):
            assert result == "15", f"Expected '15', but got '{result}'"

    finally:
        driver.quit()
