from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем, пока появится элемент с текстом "Done!"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )
    
    # Получаем src третьей картинки по CSS-селектору
    third_image_src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
    
    print("SRC третья картинка:", third_image_src)
finally:
    # Закрываем браузер
    driver.quit()
