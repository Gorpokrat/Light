from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def main():
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        time.sleep(1)
        button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

        button.click()

        time.sleep(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
