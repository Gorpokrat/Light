from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Переход на страницу
    driver.get('http://uitestingplayground.com/textinput')

    # Находим поле ввода по ID для улучшения читаемости
    input_field = driver.find_element(By.ID, 'newButtonName')
    input_field.send_keys('SkyPro')

    # Находим кнопку по ID и кликаем по ней
    update_button = driver.find_element(By.ID, 'updatingButton')
    update_button.click()

    # Ждём, пока текст кнопки обновится до ожидаемого значения
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro')
    )

    # Получаем и выводим обновлённый текст кнопки
    updated_text = driver.find_element(By.ID, 'updatingButton').text
    print(updated_text)

finally:
    driver.quit()
