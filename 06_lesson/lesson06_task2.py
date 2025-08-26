from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Автоматическая установка драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

try:
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    driver.find_element(By.ID, "updatingButton").click()

    button_text = driver.find_element(By.ID, "updatingButton").text
    print("Текст кнопки:", button_text)

    # Увеличенное время показа - 5 секунд
    time.sleep(5)

finally:
    driver.quit()
