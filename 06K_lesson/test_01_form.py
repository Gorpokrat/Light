from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для проверки цвета рамки поля
def check_border_color(element):
    # Получаем цвет рамки через CSS свойства
    border_color = element.value_of_css_property('border-color')
    return border_color

# Основной тест
def test_form_submission():
    # Инициализация драйвера (здесь используется Chrome)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Заполняем форму значениями
        # Предположим, что у каждого поля есть уникальный id или name.
        # Если нет, можно искать по label или другим селекторам.

        # Внимание: В реальной ситуации нужно проверить структуру страницы.
        # Ниже пример с использованием label текста и поиска соответствующих input.

        def fill_input(label_text, value):
            label = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//label[contains(text(), '{label_text}')]")
            ))
            input_id = label.get_attribute('for')
            input_element = driver.find_element(By.ID, input_id)
            input_element.clear()
            input_element.send_keys(value)
            return input_element

        # Заполняем поля
        fill_input("First name", "Иван")
        fill_input("Last name", "Петров")
        fill_input("Address", "Ленина, 55-3")
        fill_input("Email", "test@skypro.com")
        fill_input("Phone number", "+7985899998787")
        fill_input("Zip code", "")  # оставляем пустым
        fill_input("City", "Москва")
        fill_input("Country", "Россия")
        fill_input("Job position", "QA")
        fill_input("Company", "SkyPro")

        # Нажимаем кнопку Submit
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Submit')]")
        ))
        submit_button.click()

        # После отправки формы предполагается подсветка полей.
        # Проверяем цвет рамки каждого поля.

        # Определим функцию для проверки цвета подсветки:
        def is_field_highlighted_in_color(field_element, expected_color):
            color = check_border_color(field_element)
            return expected_color in color

        # Ожидаем появления подсветки (может потребоваться небольшая задержка)
        
        # Поля для проверки: создадим список кортежей (имя поля, ожидаемый цвет)
        fields_colors = [
            ("Zip code", "rgb(255, 0, 0)"),   # красный
            ("First name", "rgb(0, 128, 0)"), # зеленый
            ("Last name", "rgb(0, 128, 0)"),
            ("Address", "rgb(0, 128, 0)"),
            ("Email", "rgb(0, 128, 0)"),
            ("Phone number", "rgb(0, 128, 0)"),
            ("City", "rgb(0, 128, 0)"),
            ("Country", "rgb(0, 128, 0)"),
            ("Job position", "rgb(0, 128, 0)"),
            ("Company", "rgb(0, 128, 0)")
        ]

        for field_name, expected_rgb in fields_colors:
            label = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//label[contains(text(), '{field_name}')]")
            ))
            input_id = label.get_attribute('for')
            field_element = driver.find_element(By.ID, input_id)

            if field_name == "Zip code":
                assert is_field_highlighted_in_color(field_element, expected_rgb), \
                    f"{field_name} не подсвечен красным"
            else:
                assert is_field_highlighted_in_color(field_element, expected_rgb), \
                    f"{field_name} не подсвечен зеленым"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_form_submission()
