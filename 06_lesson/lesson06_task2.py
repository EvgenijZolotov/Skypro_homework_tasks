from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

try:
    # Шаг 1: Открытие страницы
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: Ввод текста в поле
    driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

    # Шаг 3: Клик по кнопке
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Шаг 4: Ожидание обновления текста
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Шаг 5: Проверка и вывод результата
    print(driver.find_element(By.ID, "updatingButton").text)

finally:
    driver.quit()
