import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Calculator_page import CalculatorPage

@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы калькулятора с задержкой 45 секунд. "
                    "Вводим выражение 7 + 8 = и ожидаем результат 15.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture(scope="function")
def driver():
    with allure.step("Инициализация драйвера Chrome"):
        driver_instance = webdriver.Chrome()
    yield driver_instance
    with allure.step("Закрытие драйвера Chrome"):
        driver_instance.quit()

@allure.step("Выполнение теста медленного калькулятора")
def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        calculator.open()

    with allure.step("Устанавливаем задержку 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Вводим число 7"):
        calculator.click_button("7")

    with allure.step("Вводим оператор '+'"):
        calculator.click_button("+")

    with allure.step("Вводим число 8"):
        calculator.click_button("8")

    with allure.step("Нажимаем '=' для вычисления"):
        calculator.click_button("=")

    wait_time = 46  # чуть больше задержки для надежности

    with allure.step(f"Ожидаем появления результата '15' в течение {wait_time} секунд"):
        wait = WebDriverWait(driver, wait_time)
           
        EC.text_to_be_present_in_element(calculator.result_locator, "15")(driver)
            # или можно использовать wait.until(...)
        wait.until(EC.text_to_be_present_in_element(calculator.result_locator, "15"))
            
    with allure.step("Результат '15' появился успешно"):
         result = calculator.get_result()
            
    with allure.step(f"Проверяем, что результат равен '15', полученное значение: '{result}'"):
         assert result == "15", f"Expected '15', but got '{result}'"
                
    with allure.step("Тест завершен успешно"):
                pass
           