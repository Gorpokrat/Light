from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait


def main():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/classattr")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        button.click()

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
