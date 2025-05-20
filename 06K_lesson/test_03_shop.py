from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_flow():
    # Инициализация драйвера (здесь используется Chrome)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизация как пользователь standard_user
        username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # 3. Добавляем товары в корзину
        # Названия товаров:
        # - Sauce Labs Backpack
        # - Sauce Labs Bolt T-Shirt
        # - Sauce Labs Onesie

        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            # Находим карточку товара по названию и добавляем в корзину
            product_xpath = f"//div[@class='inventory_item']//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            add_button = wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath)))
            add_button.click()

        # 4. Перейти в корзину
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

        # 5. Нажать Checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Заполнить форму своими данными: имя, фамилия, почтовый индекс
        first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")
        
        first_name_input.send_keys("Иван")
        last_name_input.send_keys("Иванов")
        postal_code_input.send_keys("12345")

        # 7. Нажать кнопку Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # 8. Прочитать итоговую стоимость (Total)
        total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text  # например: 'Total: $58.29'
        
        print(f"Итоговая сумма на странице: {total_text}")

    finally:
        # 9. Закрыть браузер
        driver.quit()

    # 10. Проверка итоговой суммы равна $58.29
    assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получена {total_text}"

if __name__ == "__main__":
    test_shopping_flow()
