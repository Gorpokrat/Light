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
    driver.get('http://uitestingplayground.com/ajax')

    # Нажатие на кнопку AJAX
    driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

    # Явное ожидание появления элемента с классом 'p.bg-success'
    wait = WebDriverWait(driver, 20)
    element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
    )

    # Вывод текста элемента
    print(element.text)

finally:
    # Закрытие браузера
    driver.quit()
