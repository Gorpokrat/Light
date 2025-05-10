from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    options = webdriver.FirefoxOptions()
    
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        wait = WebDriverWait(driver, 10)

        # Находим поле ввода по его тегу <input>
        input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

        # Вводим текст "Sky"
        input_field.send_keys("Sky")

        # Очищаем поле ввода
        input_field.clear()

        # Вводим текст "Pro"
        input_field.send_keys("Pro")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()