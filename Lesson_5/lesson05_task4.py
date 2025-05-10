from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
   
    options = webdriver.FirefoxOptions()
    
    driver = webdriver.Firefox()

    try:
        driver.get("http://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Ждем появления зеленой плашки с сообщением об успешном входе
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success")))

        # Выводим текст сообщения в консоль
        print(success_message.text)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
