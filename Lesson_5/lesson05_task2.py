from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    
    options = webdriver.ChromeOptions()
   

    driver = webdriver.Chrome()

        driver.get("http://uitestingplayground.com/dynamicid")

        wait = WebDriverWait(driver, 10)


       button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
)

button.click()

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
