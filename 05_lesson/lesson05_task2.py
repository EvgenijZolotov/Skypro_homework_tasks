from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def click_dynamic_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
        input("Нажмите Enter для закрытия...")
    finally:
        driver.quit()


if __name__ == "__main__":
    click_dynamic_button()
