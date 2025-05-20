# test_02_calc.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_slow_calculator():
    # Инициализация драйвера (здесь используется Chrome, убедитесь, что chromedriver установлен и в PATH)
    driver = webdriver.Chrome()

    try:
        # Открываем страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        # Вводим значение 45 в поле #delay
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        # Нажимаем кнопку "7"
        button_7 = driver.find_element(By.XPATH, "//button[text()='7']")
        button_7.click()
        
        # Нажимаем кнопку "+"
        plus_button = driver.find_element(By.XPATH, "//button[text()='+']")
        plus_button.click()
        
        # Нажимаем кнопку "8"
        button_8 = driver.find_element(By.XPATH, "//button[text()='8']")
        button_8.click()
        
        # Нажимаем "="
        equals_button = driver.find_element(By.XPATH, "//button[text()='=']")
        equals_button.click()
        
        # Ждем примерно 45 секунд для отображения результата
        time.sleep(45)
        
        # Получаем результат из элемента с id "result"
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text.strip()
        
        # Проверяем, что результат равен "15"
        assert result_text == "15", f"Expected result to be '15', but got '{result_text}'"
        
    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    test_slow_calculator()
