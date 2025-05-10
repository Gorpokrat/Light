from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    service = Service()  # например: Service('/path/to/chromedriver')
    options = webdriver.ChromeOptions()
   

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")

        wait = WebDriverWait(driver, 10)


        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))

        button.click()

    finally:
        driver.quit()

if __name__ == "__main__":
    main()